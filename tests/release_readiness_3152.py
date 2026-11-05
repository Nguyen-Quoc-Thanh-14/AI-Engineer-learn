#!/usr/bin/env python3
"""Fail-closed evidence audit; even complete records require a human final audit."""
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/release_readiness_3152.json"
REPO = os.getenv("GITHUB_REPOSITORY", "Nguyen-Quoc-Thanh-14/AI-Engineer-learn")
SHA = os.getenv("GITHUB_SHA", "")
TOKEN = os.getenv("GH_TOKEN", "")
WORKFLOWS = {
    "cpu": "full-course-3152.yml",
    "semantic": "semantic-contracts-3152.yml",
    "structural": "curriculum-quality-audit.yml",
    "native": "course-native-pr02-3152.yml",
    "gpu": "gpu-self-hosted-3152.yml"}
ARTIFACTS = {"cpu": "complete-cpython-3152-cpu-evidence",
             "gpu": "actual-cuda-cpython3152-evidence"}
MAX_CUDA_ZIP = 5 * 1024 * 1024


def api_request(path):
    if not TOKEN:
        raise RuntimeError("Missing GitHub Actions read token")
    return urllib.request.Request(
        "https://api.github.com/repos/" + REPO + "/" + path,
        headers={"Authorization": "Bearer " + TOKEN,
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "course-release-readiness"})


def get_api(path):
    with urllib.request.urlopen(api_request(path), timeout=20) as reply:
        return json.load(reply)


def get_pages(path, field):
    result = []
    for page in range(1, 21):
        data = get_api(path + ("&" if "?" in path else "?") + f"per_page=100&page={page}")
        items = data[field]
        result.extend(items)
        if len(items) < 100:
            return result
    raise RuntimeError("Pagination limit reached; refusing incomplete evidence inventory")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def read_bounded(reply, limit):
    data = reply.read(limit + 1)
    if len(data) > limit:
        raise ValueError("CUDA artifact exceeds allowed archive size")
    return data


def download_artifact(artifact_id):
    """Do not forward the GitHub token to the signed storage redirect."""
    request = api_request(f"actions/artifacts/{artifact_id}/zip")
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=30) as reply:
            return read_bounded(reply, MAX_CUDA_ZIP)
    except urllib.error.HTTPError as exc:
        if exc.code != 302:
            raise
        location = exc.headers.get("Location", "")
        exc.close()
    destination = urllib.parse.urlsplit(location)
    if destination.scheme != "https" or not destination.hostname or destination.username or destination.password:
        raise ValueError("Unsafe or missing artifact download redirect")
    with urllib.request.urlopen(urllib.request.Request(location), timeout=30) as reply:
        return read_bounded(reply, MAX_CUDA_ZIP)


def select_latest_run(candidates, workflow, sha):
    matches = [r for r in candidates if r.get("head_sha") == sha
               and str(r.get("path", "")).split("@")[0] == ".github/workflows/" + workflow]
    return max(matches, key=lambda r: (r.get("run_number", 0), r.get("id", 0))) if matches else None


def validate_gpu_job(jobs):
    found = [j for j in jobs if j.get("name") == "gpu-evidence"]
    if len(found) != 1:
        raise ValueError("Exactly one GPU evidence job is required")
    job = found[0]
    required = {"self-hosted", "linux", "x64", "gpu"}
    labels = {str(label).casefold() for label in job.get("labels", [])}
    if (job.get("status") != "completed" or job.get("conclusion") != "success"
            or not required <= labels or not job.get("runner_id") or not job.get("runner_name")):
        raise ValueError("Missing successful trusted self-hosted GPU job metadata")
    return {"job_id": job["id"], "runner_id": job["runner_id"],
            "runner_name": job["runner_name"], "labels": sorted(labels)}


def validate_cuda_artifact(archive, artifact, run, source_sha256, repository):
    """Inspect immutable ZIP bytes and the observed result, not just its name."""
    def require(condition, message):
        if not condition:
            raise ValueError(message)

    require(len(archive) <= MAX_CUDA_ZIP, "CUDA archive too large")
    digest = "sha256:" + hashlib.sha256(archive).hexdigest()
    require(artifact.get("digest") == digest, "CUDA archive digest mismatch or missing digest")
    require(artifact.get("name") == ARTIFACTS["gpu"] and artifact.get("expired") is False,
            "Wrong or expired CUDA artifact")
    origin = artifact.get("workflow_run", {})
    require(origin.get("id") == run["id"] and origin.get("head_sha") == run["head_sha"],
            "Artifact metadata belongs to another commit/run")
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        names = {"gpu_runtime.json", "cuda_3152/gpu_runtime.json",
                 "evidence/cuda_3152/gpu_runtime.json"}
        reports = [entry for entry in bundle.infolist() if entry.filename in names]
        require(len(reports) == 1, "Missing or duplicate CUDA runtime JSON")
        require(reports[0].file_size <= 256 * 1024, "CUDA JSON is too large")
        observed = json.loads(bundle.read(reports[0]).decode("utf8"))
    require(isinstance(observed, dict), "CUDA JSON must be an object")
    require(observed.get("status") == "CUDA_HARDWARE_PASS", "CUDA execution did not pass")
    require(observed.get("repository") == repository, "CUDA result belongs to another repository")
    require(observed.get("commit_sha") == run["head_sha"], "CUDA JSON commit mismatch")
    for key in ("run_id", "run_attempt"):
        require(str(observed.get(key, "")) == str(run.get(key if key == "run_attempt" else "id", "")),
                "CUDA JSON " + key + " mismatch")
    require(observed.get("source_sha256") == source_sha256, "Stale CUDA collector source hash")
    require(observed.get("python_version") == "3.15.2", "Wrong CUDA Python runtime")
    require(str(observed.get("torch_version", "")).split("+")[0] == "2.15.0", "Wrong CUDA PyTorch version")
    require(observed.get("platform_system") == "Linux" and observed.get("platform_machine") == "x86_64",
            "Unsupported CUDA platform")
    require(observed.get("cuda_available") is True and bool(observed.get("torch_cuda_runtime")),
            "CPU-only or unavailable CUDA runtime")
    require(isinstance(observed.get("device_name"), str) and bool(observed["device_name"].strip())
            and isinstance(observed.get("nvidia_smi"), str) and bool(observed["nvidia_smi"].strip()),
            "Missing NVIDIA hardware observations")
    memory = observed.get("device_memory_bytes")
    require(type(memory) is int and memory > 0, "Invalid device memory observation")
    require(observed.get("analytic_gradient_observed") == [-4.0, 0.0, 6.0], "Wrong CUDA gradient")
    require(observed.get("convolution_cpu_gpu_close") is True, "Missing CPU/GPU convolution comparison")
    initial, final, prediction = (observed.get(k) for k in ("initial_mse", "final_mse", "prediction_x3"))
    require(all(type(v) in (int, float) and math.isfinite(v) for v in (initial, final, prediction)),
            "Missing or non-finite training observations")
    require(initial == 9.0 and 0 <= final < initial * 0.01 and abs(prediction - 7.0) < 0.1,
            "CUDA training did not meet the collector's acceptance criteria")
    return observed


def collect_workflow_proof(group, candidates):
    latest = select_latest_run(candidates, WORKFLOWS[group], SHA)
    if latest is None:
        return {"passed": False, "reason": "NO_RUN_ON_EXACT_SHA"}
    proof = {"passed": False, "run_id": latest["id"], "url": latest.get("html_url"),
             "sha": latest.get("head_sha"), "run_attempt": latest.get("run_attempt")}
    if latest.get("status") != "completed" or latest.get("conclusion") != "success":
        return {**proof, "reason": "LATEST_RUN_NOT_SUCCESSFUL"}
    if group not in ARTIFACTS:
        return {**proof, "passed": True}
    artifacts = get_pages(f"actions/runs/{latest['id']}/artifacts", "artifacts")
    found = [a for a in artifacts if a.get("name") == ARTIFACTS[group] and a.get("expired") is False]
    if len(found) != 1:
        return {**proof, "reason": "MISSING_OR_AMBIGUOUS_ARTIFACT"}
    artifact = found[0]
    origin = artifact.get("workflow_run", {})
    if origin.get("id") != latest["id"] or origin.get("head_sha") != SHA:
        return {**proof, "reason": "ARTIFACT_PROVENANCE_MISMATCH"}
    proof["artifact_id"] = artifact["id"]
    if group == "gpu":
        if latest.get("event") != "workflow_dispatch" or latest.get("head_branch") != "audit/full-course-536":
            return {**proof, "reason": "UNEXPECTED_GPU_WORKFLOW_TRIGGER"}
        proof["hardware_job"] = validate_gpu_job(get_pages(f"actions/runs/{latest['id']}/jobs", "jobs"))
        collector_hash = hashlib.sha256((ROOT / "tests/gpu_cuda_3152.py").read_bytes()).hexdigest()
        observed = validate_cuda_artifact(download_artifact(artifact["id"]), artifact, latest, collector_hash, REPO)
        proof.update(artifact_content_verified=True, device_name=observed["device_name"],
                     cuda_status=observed["status"], artifact_digest=artifact["digest"])
    return {**proof, "passed": True}


def run():
    if sys.implementation.name != "cpython" or sys.version_info[:3] != (3, 15, 2):
        raise RuntimeError("Release evidence audit requires CPython 3.15.2")
    OUT.parent.mkdir(exist_ok=True, parents=True)
    lessons = list(ROOT.glob("03_HOC_PHAN/**/BAI_HOC/*.md"))
    demos = list(ROOT.glob("03_HOC_PHAN/**/MA_MAU/*_demo.py"))
    solutions = list(ROOT.glob("31_HOAN_THIEN_LOI_GIAI_V28/*_bai_B_solution.py"))
    checks = {
        "inventory": len(lessons) == 441 and len(demos) == 441
        and len({p.stem for p in lessons}) == 441
        and {p.stem for p in lessons} == {p.name.removesuffix("_demo.py") for p in demos}
        and len(solutions) == 95,
        "sha_format": bool(re.fullmatch(r"[0-9a-f]{40}", SHA))}
    proofs, errors, pr = {}, [], {}
    if checks["sha_format"] and TOKEN:
        try:
            candidates = get_pages("actions/runs?head_sha=" + SHA, "workflow_runs")
            for group in WORKFLOWS:
                try:
                    proofs[group] = collect_workflow_proof(group, candidates)
                except Exception as exc:
                    proofs[group] = {"passed": False, "reason": type(exc).__name__ + ": " + str(exc)[:200]}
            pull = get_api("pulls/4")
            pr = {"draft": pull.get("draft"), "state": pull.get("state"),
                  "merged": pull.get("merged", False), "head_sha": pull.get("head", {}).get("sha")}
            checks["pr_draft_unmerged"] = pr["draft"] is True and pr["state"] == "open" and not pr["merged"]
            checks["pr_sha_matches"] = pr["head_sha"] == SHA
        except Exception as exc:
            errors.append(type(exc).__name__ + ": " + str(exc)[:200])
    else:
        errors.append("Missing commit SHA or GitHub API credentials")
    for group in WORKFLOWS:
        checks["workflow_" + group] = proofs.get(group, {}).get("passed", False)
    try:
        proc = subprocess.run([sys.executable, str(ROOT / "tests/independent_review_gate.py")],
                              cwd=ROOT, capture_output=True, text=True, timeout=30)
        review = json.loads((ROOT / "evidence/independent_review_gate.json").read_text(encoding="utf8"))
        checks["review_manifest_complete"] = (proc.returncode == 0 and
            review.get("review_manifest_state") == "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK")
    except Exception as exc:
        review = {"error": type(exc).__name__ + ": " + str(exc)}
        checks["review_manifest_complete"] = False
    ready = all(checks.values()) and not errors
    report = {"status": "ELIGIBLE_FOR_HUMAN_FINAL_AUDIT" if ready else "BLOCKED",
              "academic_certification": "NOT_GRANTED_AUTOMATICALLY",
              "runtime": sys.version, "sha": SHA, "checks": checks,
              "workflow_proofs": proofs, "pr": pr, "review": review, "errors": errors,
              "caveat": "Runner labels, artifacts and declarations cannot authenticate independent experts or academic quality. Human identity, independence and content verification remain mandatory."}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps({"status": report["status"], "sha": SHA, "checks": checks, "errors": errors}, ensure_ascii=False))
    return 0 if ready else 3


if __name__ == "__main__":
    raise SystemExit(run())

