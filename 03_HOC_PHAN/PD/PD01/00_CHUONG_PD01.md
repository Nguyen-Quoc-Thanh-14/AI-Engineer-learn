# Chương PD01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# PD01.01 — ndarray, dtype và shape

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PD01 — NumPy · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **ndarray, dtype và shape**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** C, G, H.

## 2. Khái niệm — Bản chất

`numpy.ndarray` là cấu trúc n chiều có `shape` và `dtype` xác định. Mảng NumPy có semantics khác list Python: phép toán số học thường thực hiện elementwise, và slicing có thể trả view dùng chung buffer. Không coi một array với `dtype=object` là vector số thuần.

## 3. Nguyên lý và cơ chế từng bước

Tạo mảng 2x3 kiểu int64 (nếu platform hỗ trợ), truy cập shape và axis. Phép `.sum(axis=0)` tổng từng cột; axis=1 tổng từng hàng.

## 4. Ví dụ tối thiểu có thể chạy

```python
import numpy as np
x=np.array([[1,2,3],[4,5,6]],dtype=np.int64)
assert x.shape==(2,3)
assert x.dtype==np.dtype('int64')
assert x.sum(axis=0).tolist()==[5,7,9]
print(x.shape)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(2, 3)
```

**Thực hành:** chạy file `07_MA_VI_DU/PD01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `if array:` khi có nhiều phần tử; dùng `array.any()` hoặc `array.all()` theo ý nghĩa.
- **Trường hợp biên:** Slicing view và fancy-indexing copy có thể tạo side effect khác nhau.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Nền tảng cho pandas, ML, xử lý ảnh và khoa học tính toán.

## 7. Bài tập có yêu cầu kiểm chứng

Giải thích shape của `x[:, 1]`, thử tạo view rồi chỉnh và quan sát dữ liệu gốc.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PD01.01_loi_giai.md](LOI_GIAI/PD01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **ndarray, dtype và shape** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R23] [NumPy Manual](https://numpy.org/doc/stable/user/basics) — Chính thức thư viện.
- [R24] [pandas User Guide / CoW](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) — Chính thức thư viện.
- [R38] [Apache Arrow Python Docs](https://arrow.apache.org/docs/python/) — Chính thức thư viện.
- [R39] [pandas 3.1 Release Notes](https://pandas.pydata.org/docs/whatsnew/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

NumPy ndarray có shape, ndim và dtype; vectorized operations thực hiện trên nhiều phần tử, nhưng broadcasting chỉ hợp lệ khi kích thước từng trục từ phải sang trái bằng nhau hoặc một trong hai là 1.

### Cách suy luận và thiết kế lời giải

Kiểm tra đầu vào có đúng hai chiều và chiều cột bằng chiều vector offset trước khi cộng; chuyển dtype sang float để hạn chế tràn số nguyên. Khi shape không tương thích, trả ValueError có nghĩa thay vì dựa hoàn toàn vào exception sâu trong NumPy.

### Phản ví dụ và ngộ nhận cần tránh

Không nhầm `array * array` với nhân ma trận (`@`); và không cho rằng mọi phép NumPy đều tránh tạo thêm bộ nhớ trung gian.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`PD01.01_bai_tap_da_giai_v25.py`](MA_MAU/PD01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`PD01.01_loi_giai.md`](LOI_GIAI/PD01.01_loi_giai.md).
5. **Bài mở rộng:** So sánh memory usage khi tính trên mảng 1 triệu phần tử với xử lý theo khối và giải thích trade-off.

**Nguồn kỹ thuật chính thức:** https://numpy.org/doc/stable/user/basics.broadcasting.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# PD01.02 — Broadcasting và vectorization

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PD01 — NumPy · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Broadcasting và vectorization**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** C, G, H.

## 2. Khái niệm — Bản chất

Broadcasting mở rộng khái niệm phép toán elementwise giữa các shape tương thích bằng cách so kích thước từ phải sang trái: hai chiều hợp lệ khi bằng nhau hoặc một trong hai bằng 1. Vectorization giảm overhead vòng lặp Python nhưng không loại bỏ mọi chi phí bộ nhớ.

## 3. Nguyên lý và cơ chế từng bước

Mảng shape (2,3) cộng vector shape (3,) được broadcast theo từng hàng. Shape (2,) không khớp chiều cuối cùng 3 nên không thể cộng trực tiếp.

## 4. Ví dụ tối thiểu có thể chạy

```python
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
v=np.array([10,20,30])
y=x+v
assert y.tolist()==[[11,22,33],[14,25,36]]
assert y.shape==(2,3)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/PD01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không lạm dụng broadcast để tạo tensor trung gian khổng lồ; tính memory footprint.
- **Trường hợp biên:** Mismatch shape phát sinh ValueError thay vì tự đoán chiều.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn broadcasting khi hình dạng dữ liệu và đơn vị tính rõ ràng.

## 7. Bài tập có yêu cầu kiểm chứng

So sánh vectorization `x**2` với list comprehension cho 4 số, kiểm tra kết quả cùng nghĩa.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PD01.02_loi_giai.md](LOI_GIAI/PD01.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Broadcasting và vectorization** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R23] [NumPy Manual](https://numpy.org/doc/stable/user/basics) — Chính thức thư viện.
- [R24] [pandas User Guide / CoW](https://pandas.pydata.org/docs/user_guide/copy_on_write.html) — Chính thức thư viện.
- [R38] [Apache Arrow Python Docs](https://arrow.apache.org/docs/python/) — Chính thức thư viện.
- [R39] [pandas 3.1 Release Notes](https://pandas.pydata.org/docs/whatsnew/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# PD01.03 — Array I/O, memory layout và performance

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PD01 — NumPy · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** C, G, H. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Array I/O, memory layout và performance** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

NumPy arrays có dtype và memory layout; contiguous vs strided ảnh hưởng I/O và hiệu năng.

**Ngữ cảnh thực tế:** Trong chương **NumPy**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

`np.save/load` bảo toàn dtype/shape, còn memmap cho phép truy cập phần file mà không nạp tất cả.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
import numpy as np
a=np.arange(8).reshape(2,4)
assert a.flags.c_contiguous and a.strides[1]==a.itemsize
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PD01.03_demo.py`](MA_MAU/PD01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không mặc định array view là bản copy độc lập.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thử transpose, `.copy()`, `np.save` và ghi nhận strides.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PD01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PD01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R23: NumPy Manual](https://numpy.org/doc/stable/user/basics)
- [R24: pandas User Guide / CoW](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [R38: Apache Arrow Python Docs](https://arrow.apache.org/docs/python/)
- [R39: pandas 3.1 Release Notes](https://pandas.pydata.org/docs/whatsnew/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: PD01.01, PD01.02. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.


## Bổ sung lời giải B độc lập — v2.8

- [PD01.03 — lời giải](LOI_GIAI/PD01.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
