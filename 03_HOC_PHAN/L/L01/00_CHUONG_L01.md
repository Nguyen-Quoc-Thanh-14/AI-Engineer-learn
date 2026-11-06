# Chương L01 — Mô hình thực thi

> **Giai đoạn:** GD4 · **Học phần:** Concurrency, parallelism và asyncio  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương L01: Mô hình thực thi, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Process, thread, task; CPU-bound, I/O-bound và chọn mô hình.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [L01.01 — Process, thread, task](BAI_HOC/L01.01.md)
- [L01.02 — Concurrency so với parallelism](BAI_HOC/L01.02.md)
- [L01.03 — CPU-bound, I/O-bound và chọn mô hình](BAI_HOC/L01.03.md)

## Tiên quyết

H, F, M01

## Nguồn đối chiếu

- [R14: CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html)
- [R15: asyncio Coroutines and Tasks 3.15](https://docs.python.org/3.15/library/asyncio-task.html)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)

---

## L01.01 — Process, thread, task

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** L01 — Mô hình thực thi · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Process, thread, task**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** H, F, M01.

### 2. Khái niệm — Bản chất

Process, thread và coroutine task là các đơn vị đồng thời khác nhau. Process có không gian địa chỉ riêng; thread trong cùng process chia sẻ bộ nhớ; asyncio Task là đơn vị lập lịch coroutine bởi event loop. Concurrency không đồng nghĩa parallelism; tác vụ I/O thường phù hợp asyncio hoặc thread.

### 3. Nguyên lý và cơ chế từng bước

Tạo hai coroutine ngắn với `asyncio.gather()`; lịch trình có thể xen kẽ ở các `await`. Đoạn ví dụ không khởi chạy thread hoặc process; `await` cho event loop cơ hội chạy coroutine khác.

### 4. Ví dụ tối thiểu có thể chạy

```python
import asyncio
async def task(name):
    await asyncio.sleep(0)
    return name
async def main():
    results=await asyncio.gather(task('A'),task('B'))
    assert results==['A','B']
    return results
print(asyncio.run(main()))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
['A', 'B']
```

**Thực hành:** chạy file `07_MA_VI_DU/L01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng asyncio cho mọi đoạn tính toán CPU-bound; await không tự biến CPU thành song song.
- **Trường hợp biên:** `asyncio.run()` không thể gọi lồng bên trong event loop đang chạy.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn mô hình dựa vào workload, shared state và vòng đời tác vụ.

### 7. Bài tập có yêu cầu kiểm chứng

Giải thích vì sao gọi `time.sleep(1)` bên trong coroutine làm block loop.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [L01.01_loi_giai.md](LOI_GIAI/L01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Process, thread, task** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R14] [CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html) — Gốc triển khai.
- [R15] [asyncio Coroutines and Tasks 3.15](https://docs.python.org/3.15/library/asyncio-task.html) — Gốc.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## L01.02 — Concurrency so với parallelism

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD4 · **Chương:** L01 — Mô hình thực thi · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** H, F, M01. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Concurrency so với parallelism** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Concurrency là các tác vụ có thể tiến triển xen kẽ; parallelism là thực thi thực sự đồng thời trên nhiều resource.

**Ngữ cảnh thực tế:** Trong chương **Mô hình thực thi**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Threads phù hợp I/O và đôi khi CPU tùy GIL/free-threaded build; processes cô lập address space; asyncio cooperative scheduling.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as pool:
    assert list(pool.map(lambda x:x*x, [2,3]))==[4,9]
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`L01.02_demo.py`](MA_MAU/L01.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không đồng nghĩa “có nhiều thread” với “chạy CPU nhanh hơn” trên mọi CPython.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Phân tích lựa chọn threads vs processes cho I/O-bound và CPU-bound trên CPython mặc định.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_L01_02.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/L01.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R14: CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html)
- [R15: asyncio Coroutines and Tasks 3.15](https://docs.python.org/3.15/library/asyncio-task.html)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## L01.03 — CPU-bound, I/O-bound và chọn mô hình

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD4 · **Chương:** L01 — Mô hình thực thi · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** H, F, M01. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **CPU-bound, I/O-bound và chọn mô hình** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

CPU-bound chiếm thời gian tính toán; I/O-bound thường chờ disk/network. Cần đo workload và overhead serialization/scheduling.

**Ngữ cảnh thực tế:** Trong chương **Mô hình thực thi**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Dùng async cho I/O có API nonblocking; threads cho blocking I/O; processes hoặc native release-GIL cho CPU.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
from time import perf_counter
start=perf_counter()
result=sum(i*i for i in range(10000))
assert result>0 and perf_counter()-start>=0
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`L01.03_demo.py`](MA_MAU/L01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Chọn asyncio không làm vòng lặp tính toán CPU tự động nhanh hơn.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế benchmark I/O giả lập và CPU thuần, nêu vì sao dùng model khác nhau.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_L01_03.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/L01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- [R14: CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html)
- [R15: asyncio Coroutines and Tasks 3.15](https://docs.python.org/3.15/library/asyncio-task.html)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: L01.01. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.


## Bổ sung lời giải B độc lập — v2.8

- [L01.02 — lời giải](LOI_GIAI/L01.02_loi_giai.md)
- [L01.03 — lời giải](LOI_GIAI/L01.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
