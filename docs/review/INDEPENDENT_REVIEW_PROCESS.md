# Quy trình phản biện học thuật độc lập cho 441 bài

**Trạng thái hiện tại: CHƯA CÓ 441 phiếu đánh giá độc lập được xác minh.** CI, kiểm tra nguồn, phân tích AI hoặc 536 chương trình chạy thành công không được xem là đã phản biện chuyên gia.

## Phân công người đánh giá

Yêu cầu có chuyên gia thực, lý lịch/chuyên môn được đối chiếu độc lập, nêu tổ chức/đơn vị và xung đột lợi ích. Các nhóm chuyên môn: Python/kỹ thuật phần mềm; bảo mật và concurrency; ML/Thống kê; CPython C API/native ABI; phương pháp giảng dạy.

## Hồ sơ bắt buộc cho mỗi bài

Mã bài; SHA-256 bài học, demo và lời giải; tên và GitHub username chuyên gia thật; tổ chức, ngày, tuyên bố độc lập; năm điểm 0-4 theo rubric đang có; URL review có giải thích; ít nhất một phản ví dụ và bài tập kiểm tra kết quả; issue lỗi và commit sửa, retest URL; quyết định ACCEPTED hoặc CHANGES_REQUESTED.

Chỉ ACCEPTED khi tất cả năm tiêu chí >=3, không còn lỗi nghiêm trọng, mọi thay đổi đã kiểm thử lại, và người đánh giá độc lập được xác nhận bởi người quản lý học thuật. Không phát hành phiếu tự động, tên hoặc chữ ký chuyên gia giả.

## Ví dụ phải dùng để rà soát

N01.01 yêu cầu schema điểm số 0..10 và NaN nhưng bản cũ trả lời bài kiểm tra tuổi 0..130. Một phép thử exit 0 không phát hiện nội dung lệch đề. Các bài khác vẫn phải đối chiếu từng yêu cầu bài B với đáp án thực tế.

## Công cụ

Chạy tests/curriculum_quality_audit.py sẽ sinh ma trận tín hiệu tĩnh cho toàn 441 bài và giữ nguyên trạng thái AWAITING_EXTERNAL_REVIEW. Dữ liệu này là chỉ dẫn phân công, KHÔNG phải phán quyết đúng/sai do chuyên gia.

## Ràng buộc phiếu với nguồn được review

Manifest dùng header trong INDEPENDENT_REVIEW_SIGNOFFS.csv. Ngoài hash bài học và đáp án, bắt buộc điền demo_sha256 của MA_MAU/<mã>_demo.py. Với 95 chương trình B độc lập, điền solution_code_sha256 của 31_HOAN_THIEN_LOI_GIAI_V28/<mã>_bai_B_solution.py; để trống trường này nếu bài không có chương trình B độc lập. Thay đổi bất kỳ tệp đã ký nào làm phiếu cũ mất hiệu lực.

GitHub username được so sánh không phân biệt chữ hoa/thường: hai cách viết cùng một tài khoản chỉ tính một reviewer. Ngày phải hợp lệ và không ở tương lai. Có findings_issue_urls hoặc metadata sửa lỗi thì phải kèm đầy đủ fix_commit_sha (40 ký tự hex) và retest_evidence_url. Chuyên gia vẫn phải đối chiếu rằng commit thực sự sửa đúng lỗi và retest đúng nguồn; kiểm tra cú pháp không tự làm được việc này.

Các ca trong tests/test_evidence_gates.py dùng tên, tệp và ZIP tổng hợp trong thư mục tạm. Chúng kiểm tra hành vi của cổng bằng chứng, không tạo phiếu nghiệm thu thật. Manifest thật vẫn chưa có dòng ACCEPTED; không điền tên hoặc kết quả thay chuyên gia.


## CI không được tự cản việc phản biện hoàn tất

Structural QA kiểm tra cấu trúc bài học và gọi `independent_review_gate.py` để xác nhận mã trả về phù hợp: `EVIDENCE_PENDING` ↔ mã 3; `RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK` ↔ mã 0. Cả hai trường hợp đều không cấp `ACADEMICALLY_CERTIFIED`. Trước đây workflow chỉ cho phép mã 3, khiến workflow không thể PASS khi chuyên gia đã nộp đầy đủ hồ sơ; lỗi này được sửa để giữ cổng phát hành **có thể đạt khi đủ bằng chứng thật** mà không làm giảm điều kiện kiểm định. Các lỗi liên kết nội bộ, thiếu đáp án/demo, sai mã tiêu đề phải làm Structural QA FAIL; cảnh báo về chất lượng và nguồn phải đi vào danh sách phản biện thủ công.
