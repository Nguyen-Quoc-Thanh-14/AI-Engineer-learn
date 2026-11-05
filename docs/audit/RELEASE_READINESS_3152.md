# Release evidence needed before final certification

Draft PR #4 stays unmerged. Automated CPU/Keras checks do not prove actual NVIDIA CUDA execution or independent academic quality.

The new CI readiness workflow checks that test runs belong to the exact PR head SHA, that successful CPU/GPU runs have unexpired artifacts, and that the reviewer manifest covers every lesson. If evidence is missing, the workflow fails and uploads a JSON report listing the missing checks.

Issue #8: A trusted Linux x64 NVIDIA runner must be registered and labeled gpu, then the workflow gpu-self-hosted-3152.yml must be run on branch audit/full-course-536. A CUDA wheel or CPU emulation does not count.

Issue #7: Independent verified human experts must review the lesson, demo and B answer for each of 441 lessons, file rubric and SHA-linked evidence, fix defects and sign off without conflicts. A manifest alone cannot authenticate actual expertise; the final decision is human.

Even with a green automated gate the status is only ELIGIBLE_FOR_HUMAN_FINAL_AUDIT, never ACADEMICALLY_CERTIFIED. Keep the PR draft until the external blockers are genuinely resolved.

## Evidence validation hardening — 05/11/2026

- CUDA eligibility requires the artifact ZIP digest, runtime JSON contents, exact commit/run/attempt, collector hash, successful self-hosted GPU job metadata, runtime versions, device observations and finite numerical results.
- The latest run on the exact SHA must succeed. An earlier successful run cannot conceal a later failure or queued run.
- Review records bind lesson, answer, demo and standalone B program hashes. Reviewer logins are case-insensitive; invalid/future dates and findings without fix/retest evidence block eligibility.
- The release workflow runs adversarial contract tests in a separate CPython 3.15.2 job. They use synthetic temporary fixtures and are not a GPU run or expert review.
- No human review record or hardware result has been created by these changes. Issue #7 and Issue #8 remain open; PR #4 remains draft and unmerged.

A failing release-readiness job is expected while required evidence is absent. Inspect its JSON for the missing exact-SHA workflows and independent review records; a passing contract-tests job only validates the evidence checker.

## Same-commit evidence refresh policy (2026-11-05)

The course certification gate uses the **exact 40-hex commit SHA** of Draft PR #4. Success at an earlier commit does not validate a newer commit. CPU, semantic, structural, and native workflows must each finish successfully on the same audit-branch head. The release readiness workflow needs to be rechecked **after** those runs finish; otherwise a race can make `workflow_cpu`, `workflow_semantic`, or `workflow_native` appear false even while an eligible run is executing.

For predictable synchronization, changes to `.github/workflows/release-readiness-3152.yml` now trigger all four technical workflows. Changes to those workflows also trigger release readiness. A technical result is not accepted until its own workflow is completed, successful, and tied to the same SHA. A failed gate is expected when GPU or verified human reviewer evidence is absent; **do not weaken the gate to turn the status green**.

Required final order: finish content and reviewer fixes; complete same-SHA CPU/semantic/structural/native checks; run CUDA on a trusted NVIDIA self-hosted runner; verify the human reviews for all 441 lessons; then rerun the readiness verifier on the same SHA and perform the human final audit. Any subsequent change to versioned content or evidence policy requires checking relevant SHA-bound evidence again. The release verifier does not itself award academic certification.

Current blockers remain Issue #7 (human independent reviews) and Issue #8 (actual NVIDIA GPU). Draft PR #4 must remain DRAFT until independently verified.


## Tổng hợp các hạng mục còn mở sau hiệu đính nội dung

- **Issue #9 — Content QA:** 97 đáp án dạng thiết kế và 97 mô tả phiên bản được Structural QA gắn cờ, cần đối chiếu nội dung, không đồng nhất với lỗi đã xác minh. N01.02 và N03.01 đã bổ sung kiểm thử riêng; còn các mục khác cần phân công và hiệu đính lần lượt.
- **Issue #7 — Expert review:** 441 bài, 79 bài rủi ro cao cần thêm lượt thứ hai, tối thiểu 520 lượt đánh giá có danh tính xác thực; hiện chưa có phiếu ký nhận thực tế.
- **Issue #8 — GPU:** cần Linux x64 runner với NVIDIA GPU, workflow thủ công và artifact CUDA có dữ liệu quan sát đúng phần cứng. Không đánh dấu PASS bằng wheel CUDA hay CPU.
- **Issue #5 — Keras CPU:** blocker cũ đã được đóng sau khi nghiệm thu Keras/h5py tại Issue #6, không còn là điều kiện phát hành riêng.

**Đồng bộ bằng chứng đúng commit:** Mỗi khi chốt nội dung hoặc chỉnh chính sách kiểm định, thay đổi workflow release-readiness để kích hoạt bốn luồng CPU, semantic, structural và native trên cùng SHA; kiểm tra toàn bộ run và artifact sau khi chúng hoàn tất, rồi mới chạy lại release gate. Release gate tiếp tục BLOCKED tới khi GPU thật và phản biện độc lập có bằng chứng. Không nhầm **chạy thành công** với **chứng nhận học thuật**.
