# Chương PL01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# PL01.01 — Tensor operations và broadcasting

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PL01 — Tensor và autodiff · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Tensor operations và broadcasting**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** PM, PT.

## 2. Khái niệm — Bản chất

Tensor là mảng đa chiều với phép toán số học; trong PyTorch, `torch.Tensor` mang `dtype`, `shape`, `device` và tùy chọn `requires_grad` để xây dựng đồ thị gradient tự động. Broadcasting và shape semantics gần NumPy nhưng GPU có chi phí truyền dữ liệu.

## 3. Nguyên lý và cơ chế từng bước

Ví dụ tensor 2x2, nhân elementwise rồi giảm về scalar, gọi backward để nhận gradient theo từng phần tử. Đạo hàm của x² là 2x.

## 4. Ví dụ tối thiểu có thể chạy

```python
import torch
x=torch.tensor([1.,2.,3.],requires_grad=True)
y=(x*x).sum()
y.backward()
assert torch.allclose(x.grad,torch.tensor([2.,4.,6.]))
print(x.grad.tolist())
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
[2.0, 4.0, 6.0]
```

**Thực hành:** chạy file `07_MA_VI_DU/PL01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng in-place operation tùy tiện trên tensor cần gradient; autograd có thể phát hiện lỗi version.
- **Trường hợp biên:** Tensor trên GPU cần chuyển về CPU trước khi dùng `.numpy()` trong nhiều trường hợp.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Kiến thức nền trước khi huấn luyện neural network và debug backpropagation.

## 7. Bài tập có yêu cầu kiểm chứng

Tạo tensor và tính gradient của `3*x*x + 2*x`; so sánh với đạo hàm viết tay.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PL01.01_loi_giai.md](LOI_GIAI/PL01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Tensor operations và broadcasting** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S03] Hands-On Machine Learning 2e — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [S04] Deep Learning with Python 1e — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R27] [Keras 3 Documentation](https://keras.io/keras_3/) — Chính thức thư viện.
- [R28] [PyTorch Tutorials](https://docs.pytorch.org/tutorials/) — Chính thức thư viện.
- [R29] [TensorFlow Guide](https://www.tensorflow.org/guide) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Autograd ghi phép tính tensor để lan truyền đạo hàm từ scalar loss về các leaf tensors có requires_grad=True; backward() cộng dồn vào .grad trừ khi được reset.

### Cách suy luận và thiết kế lời giải

Với hàm f(x)=sum(3x²+2x), gradient giải tích là 6x+2. Kiểm tra các giá trị âm, 0 và dương, rồi gọi backward hai lần có chủ ý để thấy gradient cộng dồn. Định nghĩa loss scalar tránh phải truyền gradient đầu vào cho backward.

### Phản ví dụ và ngộ nhận cần tránh

Không gọi .numpy() trực tiếp trên tensor có requires_grad=True; muốn đưa sang NumPy hãy detach rồi chuyển sang CPU khi cần.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`PL01.01_bai_tap_da_giai_v25.py`](MA_MAU/PL01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`PL01.01_loi_giai.md`](LOI_GIAI/PL01.01_loi_giai.md).
5. **Bài mở rộng:** So sánh autograd với sai phân hữu hạn và nêu sai số khi step quá nhỏ do floating-point cancellation.

**Nguồn kỹ thuật chính thức:** https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# PL01.02 — Automatic differentiation và gradients

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PL01 — Tensor và autodiff · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PM, PT. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Automatic differentiation và gradients** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Autodiff áp dụng chain rule trên computational graph; gradient của loss theo weight phục vụ optimization.

**Ngữ cảnh thực tế:** Trong chương **Tensor và autodiff**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Phân biệt leaf tensor, requires_grad và no_grad context; kiểm gradient bằng analytic derivative.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
import torch
x=torch.tensor(3.,requires_grad=True)
y=x*x;y.backward()
assert x.grad.item()==6
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PL01.02_demo.py`](MA_MAU/PL01.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không nhầm gradient accumulation với giá trị gradient của một batch duy nhất.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tính gradient f(x)=sin(x)*x và so finite differences.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PL01_02.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PL01.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S03: Hands-On Machine Learning 2e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S04: Deep Learning with Python 1e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


---

# PL01.03 — Thiết lập backend và GPU

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PL01 — Tensor và autodiff · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PM, PT. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Thiết lập backend và GPU** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Thiết bị CPU/GPU, backend và dtype ảnh hưởng kết quả/tốc độ; cần kiểm availability chứ không bắt buộc có GPU.

**Ngữ cảnh thực tế:** Trong chương **Tensor và autodiff**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Data và model phải cùng device; đo memory, batch size và deterministic controls.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
import torch
device='cuda' if torch.cuda.is_available() else 'cpu'
x=torch.ones(2,device=device)
assert x.sum().item()==2
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PL01.03_demo.py`](MA_MAU/PL01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không mặc định có CUDA hoặc MPS trên máy người học.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết script kiểm backend TensorFlow/Keras/PyTorch và báo phiên bản, device.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PL01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PL01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S03: Hands-On Machine Learning 2e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S04: Deep Learning with Python 1e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: PL01.01. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.


## Bổ sung lời giải B độc lập — v2.8

- [PL01.02 — lời giải](LOI_GIAI/PL01.02_loi_giai.md)
- [PL01.03 — lời giải](LOI_GIAI/PL01.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
