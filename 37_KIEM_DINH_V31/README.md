# Bộ kiểm định CPython 3.15.2 v3.1 — bổ sung tính toàn vẹn và GitHub Actions

**Trạng thái:** Chưa chạy trên CPython 3.15.2. Tạo 2026-11-04.

Gói này **giữ nguyên** 441 bài học và các mã Python gốc của v3.0. Nó cải thiện hai điểm kỹ thuật của công cụ kiểm tra:

1. Khi kiểm tra free-threading bằng Python `-I`, biến môi trường `PYTHON_GIL=0` có thể bị bỏ qua vì chế độ cô lập bỏ qua biến môi trường `PYTHON*`. Vì vậy `run_deep_validation.py` v3.1 thêm `-X gil=0` trực tiếp trong tiến trình con khi chạy phép thử free-threaded.
2. `certification_gate.py` v3.1 đối chiếu **đúng danh sách 441 demo + 95 lời giải**, không có mã trùng, đường dẫn và SHA-256 thực tế. Vẫn không thể dùng một gate nội bộ để thay thế kiểm chứng độc lập hoặc đảm bảo chống sửa giả nhật ký.

## Hướng chạy trực tiếp

Từ thư mục gốc giáo trình, sau khi cài CPython **3.15.2 regular** và thư viện hỗ trợ:

```sh
python 37_KIEM_DINH_V31/run_deep_validation.py --mode strict --group all --timeout 50 --output deep_regular.json
python 35_KIEM_DINH_CPYTHON_3152/run_validation.py --strict --suite all --timeout 60 --jobs 2 --output full_regular.json
python 37_KIEM_DINH_V31/certification_gate.py --full full_regular.json --deep deep_regular.json --output gate_regular.json
```

Trong **CPython 3.15.2 free-threaded build** (phải xác nhận build và GIL thực tế):

```sh
python -X gil=0 37_KIEM_DINH_V31/run_deep_validation.py --mode strict --group free --output free_threaded.json
```

## GitHub Actions (chạy bên ngoài môi trường hiện tại)

Tập tin `.github/workflows/python-3152-course-check.yml` được đặt ở gốc thư mục ZIP. Đưa **toàn bộ nội dung thư mục gốc** vào repository GitHub và chạy workflow từ tab Actions. GitHub sẽ tự cài Python và các thư viện qua mạng ở runner. Định nghĩa công việc này chưa được chạy ở phiên chat; thành công của workflow còn phụ thuộc khả năng cài Python 3.15.2/3.15.2t và wheel tương thích trên GitHub Actions.

Workflow gồm CPU Ubuntu đầy đủ, Windows thử 4 tính năng mới và Ubuntu free-threaded. **GPU CUDA** cần runner có GPU thật. **abi3t** cần xây dựng extension dùng đúng `Py_TARGET_ABI3T` và kiểm thử dưới cả interpreter thường lẫn free-threaded; không được coi `abi3` là bằng chứng cho `abi3t`.

`PASS_EXIT_0` là kiểm thử smoke, không chứng minh toàn bộ logic. Cổng nghiệm thu CPU yêu cầu thêm những phép thử ngữ nghĩa đang có trong `run_deep_validation.py` nhưng **không phải chứng nhận chuyên gia độc lập**.

Tài liệu: https://www.python.org/downloads/release/python-3152/ ; https://docs.python.org/3.15/whatsnew/3.15.html ; https://docs.python.org/3/howto/abi3t-migration.html ; https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md

**Báo cáo kết quả có thật của phiên này:** `BAO_CAO_KET_QUA_HIEN_TAI.md`. Không thể chuyển các `SKIP` từ Python 3.13.5 thành `PASS` của Python 3.15.2.
