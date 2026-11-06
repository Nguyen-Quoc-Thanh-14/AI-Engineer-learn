# Kiểm định bằng chứng CUDA Kaggle — 06/11/2026

**Trạng thái:** `EXTERNAL_GPU_COLLECTOR_PASS_VERIFIED_INTERNAL_CONSISTENCY`. Đây là đánh giá gói bằng chứng người dùng tải lên, **không** phải GitHub Actions trusted-runner attestation hay chứng nhận toàn diện. Không tự động đóng Issue #8.

## Nguồn và sự toàn vẹn

- Tệp nguồn: `cuda3152_kaggle_evidence.zip` (người vận hành tải về từ Kaggle rồi cung cấp để kiểm định, 5.611 byte).
- **SHA-256 ZIP:** `531b912bbb99f2728e5f74474e87d55bd9b7411e994d50dd246654423697cb21`.
- ZIP central directory, CRC/testzip: PASS. Manifest công bố 7 SHA-256 cho 7 tệp; **cả 7/7 đều khớp thực tế**.
- Git commit từ báo cáo và manifest: `d1f740b4faa5c8d1361e5427f0d723afd804a2d2`.
- SHA-256 `gpu_cuda_3152.py`: `ac87f83064ab190129cd136a85613389e3bfa49a057acbccf73aa202990863d5`. Giá trị này khớp trường `source_sha256` trong `gpu_runtime.json`.
- Git blob SHA-1 tính lại theo định dạng Git đối với collector là `4e9df747984fb5922a14bc00d6dcd147d0eef3c6`; khớp blob của `tests/gpu_cuda_3152.py` trong repository GitHub ở commit nêu trên.

## SHA-256 từng thành phần của ZIP

| Tệp | SHA-256 |
|---|---|
| gpu_runtime.json | `6773aef199bb765954152f5d0cdb96ac5af388fe11d04d027a99cdb05acf04bf` |
| gpu_cuda_3152.py | `ac87f83064ab190129cd136a85613389e3bfa49a057acbccf73aa202990863d5` |
| collector_stdout.txt | `d8a1c1e3a015eae9585bae83b7323d7b7d242a09f0ac25cc2358ef38c19ff68f` |
| collector_stderr.txt | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| nvidia_smi.txt | `8a063ea789e005f743628beed0852cc41b8956ff450457d098203bbb0d92b12a` |
| pip_check.txt | `9261363b733079a641c2e4cc9bc46ffa1d8336945a87f807b6cf68847dbc9b09` |
| installed_versions.txt | `53188c6dc4c291876ae1f3862385eea62fb17cd3e838bdd7837056ffceb14aaa` |

## Nội dung kết quả quan sát được trong báo cáo

- Python CPython **3.15.2**, Linux x86_64; PyTorch **2.15.0+cu132**, NumPy **2.5.4**; `pip check`: `No broken requirements found.`.
- `nvidia-smi`: **2 x Tesla T4**, driver **580.178.04**, mỗi GPU ghi **15.360 MiB**. Collector cố định `cuda:0` nên chứng minh tính toán trên **một** GPU, không chứng minh bài thử multi-GPU.
- `torch.cuda.is_available=true`, GPU compute capability **[7,5]**, `device_memory_bytes=15636037632`.
- Gradient `[-4.0,0.0,6.0]`, convolution đối chiếu CPU/GPU `true`, MSE từ **9.0** xuống **4.770013362076497e-08**, dự đoán x=3 **6.999780654907227**; đáp ứng điều kiện xác nhận trong mã nguồn.
- Collector tự ghi `status=CUDA_HARDWARE_PASS`; `collector_stdout` cùng nội dung, `collector_stderr` trống.

## Phạm vi chứng minh và giới hạn bắt buộc

**Đã kiểm định độc lập:** ZIP có thể đọc, checksum đúng, JSON và biểu mẫu nhất quán, nguồn `gpu_cuda_3152.py` khớp GitHub, và các giá trị số thỏa các oracle trong mã.

**Chưa thể xác thực độc lập:** Máy đã thực sự chạy cell tại thời điểm ghi JSON hay không chỉ dựa vào ZIP bên ngoài không có chứng thực nguồn thực thi. `repository`, `run_id`, `run_attempt` đều là chuỗi rỗng; manifest ghi `github_actions_attested=false`. Không có GitHub self-hosted runner metadata, Actions job/run provenance hay artifact từ `.github/workflows/gpu-self-hosted-3152.yml`.

**Quyết định:** Ghi nhận là **bằng chứng thực nghiệm CUDA phù hợp, kiểm định nội dung PASS**, nhưng cổng phát hành vẫn `workflow_gpu=false` theo chính sách hiện tại cho đến khi có GitHub Actions GPU job thật, hoặc một chính sách external-attestation tương đương được phê duyệt và triển khai có kiểm định độc lập. Issue #7 phản biện 441 bài vẫn là blocker riêng; Draft PR #4 không được merge.

**Lưu ý lưu trữ:** Hồ sơ Markdown này lưu các hash và kết quả kiểm tra; bản ZIP gốc chưa được đưa vào repository bởi commit tạo hồ sơ này. Các hash không thay thế tệp bằng chứng gốc.
