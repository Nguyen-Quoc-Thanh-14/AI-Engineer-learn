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
