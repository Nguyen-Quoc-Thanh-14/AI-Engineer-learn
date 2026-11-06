# Quy chuẩn biên tập và dàn trang (Editorial Style Guide)

## 1. Kiến trúc giáo trình

- Bộ sách dùng **5 tập**, **26 học phần**, **137 chương**, **441 bài**. Mã bài ổn định được xem như khóa chính, không tái đánh số theo trang.
- Người học bắt đầu từ Tập 01; tập 04–05 có thể chọn nhánh chuyên sâu sau khi hoàn thành tiền đề cần thiết.
- Mỗi bài bảo toàn mục tiêu, khái niệm, ví dụ, trường hợp biên, bài tập, giải thích, tài liệu kiểm chứng và ghi chú version từ nguồn.
- Sách học viên và sách lời giải luôn tách nhau; không đặt đáp án ngay sau bài tập trong bản dành cho học viên.

## 2. Thuật ngữ và kỹ thuật

- Giữ nguyên các định danh, từ khóa, API, đường dẫn module, lệnh CLI, type annotations, ký hiệu toán và văn bản bên trong code fence.
- Dùng thống nhất các cặp thuật ngữ trong phần lời dẫn mới: bài học / lesson; ví dụ / demo; lời giải B / B-solution; kiểm thử thực thi / runtime test; kiểm tra kiểu tĩnh / static type checking.
- Không dùng "đã chứng nhận", "phản biện độc lập đạt", "CUDA đã nghiệm thu" nếu chưa có hồ sơ ký và bằng chứng thực thi cụ thể.
- Khẳng định "chạy thành công" phải gắn đúng đối tượng, runtime, SHA và link workflow. Test exit 0 không đồng nghĩa code đúng cho mọi đầu vào.
- Không tự sửa các khẳng định trong mã nguồn gốc khi kết hợp sách; các sửa đổi ngữ nghĩa cần issue/PR riêng, kiểm thử và tái xuất bản.

## 3. Quy tắc typography và liên kết

- Tên tập: H1. Mục lục và tên chương: H2. Mã bài: H3. Các mục gốc trong bài nâng cấp H4/H5, tránh xung đột số thứ tự và anchor khi ghép.
- Loại bỏ tiền tố số mục như "## 7." CHỈ ở bản dàn trang; lưu trong editorial_warnings.json; không xóa từ nguồn.
- Khối code dùng font monospace; giữ dấu tiếng Việt UTF-8, thụt dòng và ngôn ngữ của fence.
- Link tương đối của bài gốc được viết lại thành permalink tại SHA, nếu file tồn tại. Link không xác định được giữ nguyên và ghi cảnh báo, không tạo URL giả.
- In A4, chia trang trước mỗi chương/bài, bảng không quá rộng, không ngắt tiêu đề khỏi đoạn sau. Trước khi công bố cần xem bản in trên thiết bị thực.

## 4. Kiểm thử xuất bản

Ngưỡng tự động: đúng 441 bài, 137 chương, 26 học phần, có một lời giải tương ứng cho mỗi bài; đủ 10 bản Markdown, 10 bản HTML và source_map 441 hàng; SHA của thành phẩm được lưu manifest.

Ngưỡng thủ công: xem 2 bài ngẫu nhiên từ mỗi tập, xem tất cả đầu/cuối mục lục, đánh giá phông tiếng Việt và code dài, xác minh nguồn/giấy phép, soát các cảnh báo link và ký phê duyệt tên tác giả.

**Quan trọng:** cổng kiểm tra bố cục không đánh giá đúng/sai khoa học của 441 bài.
