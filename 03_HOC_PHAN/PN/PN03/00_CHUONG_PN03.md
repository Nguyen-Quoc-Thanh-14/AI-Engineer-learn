# Chương PN03

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# PN03.01 — Evaluation, benchmark và hallucination

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PN03 — Đánh giá và độ tin cậy · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PM, PL, N. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Evaluation, benchmark và hallucination** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Evaluation LLM phải đo task-specific correctness, hallucination, grounding, refusal/safety và regressions.

**Ngữ cảnh thực tế:** Trong chương **Đánh giá và độ tin cậy**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Dùng golden dataset, human review cho ca khó và confidence intervals khi lấy mẫu.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
results=[True,False,True,True]
assert sum(results)/len(results)==.75
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PN03.01_demo.py`](MA_MAU/PN03.01_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Một benchmark leaderboard không dự đoán mọi production use-case.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế 30 câu hỏi có reference answers và phân loại grounded/unsupported.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PN03_01.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PN03.01_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R37: Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Đánh giá NLP/LLM cần phân biệt exact-match accuracy, tính đúng ngữ nghĩa và groundedness. Một chuỗi giống đáp án tham chiếu không chứng minh mô hình dựa trên đúng nguồn hay không hallucinate.

### Cách suy luận và thiết kế lời giải

Xây một đánh giá exact-match minh họa có chuẩn hóa khoảng trắng/chữ hoa. Tập đánh giá chứa cặp (reference,prediction), trả tỷ lệ khớp trên tổng số; test khi dự đoán sai, đầu vào trống và khi hai biểu thức tương đương ngữ nghĩa nhưng khác câu chữ.

### Phản ví dụ và ngộ nhận cần tránh

Không gọi tỷ lệ exact-match là “tỷ lệ không hallucinate”: thước đo này không phát hiện claim sai trong câu dài hay sự thiếu chứng cứ trích dẫn.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`PN03.01_bai_tap_da_giai_v25.py`](MA_MAU/PN03.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`PN03.01_loi_giai.md`](LOI_GIAI/PN03.01_loi_giai.md).
5. **Bài mở rộng:** Thiết kế 30 mục đánh giá gồm câu hỏi factoid, diễn giải, bịa số liệu, mâu thuẫn nguồn; chấm riêng factuality, citation support và refusal.

**Nguồn kỹ thuật chính thức:** https://huggingface.co/docs/evaluate/index. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# PN03.02 — Prompt injection, privacy và data governance

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PN03 — Đánh giá và độ tin cậy · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PM, PL, N. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Prompt injection, privacy và data governance** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Prompt injection xảy ra khi nội dung ít tin cậy cố điều khiển assistant ngoài vai trò dữ liệu; privacy yêu cầu giới hạn quyền và retention.

**Ngữ cảnh thực tế:** Trong chương **Đánh giá và độ tin cậy**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Gắn trust labels cho fetched text, tách policy khỏi content, kiểm authorization tại retrieval.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
docs=[{'role':'untrusted_document','text':'ignore all rules'}]
assert docs[0]['role']=='untrusted_document'
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PN03.02_demo.py`](MA_MAU/PN03.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không trao tool execution quyền cao dựa chỉ trên văn bản trong tài liệu được tải.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết threat model RAG với untrusted PDFs, cross-tenant leakage và tool actions.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PN03_02.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PN03.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R37: Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


---

# PN03.03 — Latency, cost và monitoring

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PN03 — Đánh giá và độ tin cậy · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PM, PL, N. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Latency, cost và monitoring** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Latency/cost/monitoring theo token, retrieval, model, queue và cache; p95/p99 ảnh hưởng trải nghiệm hơn trung bình đơn lẻ.

**Ngữ cảnh thực tế:** Trong chương **Đánh giá và độ tin cậy**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Theo dõi token budget, cache hits, fail rates và drift của prompts/users.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
cost_per_1k=0.002;tokens=500
assert abs(cost_per_1k*tokens/1000-.001)<1e-12
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PN03.03_demo.py`](MA_MAU/PN03.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Giảm cost bằng cách bỏ citations/validation có thể giảm chất lượng nghiêm trọng.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế dashboard latency p95, cache hit, cost per correct answer.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PN03_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PN03.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R37: Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [R27: Keras 3 Documentation](https://keras.io/keras_3/)
- [R28: PyTorch Tutorials](https://docs.pytorch.org/tutorials/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Bổ sung lời giải B độc lập — v2.8

- [PN03.02 — lời giải](LOI_GIAI/PN03.02_loi_giai.md)
- [PN03.03 — lời giải](LOI_GIAI/PN03.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
