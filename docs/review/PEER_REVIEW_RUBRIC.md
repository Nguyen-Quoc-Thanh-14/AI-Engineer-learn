# Quy trình phản biện độc lập — 441 bài Python

**Trạng thái:** CHƯA phản biện độc lập. Bảng CSV được tạo bởi phép đo tín hiệu tĩnh, **không phải** kết quả nhận định của chuyên gia.

## Nghiệm thu từng bài

- **Tính đúng đắn (0–4):** Định nghĩa, ví dụ, đầu vào/đầu ra và sai số có chính xác? Có dẫn nguồn tài liệu gốc không? Điểm 0 = sai có hệ thống; 4 = được kiểm tra bằng ví dụ và phản ví dụ.
- **Tính sư phạm (0–4):** Tiên quyết, mục tiêu đo được, thứ tự từ dễ đến khó, thuật ngữ tiếng Việt–Anh, đáp án bám sát bài B.
- **Tính thực hành (0–4):** Có thể chạy từ đầu trong môi trường tái lập; có assert về output; kiểm thử ca thường, rỗng/biên, sai đầu vào và hồi quy.
- **An toàn (0–4):** Kiểm tra riêng với N (Security), L (Concurrency), PM (ML) và PR (Native); từ chối hành vi nguy hiểm, mất dữ liệu, rò rỉ, data leakage, race, UB/overflow.
- **Tương thích (0–4):** Có log và SHA của đúng CPython 3.15.2, đúng dependency; `SKIP`/`TIMEOUT` không được đổi thành `PASS`.

## Các trường bắt buộc ở mỗi lần đánh giá

Mã bài, tên/ngành và đơn vị của chuyên gia, xác nhận độc lập/xung đột lợi ích, ngày đánh giá, phiên bản commit và SHA file, 5 tiêu chí + bằng chứng, lỗi phát hiện kèm mức độ nghiêm trọng, commit khắc phục, kết quả kiểm tra lại; trạng thái: `AWAITING_EXTERNAL_REVIEW`, `CHANGES_REQUESTED`, `RETEST_REQUIRED`, `ACCEPTED`.

**Chấp nhận cuối bài:** không tiêu chí nào < 3/4; không còn lỗi an toàn mức nghiêm trọng; mọi kiến nghị đã được giải quyết và kiểm tra lại. Nếu không có chuyên gia thật, giữ trạng thái `AWAITING_EXTERNAL_REVIEW`.

**Không dùng điểm tự động để thay thế người đánh giá.**