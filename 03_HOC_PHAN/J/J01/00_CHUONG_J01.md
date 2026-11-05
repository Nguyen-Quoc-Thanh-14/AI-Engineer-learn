# Chương J01 — Object model và bộ nhớ

> **Giai đoạn:** GD5 · **Học phần:** Python internals và data model  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương J01: Object model và bộ nhớ, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Identity, reference và object lifetime; Garbage collection và cyclic references.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [J01.01 — Identity, reference và object lifetime](BAI_HOC/J01.01.md)
- [J01.02 — Reference counting trong CPython](BAI_HOC/J01.02.md)
- [J01.03 — Garbage collection và cyclic references](BAI_HOC/J01.03.md)

## Tiên quyết

C, D, E, F

## Nguồn đối chiếu

- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)
- [R12: CPython Developer Guide](https://devguide.python.org/)
- [R13: Python/C API Reference 3.15](https://docs.python.org/3.15/c-api/)
- [R14: CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html)

---

## J01.01 — Identity, reference và object lifetime

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD5 · **Chương:** J01 — Object model và bộ nhớ · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Identity, reference và object lifetime**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** C, D, E, F.

### 2. Khái niệm — Bản chất

Python object có identity, type và value. Tên biến là binding tới object; `is` kiểm tra identity, `==` so sánh bằng nhau theo quy tắc do kiểu định nghĩa. Lifetime phụ thuộc các tham chiếu và implementation; đừng dựa vào địa chỉ hay thời điểm thu hồi bộ nhớ như một phần hợp đồng ngôn ngữ.

### 3. Nguyên lý và cơ chế từng bước

Gán `b=a` không nhân bản list: hai tên trỏ cùng list. `c=a.copy()` tạo list mới (shallow copy); phần tử lồng nhau vẫn có thể dùng chung. Theo dõi id() chỉ để quan sát trong một lần thực thi, không dùng làm ID bền vững.

### 4. Ví dụ tối thiểu có thể chạy

```python
a=[1,2]
b=a
c=a.copy()
assert a is b
assert a is not c
assert a==c
b.append(3)
assert a==[1,2,3] and c==[1,2]
print(a,c)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
[1, 2, 3] [1, 2]
```

**Thực hành:** chạy file `07_MA_VI_DU/J01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `is` thay `==` cho số và chuỗi do interpreter có thể tái sử dụng đối tượng.
- **Trường hợp biên:** Shallow copy không copy sâu các object mutable lồng nhau.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Quan trọng cho mọi bài toán thay đổi trạng thái và debug reference.

### 7. Bài tập có yêu cầu kiểm chứng

Giải thích vì sao `x is 1000` không phải kiểm tra nội dung đáng tin cậy; viết thử nghiệm list aliasing.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [J01.01_loi_giai.md](LOI_GIAI/J01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Identity, reference và object lifetime** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.
- [R12] [CPython Developer Guide](https://devguide.python.org/) — Gốc triển khai.
- [R13] [Python/C API Reference 3.15](https://docs.python.org/3.15/c-api/) — Gốc triển khai.
- [R14] [CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html) — Gốc triển khai.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## J01.02 — Reference counting trong CPython

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD5 · **Chương:** J01 — Object model và bộ nhớ · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Reference counting trong CPython**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** C, D, E, F.

### 2. Khái niệm — Bản chất

CPython truyền thống sử dụng **reference counting** kết hợp cơ chế dọn vòng tham chiếu. Đây là chi tiết triển khai, không phải bảo đảm rằng mọi Python runtime sẽ giải phóng đối tượng ngay khi mất tên tham chiếu. Free-threaded CPython có thể có chiến lược tối ưu khác.

### 3. Nguyên lý và cơ chế từng bước

Khi nhiều tên giữ một object, xóa một binding không xóa object nếu vẫn còn tham chiếu. `sys.getrefcount()` đo mức tham chiếu tại một thời điểm (bao gồm tham chiếu tạm do lời gọi), không phù hợp để suy ra chính xác lifetime ở mọi interpreter.

### 4. Ví dụ tối thiểu có thể chạy

```python
a=[]
b=a
assert b is a
del a
b.append(1)
assert b==[1]
print('Đối tượng vẫn tồn tại:',b)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
Đối tượng vẫn tồn tại: [1]
```

**Thực hành:** chạy file `07_MA_VI_DU/J01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** `del name` xóa binding, không buộc thu hồi đối tượng trong mọi trường hợp.
- **Trường hợp biên:** Object có thể sống nhờ container, closure, traceback hoặc global reference.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng hiểu biết này để tránh memory leaks; không dựa vào thời điểm destructor.

### 7. Bài tập có yêu cầu kiểm chứng

Viết ví dụ hai tên cùng tham chiếu object; chỉ xóa một tên, giải thích object còn sống.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [J01.02_loi_giai.md](LOI_GIAI/J01.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Reference counting trong CPython** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.
- [R12] [CPython Developer Guide](https://devguide.python.org/) — Gốc triển khai.
- [R13] [Python/C API Reference 3.15](https://docs.python.org/3.15/c-api/) — Gốc triển khai.
- [R14] [CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html) — Gốc triển khai.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## J01.03 — Garbage collection và cyclic references

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD5 · **Chương:** J01 — Object model và bộ nhớ · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Garbage collection và cyclic references**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** C, D, E, F.

### 2. Khái niệm — Bản chất

**Cyclic references** xuất hiện khi các object tham chiếu thành vòng. Reference counting riêng lẻ không giải quyết được vòng mà mọi object đều không còn reachable từ chương trình. `gc` của CPython nhận diện các vòng có thể thu gom theo chính sách runtime.

### 3. Nguyên lý và cơ chế từng bước

Hai list tự tham chiếu minh họa vòng; dùng `gc.collect()` trong thử nghiệm để quan sát nhưng không coi số object thu gom là hợp đồng ổn định. Tránh phụ thuộc `__del__` hoặc số collection chính xác.

### 4. Ví dụ tối thiểu có thể chạy

```python
import gc
x=[]
x.append(x)
assert x[0] is x
del x
collected=gc.collect()
assert isinstance(collected,int)
print('GC đã chạy')
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
GC đã chạy
```

**Thực hành:** chạy file `07_MA_VI_DU/J01.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không coi `gc.collect()` là API để fix cấu trúc giữ tham chiếu vô thời hạn.
- **Trường hợp biên:** Object dùng weakref hoặc finalizer có quy tắc dọn dẹp riêng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Khi debug rò rỉ bộ nhớ, phân tích retention graph thay vì chỉ gọi gc thủ công.

### 7. Bài tập có yêu cầu kiểm chứng

Dựng vòng tham chiếu giữa hai dict; xóa hai binding; giải thích vì sao vòng không còn reachable.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [J01.03_loi_giai.md](LOI_GIAI/J01.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Garbage collection và cyclic references** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.
- [R12] [CPython Developer Guide](https://devguide.python.org/) — Gốc triển khai.
- [R13] [Python/C API Reference 3.15](https://docs.python.org/3.15/c-api/) — Gốc triển khai.
- [R14] [CPython free threading HOWTO](https://docs.python.org/3.15/howto/free-threading-python.html) — Gốc triển khai.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: J01.01, J01.02, J01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
