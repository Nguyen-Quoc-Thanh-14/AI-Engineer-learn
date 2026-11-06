# Chương PV04 — Từ hình ảnh đến video và triển khai

> **Giai đoạn:** GD6 · **Học phần:** Computer Vision  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương PV04: Từ hình ảnh đến video và triển khai, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Image dataset quality và annotation agreement; Privacy, robustness và xử lý dữ liệu hình ảnh.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [PV04.01 — Image dataset quality và annotation agreement](BAI_HOC/PV04.01.md)
- [PV04.02 — Detection, segmentation và tracking](BAI_HOC/PV04.02.md)
- [PV04.03 — Latency và deployment trên thiết bị hạn chế](BAI_HOC/PV04.03.md)
- [PV04.04 — Privacy, robustness và xử lý dữ liệu hình ảnh](BAI_HOC/PV04.04.md)

## Tiên quyết

PD, PL

## Nguồn đối chiếu

- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

---

## PV04.01 — Image dataset quality và annotation agreement

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PV04 — Từ hình ảnh đến video và triển khai · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PL. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Image dataset quality và annotation agreement** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Image dataset quality cần label schema, duplicate detection, split theo nguồn và agreement giữa annotators.

**Ngữ cảnh thực tế:** Trong chương **Từ hình ảnh đến video và triển khai**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Đánh giá nhãn mơ hồ bằng adjudication; report tỷ lệ thiếu/sai và class imbalance.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
counts={'cat':90,'dog':10}
assert counts['cat']/sum(counts.values())==.9
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PV04.01_demo.py`](MA_MAU/PV04.01_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Dataset cực lớn nhưng bị leakage cùng subject vẫn cho kết quả ảo.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế quality gate về label agreement và tỉ lệ duplicates.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PV04_01.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PV04.01_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## PV04.02 — Detection, segmentation và tracking

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PV04 — Từ hình ảnh đến video và triển khai · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PL. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Detection, segmentation và tracking** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Detection tạo boxes, segmentation tạo masks, tracking nối detections qua thời gian với identity consistency.

**Ngữ cảnh thực tế:** Trong chương **Từ hình ảnh đến video và triển khai**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Đánh giá IoU, temporal continuity và ID switches trên video có ground truth.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
mask_a={1,2,3};mask_b={2,3,4}
iou=len(mask_a&mask_b)/len(mask_a|mask_b)
assert iou==.5
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PV04.02_demo.py`](MA_MAU/PV04.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Detection tốt từng frame chưa bảo đảm tracking IDs ổn định.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế metric đơn giản số ID switches trên 10 frames.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PV04_02.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PV04.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## PV04.03 — Latency và deployment trên thiết bị hạn chế

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PV04 — Từ hình ảnh đến video và triển khai · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PL. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Latency và deployment trên thiết bị hạn chế** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Edge deployment cân nhắc model size, latency, battery, memory và độ chính xác; quantization là tradeoff cần đo.

**Ngữ cảnh thực tế:** Trong chương **Từ hình ảnh đến video và triển khai**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Benchmark CPU/GPU/NPU với batch size phù hợp, report p95 và thermal throttling.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
latencies=[20,25,30,28]
assert max(latencies)<40
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PV04.03_demo.py`](MA_MAU/PV04.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Một model chạy ở 30 FPS trên GPU server không bảo đảm 30 FPS trên thiết bị thật.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết bảng resource budget thiết bị và kế hoạch benchmark cold/warm inference.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PV04_03.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PV04.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## PV04.04 — Privacy, robustness và xử lý dữ liệu hình ảnh

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PV04 — Từ hình ảnh đến video và triển khai · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PL. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Privacy, robustness và xử lý dữ liệu hình ảnh** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Xử lý hình ảnh có người/PII cần minimization, permissions, retention và kiểm adversarial robustness; công bố hạn chế model.

**Ngữ cảnh thực tế:** Trong chương **Từ hình ảnh đến video và triển khai**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Blur danh tính chỉ khi đáp ứng mục tiêu quyền riêng tư; kiểm input tampered/corrupted.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
policy={'storage':'minimal','access':'restricted','audit':True}
assert policy['audit']
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PV04.04_demo.py`](MA_MAU/PV04.04_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không coi blur ở độ phân giải thấp là ẩn danh không thể đảo ngược.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế test malformed image, access logging và retention deletion.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PV04_04.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PV04.04_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)
- [R29: TensorFlow Guide](https://www.tensorflow.org/guide)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Bổ sung lời giải B độc lập — v2.8

- [PV04.01 — lời giải](LOI_GIAI/PV04.01_loi_giai.md)
- [PV04.02 — lời giải](LOI_GIAI/PV04.02_loi_giai.md)
- [PV04.03 — lời giải](LOI_GIAI/PV04.03_loi_giai.md)
- [PV04.04 — lời giải](LOI_GIAI/PV04.04_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
