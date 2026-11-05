"""Adversarial contract fixtures only: these tests do not run or certify CUDA,
submit real review records, or verify any person's identity.
"""
import copy
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch
import urllib.error
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import independent_review_gate as review
import release_readiness_3152 as release


class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.rows = []
        for lesson_id in ("A01.01", "N01.01", "PR01.01"):
            folder = self.root / "03_HOC_PHAN/FIXTURE"
            files = {
                "lesson_sha256": folder / "BAI_HOC" / (lesson_id + ".md"),
                "answer_sha256": folder / "LOI_GIAI" / (lesson_id + "_loi_giai.md"),
                "demo_sha256": folder / "MA_MAU" / (lesson_id + "_demo.py")}
            if lesson_id == "A01.01":
                files["solution_code_sha256"] = self.root / "31_HOAN_THIEN_LOI_GIAI_V28" / (lesson_id + "_bai_B_solution.py")
            for file in files.values():
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text("SYNTHETIC CONTRACT FIXTURE ONLY\n", encoding="utf8")
            for login in (("fixture-a",) if lesson_id == "A01.01" else ("fixture-a", "fixture-b")):
                row = dict.fromkeys(review.FIELDS, "")
                row.update({key: review.filehash(file) for key, file in files.items()})
                row.update(lesson_id=lesson_id, reviewer_github=login,
                           reviewer_affiliation="SYNTHETIC FIXTURE, NOT A SIGNOFF",
                           independence_declaration="CONFIRMED_NO_CONFLICT",
                           review_date_utc="2026-01-01", decision="ACCEPTED",
                           review_evidence_url="https://github.com/fixture/repo/pull/1#pullrequestreview-1",
                           adversarial_case_url="https://github.com/fixture/repo/actions/runs/2")
                row.update(dict.fromkeys(review.SCORE_FIELDS, "3"))
                self.rows.append(row)

    def check(self, rows=None):
        return review.validate_records(self.root, self.rows if rows is None else rows,
                                       expected_lessons=3, today=date(2026, 11, 5))

    def assertPending(self, rows=None):
        result = self.check(rows)
        self.assertEqual(result["review_manifest_state"], "EVIDENCE_PENDING")
        self.assertEqual(result["academic_certification"], "NOT_GRANTED_AUTOMATICALLY")
        return result

    def test_complete_fixture_still_needs_human_verification(self):
        result = self.check()
        self.assertEqual(result["review_manifest_state"], "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK")
        self.assertEqual(result["reviewer_identity_verification"], "REQUIRES_HUMAN_VERIFICATION")
        self.assertEqual(result["academic_certification"], "NOT_GRANTED_AUTOMATICALLY")

    def test_empty_and_missing_lesson_records_block(self):
        self.assertPending([])
        self.assertPending(self.rows[1:])

    def test_one_high_risk_reviewer_cannot_count_twice_by_case(self):
        self.rows[2]["reviewer_github"] = self.rows[1]["reviewer_github"].upper()
        result = self.assertPending()
        self.assertEqual(result["high_risk_lessons_requiring_second_review_count"], 1)

    def test_each_changed_source_invalidates_its_record(self):
        for field, relative in (
            ("lesson", "03_HOC_PHAN/FIXTURE/BAI_HOC/A01.01.md"),
            ("answer", "03_HOC_PHAN/FIXTURE/LOI_GIAI/A01.01_loi_giai.md"),
            ("demo", "03_HOC_PHAN/FIXTURE/MA_MAU/A01.01_demo.py"),
            ("B code", "31_HOAN_THIEN_LOI_GIAI_V28/A01.01_bai_B_solution.py")):
            with self.subTest(field=field):
                file = self.root / relative
                original = file.read_bytes()
                file.write_bytes(original + b"changed\n")
                self.assertPending()
                file.write_bytes(original)

    def test_missing_demo_or_b_checksum_blocks(self):
        for key in ("demo_sha256", "solution_code_sha256"):
            with self.subTest(key=key):
                rows = copy.deepcopy(self.rows)
                rows[0][key] = ""
                self.assertPending(rows)

    def test_invalid_or_future_dates_block(self):
        for text in ("2026-99-99", "2026-02-30", "2027-01-01", "2026-1-1", ""):
            with self.subTest(text=text):
                rows = copy.deepcopy(self.rows)
                rows[0]["review_date_utc"] = text
                self.assertPending(rows)

    def test_author_ai_bot_and_invalid_logins_block(self):
        for login in ("Nguyen-Quoc-Thanh-14", "CHATGPT", "copilot", "robot[bot]", "bad--login", ""):
            with self.subTest(login=login):
                rows = copy.deepcopy(self.rows)
                rows[0]["reviewer_github"] = login
                self.assertPending(rows)

    def test_finding_requires_both_fix_and_retest(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["findings_issue_urls"] = "https://github.com/fixture/repo/issues/3"
        self.assertPending(rows)
        rows[0]["fix_commit_sha"] = "a" * 40
        self.assertPending(rows)
        rows[0]["retest_evidence_url"] = "https://github.com/fixture/repo/actions/runs/4"
        self.assertEqual(self.check(rows)["review_manifest_state"],
                         "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK")

    def test_bad_fix_sha_or_retest_url_blocks(self):
        for key, bad in (("fix_commit_sha", "abcd"),
                         ("retest_evidence_url", "https://github.com.evil.invalid/repo/issues/3")):
            with self.subTest(key=key):
                rows = copy.deepcopy(self.rows)
                rows[0].update(findings_issue_urls="https://github.com/fixture/repo/issues/3",
                               fix_commit_sha="a" * 40,
                               retest_evidence_url="https://github.com/fixture/repo/actions/runs/4")
                rows[0][key] = bad
                self.assertPending(rows)

    def test_bad_urls_and_scores_block(self):
        for key, bad in (("review_evidence_url", "https://github.com/"),
                         ("adversarial_case_url", "https://github.com@evil.invalid/a/b/issues/1"),
                         ("findings_issue_urls", "not a URL"),
                         ("technical_0_4", "2"), ("safety_0_4", "5"),
                         ("compatibility_0_4", "NaN"), ("decision", "CHANGES_REQUESTED"),
                         ("independence_declaration", ""), ("reviewer_affiliation", "")):
            with self.subTest(key=key):
                rows = copy.deepcopy(self.rows)
                rows[0][key] = bad
                self.assertPending(rows)

    def test_malformed_csv_rows_and_wrong_inventory_block(self):
        rows = copy.deepcopy(self.rows)
        rows[0][None] = ["extra CSV cell"]
        self.assertPending(rows)
        result = review.validate_records(self.root, self.rows)
        self.assertEqual(result["review_manifest_state"], "EVIDENCE_PENDING")
        self.assertGreater(result["problems_count"], 0)


class CudaArtifactTests(unittest.TestCase):
    def setUp(self):
        self.repo = "fixture/repo"
        self.sha = "a" * 40
        self.source_hash = "b" * 64
        self.run = {"id": 17, "run_number": 3, "run_attempt": 2,
                    "head_sha": self.sha, "head_branch": "audit/full-course-536",
                    "path": ".github/workflows/gpu-self-hosted-3152.yml",
                    "event": "workflow_dispatch", "status": "completed", "conclusion": "success"}
        self.observed = {
            "status": "CUDA_HARDWARE_PASS", "repository": self.repo, "commit_sha": self.sha,
            "run_id": "17", "run_attempt": "2", "source_sha256": self.source_hash,
            "python_version": "3.15.2", "torch_version": "2.15.0+fixture",
            "platform_system": "Linux", "platform_machine": "x86_64",
            "cuda_available": True, "torch_cuda_runtime": "SYNTHETIC",
            "device_name": "SYNTHETIC TEST DEVICE, NOT HARDWARE EVIDENCE",
            "device_memory_bytes": 1024, "nvidia_smi": "SYNTHETIC CONTRACT FIXTURE ONLY",
            "device_compute_capability": [7,5], "torch_cuda_arches": ["sm_75"],
            "analytic_gradient_observed": [-4.0, 0.0, 6.0],
            "convolution_cpu_gpu_close": True, "initial_mse": 9.0, "final_mse": 0.001,
            "prediction_x3": 6.999}
        self.job = {"id": 19, "name": "gpu-evidence", "status": "completed", "conclusion": "success",
                    "labels": ["self-hosted", "Linux", "X64", "gpu"],
                    "runner_id": 7, "runner_name": "synthetic-fixture"}

    def bundle(self, observed=None, *, name="gpu_runtime.json", duplicate=False):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as z:
            z.writestr(name, json.dumps(self.observed if observed is None else observed))
            if duplicate:
                z.writestr("cuda_3152/gpu_runtime.json", json.dumps(self.observed))
        raw = stream.getvalue()
        meta = {"id": 23, "name": release.ARTIFACTS["gpu"], "expired": False,
                "digest": "sha256:" + hashlib.sha256(raw).hexdigest(),
                "workflow_run": {"id": 17, "head_sha": self.sha}}
        return raw, meta

    def validate(self, raw, meta):
        return release.validate_cuda_artifact(raw, meta, self.run, self.source_hash, self.repo)

    def test_synthetic_well_formed_observation_parses(self):
        self.assertEqual(self.validate(*self.bundle()), self.observed)

    def test_absent_duplicate_or_malformed_report_blocks(self):
        for options in ({"name": "different.json"}, {"duplicate": True}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                self.validate(*self.bundle(**options))
        raw, meta = self.bundle()
        meta["digest"] = "sha256:" + hashlib.sha256(b"not zip").hexdigest()
        with self.assertRaises(zipfile.BadZipFile):
            self.validate(b"not zip", meta)

    def test_tampered_expired_or_wrong_artifact_blocks(self):
        raw, meta = self.bundle()
        for key, bad in (("digest", "sha256:" + "0" * 64), ("expired", True),
                         ("name", "wrong"), ("workflow_run", {"id": 18, "head_sha": self.sha})):
            with self.subTest(key=key), self.assertRaises(ValueError):
                changed = copy.deepcopy(meta)
                changed[key] = bad
                self.validate(raw, changed)

    def test_stale_provenance_failed_cpu_only_and_bad_numeric_results_block(self):
        for key, bad in (
            ("commit_sha", "c" * 40), ("repository", "other/repo"),
            ("run_id", "99"), ("run_attempt", "1"), ("source_sha256", "c" * 64),
            ("status", "CUDA_HARDWARE_FAIL"), ("python_version", "3.12.14"),
            ("torch_version", "2.14.0"), ("platform_system", "Windows"),
            ("cuda_available", False), ("torch_cuda_runtime", None),
            ("device_name", ""), ("device_memory_bytes", 0), ("nvidia_smi", ""),
            ("device_compute_capability", [5,2]), ("device_compute_capability", [7]),
            ("device_compute_capability", ["7","5"]), ("torch_cuda_arches", None),
            ("analytic_gradient_observed", [0, 0, 0]), ("convolution_cpu_gpu_close", False),
            ("initial_mse", float("nan")), ("final_mse", float("inf")),
            ("final_mse", -1.0), ("final_mse", 2.0), ("prediction_x3", 0.0)):
            with self.subTest(key=key, bad=bad), self.assertRaises(ValueError):
                observed = {**self.observed, key: bad}
                self.validate(*self.bundle(observed))

    def test_successful_gpu_job_requires_runner_labels_and_observations(self):
        self.assertEqual(release.validate_gpu_job([self.job])["runner_id"], 7)
        for key, bad in (("labels", ["ubuntu-latest"]), ("runner_id", None),
                         ("runner_name", ""), ("conclusion", "failure"), ("status", "queued")):
            with self.subTest(key=key), self.assertRaises(ValueError):
                release.validate_gpu_job([{**self.job, key: bad}])
        with self.assertRaises(ValueError):
            release.validate_gpu_job([])

    def test_new_failure_or_queued_run_overrides_earlier_success(self):
        for status in ("completed", "queued"):
            with self.subTest(status=status):
                newer = {**self.run, "id": 18, "run_number": 4, "status": status, "conclusion": "failure"}
                with patch.object(release, "SHA", self.sha), patch.object(release, "get_pages") as api:
                    proof = release.collect_workflow_proof("gpu", [self.run, newer])
                self.assertFalse(proof["passed"])
                self.assertEqual(proof["run_id"], 18)
                api.assert_not_called()

    def test_no_evidence_from_a_different_commit_or_workflow_path(self):
        self.assertIsNone(release.select_latest_run([self.run], release.WORKFLOWS["gpu"], "d" * 40))
        altered = {**self.run, "path": "untrusted/gpu-self-hosted-3152.yml"}
        self.assertIsNone(release.select_latest_run([altered], release.WORKFLOWS["gpu"], self.sha))

    def test_complete_gpu_proof_inspects_archive_and_job(self):
        raw, meta = self.bundle()
        collector = MagicMock()
        collector.read_bytes.return_value = b"fixture collector"
        source_hash = hashlib.sha256(b"fixture collector").hexdigest()
        raw, meta = self.bundle({**self.observed, "source_sha256": source_hash})
        with patch.object(release, "SHA", self.sha), patch.object(release, "REPO", self.repo), \
             patch.object(release, "ROOT") as root, \
             patch.object(release, "get_pages", side_effect=[[meta], [self.job]]), \
             patch.object(release, "download_artifact", return_value=raw) as download:
            root.__truediv__.return_value = collector
            proof = release.collect_workflow_proof("gpu", [self.run])
        self.assertTrue(proof["passed"])
        self.assertTrue(proof["artifact_content_verified"])
        download.assert_called_once_with(23)

    def test_artifact_name_alone_or_wrong_trigger_cannot_pass(self):
        raw, meta = self.bundle()
        for run, artifacts in ((self.run, []), ({**self.run, "event": "push"}, [meta])):
            with self.subTest(run=run["event"], artifacts=len(artifacts)), \
                 patch.object(release, "SHA", self.sha), \
                 patch.object(release, "get_pages", return_value=artifacts), \
                 patch.object(release, "download_artifact") as download:
                self.assertFalse(release.collect_workflow_proof("gpu", [run])["passed"])
                download.assert_not_called()

    def test_signed_download_does_not_forward_github_token(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"fixture ZIP"
        redirected = urllib.error.HTTPError("https://api.github.com/test", 302, "Found",
                    {"Location": "https://storage.example.invalid/signed"}, io.BytesIO())
        opener = MagicMock()
        opener.open.side_effect = redirected
        with patch.object(release, "TOKEN", "synthetic-token"), \
             patch.object(release.urllib.request, "build_opener", return_value=opener), \
             patch.object(release.urllib.request, "urlopen", return_value=response) as follow:
            self.assertEqual(release.download_artifact(23), b"fixture ZIP")
        request = follow.call_args.args[0]
        self.assertIsNone(request.get_header("Authorization"))

    def test_unsafe_redirect_and_oversized_download_block(self):
        opener = MagicMock()
        opener.open.side_effect = urllib.error.HTTPError(
            "https://api.github.com/test", 302, "Found",
            {"Location": "http://unsafe.invalid/file"}, io.BytesIO())
        with patch.object(release, "TOKEN", "synthetic-token"), \
             patch.object(release.urllib.request, "build_opener", return_value=opener), \
             patch.object(release.urllib.request, "urlopen") as follow, \
             self.assertRaises(ValueError):
            release.download_artifact(23)
        follow.assert_not_called()
        with self.assertRaises(ValueError):
            release.read_bounded(io.BytesIO(b"12345"), 4)


if __name__ == "__main__":
    unittest.main()
