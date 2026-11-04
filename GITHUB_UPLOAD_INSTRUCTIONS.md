# Giáo trình Python: nguồn kiểm định và quy trình tải GitHub

**Phạm vi:** 441 demo và 95 lời giải B, cùng 441 file bài học, bộ kiểm định phiên bản và rubric heuristic. Nội dung nguồn lấy từ ZIP giáo trình v3.1, **chưa chỉnh sửa mã**, không có 4 demo gốc mới khác với bản đang nằm trên repository.

**Trạng thái:** Đây là gói **dùng để đưa lên GitHub** nhằm thực thi kiểm thử 536 file trên CPython 3.15.2. Chỉ có 4 demo đã được kiểm thử 3.15.2 trên GitHub trước đó. Không đánh dấu 536/536 PASS khi chưa chạy workflow mới.

## Cách tải bằng Git

1. Giải nén gói này vào thư mục gốc repository (cùng cấp `.github`).
2. Không thêm tệp bí mật, token, venv, dữ liệu cá nhân. Xem `GITHUB_SOURCE_SHA256.csv` để đối chiếu ấn định nội dung.
3. Mở Terminal/PowerShell tại repository và chạy:

```powershell
git checkout -b audit/full-course-536
# Sau khi đã giải nén bộ nguồn vào đúng thư mục:
git add 03_HOC_PHAN 31_HOAN_THIEN_LOI_GIAI_V28 35_KIEM_DINH_CPYTHON_3152 37_KIEM_DINH_V31 GITHUB_REVIEW_MATRIX.csv GITHUB_SOURCE_SHA256.csv GITHUB_UPLOAD_INSTRUCTIONS.md
git commit -m "test: add 441 Python demos and 95 B solutions for CPython 3.15.2"
git push -u origin audit/full-course-536
```

4. Mở PR. Workflow `.github/workflows/full-course-3152.yml` đã được thiết lập qua GitHub; khi các thư mục nguồn được tải lên nhánh `audit/full-course-536`, workflow có thể chạy theo sự kiện `push`. Ghi nhận mã bài FAIL/TIMEOUT/SKIP riêng; **không tự động hợp nhất vào main khi test chưa đạt**.

## Điều kiện nghiệm thu

- Cổng kiểm định có trong `37_KIEM_DINH_V31/certification_gate.py` kiểm tra 441 demo + 95 lời giải, đường dẫn, SHA-256 và các kiểm thử ngữ nghĩa.
- `PASS_EXIT_0` chỉ là smoke test; cần assertion thực tế và phản biện chuyên môn độc lập cho bài có rủi ro.
- Kiểm thử không chứng nhận GPU, free-threaded hoặc native abi3t nếu không có bằng chứng thực tế.
