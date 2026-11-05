# Cổng GPU CUDA thực — chưa nghiệm thu

Workflow: .github/workflows/gpu-self-hosted-3152.yml; script: tests/gpu_cuda_3152.py.

## Trạng thái

**CUDA_HARDWARE_PASS: CHƯA CÓ BẰNG CHỨNG.** GitHub Actions runner tiêu chuẩn không cung cấp GPU NVIDIA. Chỉ chạy workflow trên self-hosted runner Linux x64 đã kết nối với tài khoản GitHub và gắn nhãn gpu; máy phải có card NVIDIA tương thích và driver/CUDA runtime hoạt động.

Không dùng mô phỏng GPU, không coi torch==2.15.0+cu132 hoặc nvidia-smi một mình là PASS. Bài test buộc tạo tensor thật trên cuda:0, tính gradient, so kết quả convolution với CPU, train mô hình bằng optimizer trên GPU, synchronize và lưu phiên bản/đầu ra.

## Hướng dẫn vận hành

1. Chuẩn bị runner riêng Linux x64 có card NVIDIA, driver, nvidia-smi và truy cập mạng để cài CPython 3.15.2; dùng máy chạy việc kiểm thử tin cậy, không chạy code từ PR của người lạ.
2. Đăng ký self-hosted runner trong repository, gắn nhãn gpu và xác nhận runner Online/Idle trong Settings > Actions > Runners.
3. Mở Actions > Actual NVIDIA CUDA hardware evidence > Run workflow; chọn nhánh audit/full-course-536.
4. Kiểm tra job PASS và tải artifact actual-cuda-cpython3152-evidence. Đối chiếu CUDA_HARDWARE_PASS, device_name, driver, torch_version, SHA256 và kết quả toán/training.
5. Nếu không có GPU hoặc job bị chặn, trạng thái vẫn là NOT_TESTED/NOT_PASSED. Đừng tự xác nhận bằng kết quả CPU hay từ phiên bản gói cài.

**Giới hạn:** kiểm thử một GPU và những phép toán mẫu, không phải benchmark toàn bộ Computer Vision/Deep Learning trên mọi GPU.
