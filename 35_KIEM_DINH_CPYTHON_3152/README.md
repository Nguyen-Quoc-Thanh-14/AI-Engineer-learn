# Gói kiểm định giáo trình Python v2.9 (chưa chứng nhận 3.15.2)

**Tình trạng:** Đã kiểm thử baseline CPython 3.13.5. Chưa có môi trường CPython 3.15.2, do đó **không được diễn giải file này là chứng chỉ tương thích 3.15.2**.

## Bằng chứng đã thực hiện

- 441 demo và 95 lời giải có chương trình Python đã được kiểm tra bằng `run_validation.py` trong tiến trình độc lập, thư mục tạm và môi trường CPU.
- Kết quả ban đầu: 529 exit 0, 1 lỗi ZeroDivisionError có chủ đích, 4 bài yêu cầu 3.15, 2 lần timeout 9 giây.
- Hai bài timeout được chạy lại riêng với timeout 42 giây, **cả hai exit 0**; nhật ký trước và sau đều được giữ.
- Tổng hợp có đối chiếu: 531 chương trình exit 0 (gồm 2 chạy lại), 1 lỗi có chủ đích, 4 bài chưa chạy do yêu cầu Python 3.15.
- 17 bài nhập môn được đối chiếu **đầu ra cụ thể**, cả 17 đạt.
- 373 demo có cú pháp `assert` (theo AST Python 3.13); hai file cú pháp chỉ hợp lệ trên 3.15 chưa thể parse bằng 3.13.
- Gói kiểm thử Python 3.15.2 có gate chính xác theo version. Chưa có kết quả chạy gate **thành công** trên 3.15.2.

## Cách chạy trên máy đã cài CPython 3.15.2

Giải nén gói vào một thư mục và mở terminal tại thư mục gốc.

```bash
python --version
python 35_KIEM_DINH_CPYTHON_3152/run_validation.py --strict --suite all --jobs 2 --timeout 20
python 35_KIEM_DINH_CPYTHON_3152/run_output_oracles.py
python 35_KIEM_DINH_CPYTHON_3152/verify_new_315_features.py
python 35_KIEM_DINH_CPYTHON_3152/verify_libraries_on_3152.py
```

Nếu lệnh `python` không trỏ tới 3.15.2, dùng đường dẫn tuyệt đối tới đúng executable hoặc `py -3.15` trên Windows **và kiểm tra bản vá** trước. `run_validation.py --strict` từ chối mọi bản khác 3.15.2. Trong môi trường CPU yếu, dùng `--jobs 1`. Gói này chỉ kiểm tra mã hiện có; không tự động cài Python, pip hoặc các thư viện.

## Phân loại chứng cứ

| Trạng thái | Ý nghĩa |
|---|---|
| PASS_EXIT_0 | Tiến trình thoát mã 0; chưa chứng minh tính đúng toàn bộ |
| PASS_EXIT_0_AFTER_RETRY | Chạy lại sau timeout, có lưu chứng cứ riêng |
| EXPECTED_ERROR | Ngoại lệ có chủ đích trong bài gỡ lỗi |
| REQUIRES_PYTHON_315 | Cú pháp/đối tượng của 3.15 chưa thể kiểm tra bằng 3.13 |
| PASS_ORACLE | Đầu ra bằng đúng kết quả kỳ vọng đã viết độc lập |
| NOT_INSTALLED | Thư viện không có trong môi trường |
| PASS (library probe) | Đoạn thử chức năng thư viện đã chạy trên đúng runtime |

## Các giới hạn còn tồn tại

1. Không thực thi trực tiếp 3.15.2 trong phiên này do không có bản interpreter và môi trường không tải được từ bên ngoài.
2. PyPI cung cấp wheel `cp315` không đồng nghĩa với chạy được trong hệ thống đích; còn phụ thuộc OS/architecture, transitive dependencies và driver.
3. Chưa kiểm tra tải thực tế, memory leak, free-threading, race conditions hay kiểm thử GPU/CUDA. `abi3t` phải được kiểm tra riêng trên free-threaded CPython.
4. 99 lời giải thiết kế/quy trình không thể nghiệm thu bằng `exit code`; cần đánh giá chuyên môn hoặc triển khai thực tế.
5. `PASS_EXIT_0` là smoke test. Các bài chuyên môn cần thêm test chức năng, trường hợp biên và phản biện sư phạm.

## Đường dẫn bằng chứng

- `BASELINE_3135.json`: kết quả thực thi gốc
- `TIMEOUT_RETRY.json`: nhật ký chạy lại hai trường hợp timeout
- `BASELINE_3135_RECONCILED.json`: thống kê sau chạy lại, không xóa lịch sử
- `ORACLE_RESULTS.json`: 17 kiểm thử đầu ra
- `dependency_matrix.csv`: thống kê thư viện và wheel PyPI
- `static_demo_inventory.csv`: AST, import, SHA-256 từng demo
- `AUDIT_SUMMARY_V29.json`: tổng hợp

## Nguồn ngoài

- CPython 3.15.2: https://www.python.org/downloads/release/python-3152/
- Changes 3.15: https://docs.python.org/3.15/whatsnew/3.15.html
- NumPy 2.5.4: https://pypi.org/project/numpy/2.5.4/
- pandas 3.1.0: https://pypi.org/project/pandas/3.1.0/
- scikit-learn 1.9.1: https://pypi.org/project/scikit-learn/1.9.1/
- PyTorch 2.15.0: https://pypi.org/project/torch/2.15.0/
- PyArrow 26.0.0: https://pypi.org/project/pyarrow/26.0.0/
