# Bộ bản thảo xuất bản — Giáo trình Python

**Trạng thái: CÔNG BỐ CÔNG KHAI 1.0 THEO YÊU CẦU CHỦ SỞ HỮU — CHƯA ĐƯỢC KIỂM ĐỊNH ĐỘC LẬP.** Bản GitHub không có tuyên bố bảo đảm tính chính xác toàn diện, bảo đảm quyền tái sử dụng bên thứ ba, hay chứng nhận CUDA/chuyên gia.

Thư mục này tách biệt với 441 bài học ở 03_HOC_PHAN và mã nguồn kiểm toán. Mục tiêu là chỉnh thể cách đọc, mục lục, thứ tự chương, liên kết và trình bày mà KHÔNG thay đổi hợp đồng bài tập, kết quả kiểm thử lịch sử hay mã gốc.

## Tập 00 — Nền tảng toán học (học trước Tập 01)

[TẬP 00 — NỀN TẢNG TOÁN HỌC CHO PYTHON VÀ AI](TAP_00_TOAN_HOC/TAP_00_NEN_TANG_TOAN_HOC.md) là **tài liệu bổ trợ thuần lý thuyết** gồm 15 chương: logic, đại số, hàm số, giải tích, đại số tuyến tính, tối ưu, xác suất, thống kê, lý thuyết thông tin, số học máy tính, Machine Learning, Deep Learning và Computer Vision. Các chứng minh có giả thiết; kết quả nâng cao có thể chỉ được phác thảo.

**Thứ tự học đề xuất:** Tập 00 → Tập 01 → Tập 02 → Tập 03 → Tập 04 → Tập 05. Tập 00 **không nằm trong** bộ 441 bài và không thay đổi các chỉ tiêu 5 tập/10 ấn bản của pipeline xuất bản hiện có. Word/PDF của Tập 00 được dựng riêng; tệp Markdown là bản đọc/biên tập trên GitHub.

## Cấu trúc thành phẩm

| Tập | Học phần | Bài học | Nội dung |
|---|---|---:|---|
| 01 | A, B, C, D, E | 104 | Nền tảng Python và lập trình có cấu trúc |
| 02 | F, G, H, I, J | 95 | Công cụ phát triển, kiểm thử và tư duy lập trình |
| 03 | K, L, M, N, O | 92 | Hiệu năng, đồng thời, hệ thống và bảo mật |
| 04 | PA, PD, PE, PL, PM | 73 | Ứng dụng, dữ liệu, kỹ thuật dữ liệu và học máy |
| 05 | PN, PR, PS, PT, PV, PW | 77 | AI ứng dụng, native, khoa học và thị giác máy tính |
| **Tổng** | **26 học phần** | **441** | **137 chương** |

Mỗi tập gồm 2 ấn bản: HOC_VIEN (đọc và thực hành trước) và LOI_GIAI (đối chiếu sau), mỗi ấn bản có Markdown và HTML in A4. Workflow cố gắng tạo thêm EPUB3 qua Pandoc. Học liệu tham chiếu bên ngoài chỉ được dẫn đường link, không đính kèm PDF của tác giả khác.

## Quy trình dựng bản thảo

Tại gốc repository, với Python >=3.14 và module markdown 3.9:

    python -m pip install markdown==3.9
    python 40_BIEN_TAP_XUAT_BAN/build.py

Trong GitHub Actions, commit SHA chính xác được tự lấy từ GITHUB_SHA. Máy local không thuộc Git phải cung cấp SHA:

    python 40_BIEN_TAP_XUAT_BAN/build.py --sha <SHA-40-ky-tu>

Kết quả đặt ở 40_BIEN_TAP_XUAT_BAN/_build (không commit):
- 05 tập sách học viên và 05 tập lời giải với đuôi .md, .html, và .epub nếu bước EPUB thành công.
- source_map.csv gồm 441 đường dẫn mã bài và checksum của tệp gốc.
- manifest.json gồm commit nguồn, số chương/bài, checksum thành phẩm và điều kiện xuất bản còn mở.
- editorial_warnings.json ghi nhận các liên kết cần rà soát và tiền tố số thứ tự tiêu đề đã đồng nhất.

Workflow GitHub: editorial-publication-preview.yml đóng gói artifact định dạng sách. Tên artifact có thể còn chữ PREVIEW do quy ước kỹ thuật. Không đồng nghĩa với nghiệm thu CUDA/native/chuyên gia và không tự tạo GitHub Release.

## Quy tắc biên tập an toàn

1. Không sửa mã hay lời giải gốc trong bước đóng gói. Không thay đổi điều kiện đề B.
2. Mỗi chương và bài có mã định danh A01, A01.01... và liên kết đến SHA nguồn cố định.
3. Tiêu đề cấp thấp được chuẩn hóa để hình thức đồng nhất; các tiền tố thứ tự trong đề mục (như "11. Nguồn") được bỏ trong bản dàn trang vì dễ trùng số sau các phụ lục. Không thay đổi nội dung giải thích.
4. Ghi chú trạng thái kiểm thử trong nguồn được giữ lại như dấu vết lịch sử. Xem VALIDATION_SCOPE và workflow thực tế cho phạm vi kiểm định.
5. Cảnh báo được xuất ra báo cáo; không tự chuyển thành PASS hoặc sửa lặng lẽ.
6. Quyền tái bản, nhãn giấy phép, tên hiển thị tác giả, ISBN, thông tin phát hành và phê duyệt cuối cùng: chủ sở hữu xác nhận trước khi công khai.

Đọc thêm: QUY_CHUAN_BIEN_TAP.md, QUYEN_TAC_GIA_VA_NGUON.md, QUYET_DINH_XUAT_BAN.md và GHI_NHAN_DANH_GIA.md.
