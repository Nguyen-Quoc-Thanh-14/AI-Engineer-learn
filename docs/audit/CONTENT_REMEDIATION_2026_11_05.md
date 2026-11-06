# Báo cáo hiệu đính nội dung và hồ sơ nghiệm thu — 05/11/2026

## 1. Phát hiện chính

Nhiều lời giải v2.5 được viết theo cùng chủ đề nhưng **không khớp yêu cầu Bài B**. Một mã Python chạy thành công không chứng minh đã giải đúng yêu cầu giảng dạy.

### Nhóm đã hiệu đính (13 bài)

| Mã | Yêu cầu đề bài gốc | Lỗi của đáp án cũ |
|---|---|---|
| N01.01 | Điểm 0–10 và từ chối NaN | Kiểm tra tuổi 0–130 |
| I02.01 | Lower bound / vị trí chèn đầu tiên >= x | Trả -1 nếu phần tử không khớp chính xác |
| F01.01 | Import statistics, tính mean của list không rỗng | Tính căn bậc hai bằng math |
| PR01.01 | Structure thêm c_double, tính sizeof/alignment | Sao chép bytes trong buffer |
| PN03.01 | 30 câu hỏi reference answers, grounded/unsupported | Chỉ tính tỷ lệ exact match |
| PS02.01 | Ước lượng π theo nhiều N và vẽ error bars qua runs | Chỉ ước lượng π đơn lẻ |
| PV01.01 | Ảnh xám 4×4, đường chéo, tổng pixel | Chuyển RGB sang grayscale |
| PD01.01 | Shape và aliasing của x[:,1] view/copy | Broadcasting và dịch cột |
| H02.01 | unittest trừ tồn kho: thường, 0, âm | unittest chuẩn hóa username |
| PT03.01 | Gradient 2D của x²+3xy và finite differences | Đạo hàm một biến x² |
| PW01.01 | Ánh xạ lỗi validation/404/500, không lộ chi tiết | Phân tích URL/query |
| K01.01 | timeit n=1000, median và mức dao động | đo n=100, chỉ báo minimum |
| M04.01 | SQL placeholder tra tên sản phẩm theo ID | Truy vấn người theo tên |

**Không được tự ghi thêm bài nào đã được chuyên gia chấp nhận**: các sửa đổi trên là hiệu đính kỹ thuật nội bộ và kiểm thử nguồn, chưa phải phản biện học thuật độc lập.

### Bằng chứng kiểm thử

- Workflow [#41994121787](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/41994121787): 7/7 lời giải nhóm I02/F01/PR01/PN03/PS02/PV01/PD01 và 93 ca N01.01 đã PASS CPython 3.15.2; 22 hợp đồng ngữ nghĩa cũ vẫn PASS.
- Workflow [#41994757838](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/41994757838): kiểm thử độc lập cho H02/PT03/PW01/K01/M04. Chỉ đổi thành PASS sau khi nhật ký thực tế xác nhận.
- Kiểm kê [#41993123233](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/41993123233): đủ 441 bài, 441 demo, 95 chương trình B, 441 hướng dẫn lời giải; không còn link hỏng.
- CPU + Keras [#41938644728](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/41938644728): PASS trên CPython 3.15.2 (bản nguồn trước hiệu đính); các thay đổi bài B cần kiểm tra độc lập và hồi quy mới.

## 2. Các phần vẫn chưa nghiệm thu toàn diện

- **GPU CUDA thực tế**: chưa có runner Linux x64 gắn nhãn gpu với NVIDIA GPU được xác nhận; tests/gpu_cuda_3152.py kiểm tra phần cứng, CUDA kernels, gradient, convolution và device training; chưa chạy trên GPU.
- **Phản biện độc lập**: 0/441 người đánh giá được xác thực; không thể dùng AI giả mạo tên chuyên gia. Phiếu review riêng kèm SHA và cổng giữ trạng thái PENDING.
- **Đáp án thiết kế và phát biểu phiên bản**: bộ lint báo 98 đáp án dạng thiết kế và 109 phát biểu có thể lỗi thời; đây chỉ là tín hiệu để kiểm tra, không phải 98/109 lỗi đã được xác minh.
- **Tính đúng sâu**: exit code 0 là smoke test; các thuật toán/chủ đề cần bài tập thực tiễn, case biên, kiểm thử âm và phản biện chuyên môn theo đúng đề.

## 3. Chặn phát hành sai

Cổng CPU + Keras, chứng cứ GPU và xác minh reviewer là các điều kiện khác nhau; không gắn nhãn FULLY_CERTIFIED chỉ từ cổng CPU. Draft PR #4 vẫn chưa merge main. Theo dõi [Issue #3](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/3), [Issue #7](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/7), [Issue #8](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/issues/8).
