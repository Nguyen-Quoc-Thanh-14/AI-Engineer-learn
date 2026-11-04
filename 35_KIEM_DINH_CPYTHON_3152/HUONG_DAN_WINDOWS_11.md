# Chạy kiểm định CPython 3.15.2 trên Windows 11

1. Cài đúng Python 3.15.2 từ https://www.python.org/downloads/release/python-3152/.
2. Kiểm tra phiên bản thực tế trong PowerShell: `py -3.15 --version` (phải chính xác 3.15.2).
3. Tạo môi trường: `py -3.15 -m venv .venv315`.
4. Sử dụng `./.venv315/Scripts/python.exe --version` (PowerShell có thể dùng `.\.venv315\Scripts\python.exe`).
5. Cài gói có wheel CPython 3.15 đã được xác nhận trên PyPI, chia theo nhóm:

   ```powershell
   .\.venv315\Scripts\python.exe -m pip install --upgrade pip
   .\.venv315\Scripts\python.exe -m pip install numpy==2.5.4 pandas==3.1.0 scikit-learn==1.9.1
   .\.venv315\Scripts\python.exe -m pip install pyarrow==26.0.0 scipy Pillow opencv-python fastapi SQLAlchemy
   # PyTorch chỉ cài khi cần và sau khi đối chiếu hướng dẫn CPU/CUDA chính thức:
   # https://pytorch.org/get-started/locally/
   ```

   Tên gói, phiên bản và phụ thuộc cần được pip giải quyết thành công trên máy đích; không thể bảo đảm trước.
6. Chạy kiểm tra (từ thư mục gốc có `03_HOC_PHAN/`):

   ```powershell
   .\.venv315\Scripts\python.exe 35_KIEM_DINH_CPYTHON_3152/run_validation.py --strict --suite demos --jobs 1 --timeout 25
   .\.venv315\Scripts\python.exe 35_KIEM_DINH_CPYTHON_3152/run_output_oracles.py
   .\.venv315\Scripts\python.exe 35_KIEM_DINH_CPYTHON_3152/verify_new_315_features.py
   .\.venv315\Scripts\python.exe 35_KIEM_DINH_CPYTHON_3152/verify_libraries_on_3152.py
   ```

**Không** dùng `python` không rõ phiên bản để chứng nhận. Script `--strict` sẽ từ chối sai phiên bản. Với máy RAM thấp, chạy `--jobs 1`; PyTorch có thể đòi nhiều RAM. `tensorflow`, CUDA và free-threaded `abi3t` là các hạng mục xác minh riêng.
