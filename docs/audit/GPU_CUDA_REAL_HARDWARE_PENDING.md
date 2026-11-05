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

## Đối chiếu artifact với đúng lượt chạy

Bộ thu ghi commit_sha từ git HEAD, repository, run_id, run_attempt và source_sha256; từ chối nguồn collector/workflow có thay đổi chưa commit. Workflow giữ yêu cầu CPython 3.15.2, Linux x86_64 và torch 2.15.0; Python chạy với -O bị từ chối vì sẽ bỏ các assert.

Cổng phát hành tải ZIP và đối chiếu digest SHA-256 của artifact do GitHub trả về; đọc gpu_runtime.json, kiểm tra đúng commit/lượt chạy/lần thử và hash bộ thu. Nó còn kiểm tra metadata job self-hosted/linux/x64/gpu, phiên bản, quan sát thiết bị, gradient, đối chiếu convolution CPU/GPU và các chỉ số huấn luyện hữu hạn. Có artifact đúng tên là chưa đủ. Một lần chạy mới bị lỗi hoặc còn chờ sẽ chặn, không dùng lần chạy xanh cũ để thay thế.

Token GitHub chỉ dùng với API GitHub; request tới URL lưu trữ có chữ ký không mang Authorization. Kiểm tra tự động vẫn dựa trên runner tin cậy và không chứng minh toàn bộ chất lượng CV/DL. Các ZIP tổng hợp trong kiểm thử đơn vị không phải bằng chứng đã chạy GPU.


## Tương thích GPU với môi trường nghiệm thu PyTorch 2.15/CUDA 13.x

**Yêu cầu của bộ kiểm định:** GPU Linux x64 có compute capability **>= 7.5** (Turing hoặc mới hơn). Theo tài liệu NVIDIA, CUDA 13 đã loại bỏ hỗ trợ biên dịch offline và thư viện cho Maxwell/Pascal/Volta. PyTorch 2.15 ngừng cung cấp binary CUDA 12.6 (mốc cuối cho các kiến trúc này). Bộ collector lấy compute capability bằng `torch.cuda.get_device_capability()`, chặn thiết bị không hỗ trợ, đồng thời ghi capability và danh sách kiến trúc PyTorch biên dịch vào artifact; điều kiện thực thi CUDA và huấn luyện thật vẫn bắt buộc.

**Lưu ý Quadro M620:** NVIDIA liệt kê Quadro M620 ở compute capability **5.2 (Maxwell)**, do đó không phù hợp để chạy bộ GPU nghiệm thu yêu cầu PyTorch 2.15/CUDA 13.x. Muốn khảo sát GPU cũ cần một bộ benchmark riêng (phiên bản CUDA/PyTorch cũ) và **không được** dùng kết quả đó thay GPU proof trên CPython 3.15.2 với dependency pinned của giáo trình.

- NVIDIA CC: https://developer.nvidia.com/cuda/gpus/legacy
- NVIDIA CUDA 13 kiến trúc: https://docs.nvidia.com/cuda/archive/13.0.0/cuda-toolkit-release-notes/
- PyTorch 2.15 GPU wheel binary support: https://dev-discuss.pytorch.org/t/notice-cuda-12-6-wheels-will-no-longer-be-published-from-pytorch-2-15-drops-maxwell-pascal-volta/3432

### Hướng chọn runner

**Phương án hiện đã cấu hình:** self-hosted Linux x64 GPU Turing+ (T4, RTX 20-series trở lên hoặc các kiến trúc mới hơn nếu đáp ứng driver) với nhãn `gpu`, job được gọi thủ công. **Không chạy trên thiết bị mà người vận hành không sở hữu/không được phép sử dụng.**

**Lựa chọn có tính phí:** GitHub có larger runner NVIDIA T4 cho tổ chức sử dụng GitHub Team hoặc Enterprise Cloud, nhưng repository này hiện thuộc tài khoản cá nhân (không phải organization). Muốn dùng larger GPU runner GitHub cần chủ repository lựa chọn phương án tổ chức, cấu hình thanh toán và điều chỉnh workflow/evidence gate để chấp nhận metadata của GPU hosted thật. **Chưa cấu hình thanh toán, chuyển repo hay kích hoạt chạy GPU.**

Nguồn GitHub: https://docs.github.com/en/actions/concepts/runners/larger-runners
