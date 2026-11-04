# Chương L04 — Async Python

> **Giai đoạn:** GD4 · **Học phần:** Concurrency, parallelism và asyncio  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương L04: Async Python, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Coroutine, await và event loop; Async I/O và tránh blocking calls.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [L04.01 — Coroutine, await và event loop](BAI_HOC/L04.01.md)
- [L04.02 — asyncio tasks và gather](BAI_HOC/L04.02.md)
- [L04.03 — Async I/O và tránh blocking calls](BAI_HOC/L04.03.md)

## Tiên quyết

H, F, M01

## Nguồn đối chiếu

- [R14: CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html)
- [R15: asyncio Coroutines and Tasks 3.15](https://docs.python.org/3.15/library/asyncio-task.html)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)

---

## L04.01 — Coroutine, await và event loop

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** L04 — Async Python · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Coroutine, await và event loop**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** H, F, M01.

### 2. Khái niệm — Bản chất

Coroutine được định nghĩa bằng `async def` và có thể tạm dừng bằng `await`; event loop lập lịch các tác vụ khi chúng nhường quyền. Việc viết async không tự động biến CPU-bound code thành song song.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
import asyncio
async def lay_du_lieu():
    await asyncio.sleep(0)
    return 5
assert asyncio.run(lay_du_lieu())==5
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/L04.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không gọi time.sleep trong event loop vì chặn các task khác.
- **Trường hợp biên:** `asyncio.run` không dùng lồng vào một event loop đang chạy.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Viết async function nhận `n`, await sleep(0) rồi trả n**2; kiểm thử asyncio.run.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [L04.01_loi_giai.md](LOI_GIAI/L04.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Coroutine, await và event loop** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## L04.02 — asyncio tasks và gather

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** L04 — Async Python · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **asyncio tasks và gather**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** H, F, M01.

### 2. Khái niệm — Bản chất

`asyncio.create_task` tạo và lập lịch Task; `asyncio.gather` chờ nhiều awaitables và trả kết quả theo thứ tự đối số. Concurrency không đảm bảo các coroutine chạy đồng thời trên nhiều CPU core.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
import asyncio
async def f(x):
    await asyncio.sleep(0)
    return x*2
async def main():
    return await asyncio.gather(f(1),f(2))
assert asyncio.run(main())==[2,4]
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/L04.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không tạo Task rồi quên quản lý vòng đời; task bỏ mặc có thể fail mà không được quan sát.
- **Trường hợp biên:** gather mặc định có semantics xử lý exception/cancellation cần đọc tài liệu phiên bản đích.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo 3 coroutine trả x+1, gather rồi assert đúng thứ tự kết quả.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [L04.02_loi_giai.md](LOI_GIAI/L04.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **asyncio tasks và gather** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## L04.03 — Async I/O và tránh blocking calls

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** L04 — Async Python · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Async I/O và tránh blocking calls**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** H, F, M01.

### 2. Khái niệm — Bản chất

Async I/O tận dụng thời gian chờ I/O bằng cách nhường quyền cho event loop. Với thao tác blocking ngoài async, dùng thread offloading hoặc thư viện async thực sự; cần áp backpressure.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
import asyncio
async def f(x):
    await asyncio.sleep(0)
    return x
async def main():
    sem=asyncio.Semaphore(2)
    async def run(x):
        async with sem:return await f(x)
    return await asyncio.gather(*(run(i) for i in range(4)))
assert asyncio.run(main())==[0,1,2,3]
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/L04.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Async không có nghĩa giảm độ phức tạp hoặc không thể phát sinh race condition.
- **Trường hợp biên:** Không nhầm timeout với cancellation cleanup; tài nguyên cần đóng đúng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Dùng semaphore giới hạn số tác vụ xử lý đồng thời.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [L04.03_loi_giai.md](LOI_GIAI/L04.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Async I/O và tránh blocking calls** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: L04.01, L04.02, L04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
