# Release evidence needed before final certification

Draft PR #4 stays unmerged. Automated CPU/Keras checks do not prove actual NVIDIA CUDA execution or independent academic quality.

The new CI readiness workflow checks that test runs belong to the exact PR head SHA, that successful CPU/GPU runs have unexpired artifacts, and that the reviewer manifest covers every lesson. If evidence is missing, the workflow fails and uploads a JSON report listing the missing checks.

Issue #8: A trusted Linux x64 NVIDIA runner must be registered and labeled gpu, then the workflow gpu-self-hosted-3152.yml must be run on branch audit/full-course-536. A CUDA wheel or CPU emulation does not count.

Issue #7: Independent verified human experts must review the lesson, demo and B answer for each of 441 lessons, file rubric and SHA-linked evidence, fix defects and sign off without conflicts. A manifest alone cannot authenticate actual expertise; the final decision is human.

Even with a green automated gate the status is only ELIGIBLE_FOR_HUMAN_FINAL_AUDIT, never ACADEMICALLY_CERTIFIED. Keep the PR draft until the external blockers are genuinely resolved.
