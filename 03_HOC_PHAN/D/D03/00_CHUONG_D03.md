# Chương D03 — Tên, scope và namespace

> **Giai đoạn:** GD2 · **Học phần:** Hàm và mô hình lập trình nâng cao  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương D03: Tên, scope và namespace, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: LEGB và lexical scope; Namespace, shadowing và lỗi UnboundLocalError.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [D03.01 — LEGB và lexical scope](BAI_HOC/D03.01.md)
- [D03.02 — global, nonlocal và rebinding](BAI_HOC/D03.02.md)
- [D03.03 — Namespace, shadowing và lỗi UnboundLocalError](BAI_HOC/D03.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)
- [R10: Python typing specification](https://typing.python.org/en/latest/spec/)
- [R19: mypy Documentation](https://mypy.readthedocs.io/en/stable/)

---

## D03.01 — LEGB và lexical scope

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D03 — Tên, scope và namespace · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **LEGB và lexical scope**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Scope** là vùng xác định binding của tên; LEGB tóm tắt thứ tự tìm tên trong nhiều tình huống: Local, Enclosing, Global, Builtins. **Lexical scope** dựa vào vị trí định nghĩa, không phụ thuộc hàm được gọi từ đâu.

### 3. Nguyên lý và cơ chế từng bước

Tên `x` trong `inner` được tìm trong local rồi enclosing (ở `outer`). Hàm gọi `inner` không thay đổi phạm vi lexical của `inner`.

### 4. Ví dụ tối thiểu có thể chạy

```python
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        return x
    return inner
f = outer()
assert f() == 'enclosing'
print(f())
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
enclosing
```

**Thực hành:** chạy file `07_MA_VI_DU/D03.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** LEGB chỉ là mô hình ghi nhớ; các trường hợp như comprehension scope và class body có quy tắc đặc biệt.
- **Trường hợp biên:** Một local binding (dù gán sau dòng đọc) có thể làm phát sinh UnboundLocalError.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng tham số tường minh khi biến toàn cục tạo phụ thuộc khó kiểm thử.

### 7. Bài tập có yêu cầu kiểm chứng

Viết hàm lồng nhau lấy cấu hình từ enclosing scope, kiểm tra khi tồn tại tên trùng ở module.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D03.01_loi_giai.md](LOI_GIAI/D03.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **LEGB và lexical scope** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## D03.02 — global, nonlocal và rebinding

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D03 — Tên, scope và namespace · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **global, nonlocal và rebinding**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

`global` yêu cầu binding tới module scope, còn `nonlocal` yêu cầu binding tới enclosing function scope gần phù hợp. Đây là thay đổi quy tắc *gán tên*, không phải điều kiện bắt buộc để thay đổi nội dung của đối tượng mutable.

### 3. Nguyên lý và cơ chế từng bước

Trong ví dụ, `nonlocal` cập nhật một số nguyên thuộc scope `tao`. Nếu không khai báo, gán `dem += 1` coi `dem` là local và đọc trước gán sẽ gây UnboundLocalError.

### 4. Ví dụ tối thiểu có thể chạy

```python
def tao():
    dem=0
    def tang():
        nonlocal dem
        dem += 1
        return dem
    return tang
f=tao()
assert [f(),f()] == [1,2]
print(f())
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
3
```

**Thực hành:** chạy file `07_MA_VI_DU/D03.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `global` như giải pháp mặc định cho dữ liệu dùng chung; dễ tạo phụ thuộc và lỗi concurrency.
- **Trường hợp biên:** `nonlocal` phải trỏ tới binding trong enclosing function scope; không được tự tạo một binding không tồn tại.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn nonlocal khi trạng thái rất nhỏ; nếu nhiều thao tác, ưu tiên class.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo factory `tao_vi()` có `nonlocal vi`, cho phép tăng chỉ số; giải thích vì sao không cần `global`.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D03.02_loi_giai.md](LOI_GIAI/D03.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **global, nonlocal và rebinding** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## D03.03 — Namespace, shadowing và lỗi UnboundLocalError

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D03 — Tên, scope và namespace · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Namespace, shadowing và lỗi UnboundLocalError**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Namespace** là ánh xạ tên tới đối tượng. **Shadowing** xảy ra khi tên trong scope gần hơn che tên trùng ở scope ngoài. `UnboundLocalError` xảy ra khi local binding bị tham chiếu trước khi có giá trị.

### 3. Nguyên lý và cơ chế từng bước

Trước khi chạy hàm, trình biên dịch xác định một số local binding qua phép gán trong thân hàm; vì vậy thứ tự dòng không thể tự chuyển biến thành global lookup.

### 4. Ví dụ tối thiểu có thể chạy

```python
ten='ngoai'
def demo():
    ten='trong'
    return ten
assert demo()=='trong'
assert ten=='ngoai'
print(demo(),ten)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
trong ngoai
```

**Thực hành:** chạy file `07_MA_VI_DU/D03.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không đặt tên biến `list`, `dict`, `sum`, `id` khi sau đó còn muốn gọi builtins tương ứng.
- **Trường hợp biên:** Hàm có `x += 1` mà `x` chưa khởi tạo trong local thường phát sinh UnboundLocalError; dùng tham số hoặc nonlocal tùy ý đồ.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Đặt tên cục bộ rõ ý nghĩa thay vì cố tận dụng tên ngắn từ builtins.

### 7. Bài tập có yêu cầu kiểm chứng

Viết hàm dùng tên tham số `sum` và trình bày rủi ro che built-in `sum`; đề xuất tên khác.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D03.03_loi_giai.md](LOI_GIAI/D03.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Namespace, shadowing và lỗi UnboundLocalError** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: D03.01, D03.02, D03.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
