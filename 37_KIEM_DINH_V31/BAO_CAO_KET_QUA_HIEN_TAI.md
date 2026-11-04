# Báo cáo v3.1: trạng thái kiểm định có thể tái lập

**Ngày lập:** 04/11/2026. **Đối tượng:** giáo trình Python v3.0, 441 bài học, 441 demo, 95 lời giải mã.

## Các hoạt động đã thực hiện trong phiên này

- Đọc, kiểm tra ZIP v3.0 và đối chiếu số lượng file bài/demo/lời giải: 441/441/95.
- Kiểm tra môi trường: `sys.version` = CPython 3.13.5; không phát hiện CPython 3.15.2 đã cài.
- Thử truy cập Python.org qua urllib và công cụ tải URL: thất bại do hạn chế mạng/DNS.
- Kiểm tra cú pháp chương trình kiểm định v3.1: đạt trên Python 3.13.5.
- Chạy chế độ strict trên 3.13.5: bị chặn với exit code 2, đúng thiết kế.
- Chạy baseline bốn tính năng 3.15 và free-threading trên 3.13.5: 9 trạng thái SKIP, **không có PASS của 3.15.2**.
- Chạy cổng nghiệm thu v3.1 với báo cáo baseline của v3.0: trả `NOT_PASSED`, exit code 3.
- Kiểm tra tính toàn vẹn hai ZIP v3.1: không phát hiện mục ZIP hỏng.

## Cải tiến kỹ thuật trong v3.1

- Trình kiểm tra free-threading chạy child process với cờ `-X gil=0`, tránh phụ thuộc biến `PYTHON_GIL` khi trình thông dịch chạy `-I`.
- Cổng nghiệm thu đối chiếu cả tập mã bài/kind (441 demo + 95 lời giải), đường dẫn và SHA-256 từ báo cáo kiểm thử với các file hiện có.
- GitHub Actions có ba hạng mục: Ubuntu CPython 3.15.2 CPU, Windows CPython 3.15.2 (bốn tính năng mới), Ubuntu 3.15.2t free-threaded. Workflow **mới tạo, chưa được chạy**.

## Những điều không được xác nhận

- Chưa có bằng chứng chạy 536 file trên CPython 3.15.2.
- Chưa có bằng chứng CPU, GPU, `abi3t` trên CPython 3.15.2.
- Chưa có bằng chứng tất cả thư viện ngoài tương thích đồng thời khi cài trong cùng môi trường; có wheel không đồng nghĩa tương thích tích hợp.
- Smoke test `exit code=0` không thay cho kiểm định nghiệp vụ hoặc phản biện độc lập.

## Nguồn chính thức

- Python 3.15.2: https://www.python.org/downloads/release/python-3152/
- What's new: https://docs.python.org/3.15/whatsnew/3.15.html
- Free threading: https://docs.python.org/3/howto/free-threading-python.html
- Stable ABI `abi3t`: https://docs.python.org/3/howto/abi3t-migration.html
- Hosted CI setup: https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md
