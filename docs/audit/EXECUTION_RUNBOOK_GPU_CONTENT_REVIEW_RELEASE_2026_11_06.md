# Runbook chủ repo và AI: từ GPU Kaggle tới sẵn sàng phát hành

**Ngày:** 06/11/2026. **Nhánh lưu hướng dẫn:** `experiment/kaggle-cuda`. **Không đổi** `main` hoặc Draft PR #4. Chứng nhận toàn diện chưa được cấp.

## Nguyên tắc

1. Không chuyển `SKIP` hoặc `BLOCKED` sang PASS không có bằng chứng.
2. Phân biệt (a) đúng nội dung kỹ thuật; (b) bằng chứng runtime GPU; (c) chứng thực môi trường và nguồn thực thi; (d) phản biện độc lập thật; (e) quyết định phát hành.
3. Bằng chứng CUDA Kaggle cũ gắn commit `d1f740b4faa5c8d1361e5427f0d723afd804a2d2`, **không tự động chuyển hợp lệ** nếu nguồn/script/chính sách ở commit cuối khác.
4. AI được sửa, kiểm thử và thu xếp hồ sơ trong nhánh làm việc, nhưng không tự đại diện người phản biện hoặc cấp chứng chỉ.

## Giai đoạn A. Bảo quản bằng chứng CUDA đã đạt

**AI đã làm:** Kiểm tra `cuda3152_kaggle_evidence.zip`: SHA-256 ZIP `531b912bbb99f2728e5f74474e87d55bd9b7411e994d50dd246654423697cb21`, 7/7 manifest digests khớp, mã collector so khớp Git blob tại SHA nguồn, kiểm tra điều kiện toán học. Hồ sơ [KAGGLE_T4_EXTERNAL_GPU_EVIDENCE_2026_11_06.md](KAGGLE_T4_EXTERNAL_GPU_EVIDENCE_2026_11_06.md).

**Chủ repo cần làm:** Giữ bản ZIP gốc và lưu version Kaggle có mã + output truy xuất được; chia sẻ link phiên bản bất biến nếu có. Không gửi token GitHub/Kaggle hoặc mật khẩu.

**Chưa đạt:** `GITHUB_RUN_ID`/`GITHUB_RUN_ATTEMPT` và provenance GitHub Actions self-hosted; `workflow_gpu=false` tại release gate cũ. Việc thêm checksum hoặc ảnh không tạo được chứng thực hệ thống. Nếu muốn chấp nhận Kaggle làm đường thay thế, cần chính sách attestation khác (Kaggle version metadata, nguồn độc lập, verify source SHA, kiểm tra tiêu chí, duyệt thủ công), test âm tính và phê duyệt bằng người thật; tuyệt đối không tự cấp PASS.

## Giai đoạn B. Kiểm toán 441 bài trước khi ký nghiệm thu

**AI có thể làm bằng GitHub:**
- Mở [Issue #9](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/9), tải artifact `course-441-structural-audit-not-peer-review` từ [structural QA](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42048363681) và đọc `lessons_441.csv`.
- Rà tín hiệu **97** câu trả lời dạng thiết kế và **97** câu về phiên bản có thể cũ; *không* coi là 194 lỗi thực. Đối chiếu từng bài B với lời giải `LOI_GIAI`, `MA_MAU` và 95 bài B có executable riêng trong `31_HOAN_THIEN_LOI_GIAI_V28`.
- Với mỗi bài ghi `FALSE_POSITIVE / CONFIRMED_DEFECT / NEEDS_HUMAN_REVIEW`, link file, dòng, mô tả lỗi, testcase, sửa ở nhánh phát triển; thêm semantic tests khi có thể.
- Chạy `curriculum-quality-audit`, `semantic-contracts`, `full-course-3152`, `course-native-pr02-3152` trên SHA **mới nhất**; không dùng run cũ cho nguồn mới.

**Chủ repo cần làm:** Xem và quyết định các thay đổi có tác động chương trình học/kiến trúc; không buộc tham gia sửa mã từng bài.

**Xong khi:** Lỗi nội dung blocking không còn, cảnh báo còn lại có lý do/nguồn, hồi quy các job đều đạt trên SHA chốt.

## Giai đoạn C. Người phản biện độc lập thật, 441 bài / 520 lượt

**AI đã chuẩn bị:** Script và artifact phân công 520 lượt: [workflow](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42047877209), [hướng dẫn](../../review/EXPERT_REVIEW_PACKET_GUIDE.md), [rubric](../../review/PEER_REVIEW_RUBRIC.md), [quy trình](../../review/INDEPENDENT_REVIEW_PROCESS.md).

**Chủ repo bắt buộc:**
- Tìm và mời người có danh tính + chuyên môn xác thực, khai báo xung đột lợi ích, công khai phạm vi làm việc và thời gian/chi phí nếu có.
- Giao task theo SHA nguồn chốt; ít nhất **441** bài có một reviewer, **79** bài rủi ro cao cần một reviewer thứ hai *khác người* (tổng **520** lượt).
- Sau khi reviewer nêu phát hiện, AI có thể sửa/test; reviewer cần **kiểm lại** theo SHA mới.
- Chỉ điền review thật vào `docs/review/INDEPENDENT_REVIEW_SIGNOFFS.csv`; 5 tiêu chí đều >=3/4, issue/fix/retest URL khi cần, không tạo danh tính hay điểm giả.

**AI có thể làm:** soạn lời mời, phân công công việc, issue checklist, sửa lỗi, tạo báo cáo so sánh trước/sau, chạy `tests/independent_review_gate.py`. Cổng này không xác thực năng lực/danh tính thật; cần người chịu trách nhiệm kiểm lại.

**Xong khi:** Gate báo `RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK` và người quản lý độc lập xác minh 520 lượt thật, bằng chứng, không tồn đọng lỗi blocking.

## Giai đoạn D. Chứng thực GPU trên bản chốt + release gate

**Thứ tự chính xác:** sửa nội dung/retest → chốt SHA → thu GPU proof trên SHA đó → review/corrections cuối (nếu đổi SHA, retest các cổng liên quan) → chạy release readiness → người có thẩm quyền kiểm toán cuối.

**Lựa chọn giữ nguyên chính sách hiện hành (khuyến nghị nếu cần cổng máy PASS):**
- Chủ repo cung cấp **Linux x64 GPU NVIDIA CC>=7.5** được phép sử dụng, tạo self-hosted Actions runner với nhãn `self-hosted,linux,x64,gpu`, bảo vệ môi trường và không chạy code không tin cậy chứa secret.
- Mở [GPU workflow](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/workflows/gpu-self-hosted-3152.yml), chọn branch `audit/full-course-536` tại SHA chốt, chạy thủ công; kiểm artifact `actual-cuda-cpython3152-evidence` cùng run ID, attempt và runner metadata.
- **Không** giả tạo `GITHUB_RUN_ID` để thuyết phục collector. Kaggle notebook bình thường không phải self-hosted runner.

**AI có thể làm:** kiểm tra workflow/job/log/artifact, đối chiếu SHA/checksums, chạy hợp đồng âm tính và hỗ trợ khắc phục; không điều khiển GPU Kaggle khi không có connector phiên, không xác thực người review thay chủ repo.

**Release final:** trên đúng SHA chạy `full-course-3152.yml`, `semantic-contracts-3152.yml`, `curriculum-quality-audit.yml`, `course-native-pr02-3152.yml`, GPU workflow và `release-readiness-3152.yml`; kiểm đủ 520 signoffs, đánh giá thủ công và kiểm toán cuối. Trạng thái `ELIGIBLE_FOR_HUMAN_FINAL_AUDIT` **không phải** chứng nhận pháp lý/học thuật bên ngoài. Chỉ đổi PR #4 từ Draft và merge khi có quyết định cuối có bằng chứng.

## Phân công trách nhiệm

| Hạng mục | AI có thể tự xử lý | Chủ repo/người thật cần làm |
|---|---|---|
| Kiểm toán 441/95, sửa và test | Có, qua GitHub | Duyệt các thay đổi nội dung quan trọng |
| Bằng chứng GPU đã cung cấp: kiểm ZIP/SHA và ghi hồ sơ | Có | Lưu bản gốc / Kaggle version |
| Tạo GitHub self-hosted runner GPU vật lý | Không tự thực hiện | Cấp máy, đăng ký runner tin cậy, quyết định chi phí |
| Phản biện và ký chuyên gia độc lập | Không giả mạo | Mời, đánh giá chuyên môn, ký/duyệt thật |
| Release readiness | Kiểm tra tự động và báo cáo | Phê duyệt cuối nếu đạt và quyết định merge |

**Các đầu mối:** [Issue #9](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/9) (content), [Issue #7](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/7) (human review), [Issue #8](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/8) (GPU), [Draft PR #4](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/pull/4) (release).
