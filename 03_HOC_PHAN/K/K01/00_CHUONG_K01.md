# Chương K01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# K01.01 — Benchmark, baseline và warmup

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD5 · **Chương:** K01 — Đo lường đúng cách · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Benchmark, baseline và warmup**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** I, H, J.

## 2. Khái niệm — Bản chất

Benchmark hợp lệ phải định nghĩa workload, baseline, môi trường và tiêu chí đo. Warmup có thể ảnh hưởng bộ nhớ đệm và trạng thái runtime. Một lần chạy không đủ chứng minh cách tối ưu nhanh hơn; phải ghi lại độ dao động, kích thước đầu vào và phiên bản Python.

## 3. Nguyên lý và cơ chế từng bước

`timeit.repeat()` đo nhiều lần, dùng median/mean tùy mục tiêu. Cùng mã có thể cho kết quả khác vì CPU scaling, garbage collector, I/O hoặc background process. Đừng diễn giải chênh lệch nhỏ hơn nhiễu thành lợi thế chắc chắn.

## 4. Ví dụ tối thiểu có thể chạy

```python
import timeit
samples=timeit.repeat('sum(range(100))',number=100,repeat=3)
assert len(samples)==3
assert all(x>=0 for x in samples)
print('số mẫu:',len(samples))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
số mẫu: 3
```

**Thực hành:** chạy file `07_MA_VI_DU/K01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không benchmark bằng `print()` hoặc mạng rồi quy kết cho CPU của thuật toán.
- **Trường hợp biên:** Microbenchmark có thể khác hệ thống thật do cache, vectorization hoặc concurrency.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chỉ tối ưu khi có baseline và mục tiêu định lượng rõ.

## 7. Bài tập có yêu cầu kiểm chứng

So sánh hai cách tạo bình phương n=1_000 bằng `timeit`, ghi median và mức dao động.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [K01.01_loi_giai.md](LOI_GIAI/K01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Benchmark, baseline và warmup** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R09] [Profiling package 3.15](https://docs.python.org/3.15/library/profiling.html) — Gốc.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R23] [NumPy Manual](https://numpy.org/doc/stable/user/basics) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Benchmark chỉ cung cấp bằng chứng về một khối lượng công việc trong một môi trường đo cụ thể. Kết quả thời gian không phải định luật phổ quát; cần có baseline, kiểm tra tính đúng và nhiều lượt đo.

### Cách suy luận và thiết kế lời giải

Dùng timeit.repeat với number và repeat cố định, báo cáo các phép đo riêng và giá trị tối thiểu, không đặt assertion cứng rằng cách A luôn nhanh hơn cách B. Nên ghi Python version, CPU, dữ liệu và môi trường.

### Phản ví dụ và ngộ nhận cần tránh

Tránh dùng time.time để đo những đoạn quá ngắn một lần; độ nhiễu hệ thống có thể lớn hơn thời gian chương trình.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`K01.01_bai_tap_da_giai_v25.py`](MA_MAU/K01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`K01.01_loi_giai.md`](LOI_GIAI/K01.01_loi_giai.md).
5. **Bài mở rộng:** Đo list comprehension và vòng for cho dãy dài 10, 1000, 100000 phần tử; ghi lại đường xu hướng và thảo luận O(n).

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/timeit.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# K01.02 — timeit, cProfile và sampling profiler

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD5 · **Chương:** K01 — Đo lường đúng cách · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **timeit, cProfile và sampling profiler**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** I, H, J.

## 2. Khái niệm — Bản chất

`timeit` phù hợp đo đoạn mã ngắn; `cProfile` ghi nhận thống kê lời gọi hàm và thời gian; sampling profiler lấy mẫu stack để tìm vị trí tốn thời gian với tradeoff về độ chi tiết và overhead. Python 3.15 bổ sung gói `profiling` và Tachyon; cần chạy trực tiếp bằng Python 3.15 để kiểm chứng các API mới.

## 3. Nguyên lý và cơ chế từng bước

Ví dụ dùng `cProfile.Profile()` có sẵn trên Python 3.13. Đọc `stats` theo cumulative time thay vì chỉ xem một call nhanh/đắt. Kết quả phụ thuộc workload; phải ghi phiên bản runtime.

## 4. Ví dụ tối thiểu có thể chạy

```python
import cProfile, pstats, io
p=cProfile.Profile()
p.enable()
sum(i*i for i in range(1000))
p.disable()
out=io.StringIO()
pstats.Stats(p,stream=out).sort_stats('cumtime').print_stats(3)
assert 'function calls' in out.getvalue()
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/K01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Đừng coi số liệu profiler là thời gian sản xuất; instrumentation làm tăng overhead.
- **Trường hợp biên:** Sampling có thể bỏ qua các call rất ngắn; profiler mới trên 3.15 cần tài liệu phiên bản.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng profiler để tìm hotspot trước khi thay đổi cấu trúc dữ liệu.

## 7. Bài tập có yêu cầu kiểm chứng

Tự profile một hàm lọc và sort 10.000 số; giải thích hai hotspot.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [K01.02_loi_giai.md](LOI_GIAI/K01.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **timeit, cProfile và sampling profiler** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R09] [Profiling package 3.15](https://docs.python.org/3.15/library/profiling.html) — Gốc.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R23] [NumPy Manual](https://numpy.org/doc/stable/user/basics) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# K01.03 — Độ nhiễu đo và diễn giải kết quả

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD5 · **Chương:** K01 — Đo lường đúng cách · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** I, H, J. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Độ nhiễu đo và diễn giải kết quả** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Đo hiệu năng có nhiễu do warmup, clock, scheduling, CPU scaling, filesystem cache và GC.

**Ngữ cảnh thực tế:** Trong chương **Đo lường đúng cách**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Dùng nhiều lượt, thống kê median/IQR, đo workloads đại diện và ghi môi trường; benchmark với `%timeit`/`timeit` tùy tình huống.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
import timeit
samples=timeit.repeat('sum(range(100))', repeat=3, number=1000)
assert len(samples)==3 and all(x>=0 for x in samples)
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`K01.03_demo.py`](MA_MAU/K01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Đừng suy ra tốc độ production từ một phép đo có dữ liệu đầu vào quá nhỏ.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thử ít nhất 10 repeat và so sánh median khi number=1 với number=1000.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_K01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/K01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R09: Profiling package 3.15](https://docs.python.org/3.15/library/profiling.html)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R23: NumPy Manual](https://numpy.org/doc/stable/user/basics)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: K01.01, K01.02. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.


## Bổ sung lời giải B độc lập — v2.8

- [K01.03 — lời giải](LOI_GIAI/K01.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
