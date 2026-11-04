# Chương D02

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# D02.01 — Decorator function và cú pháp @

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D02 — Decorator và chức năng chéo · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Decorator function và cú pháp @**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

## 2. Khái niệm — Bản chất

**Decorator** là callable nhận một hàm hoặc class và trả về một đối tượng thay thế. `@decorator` phía trước `def f` tương đương gán `f = decorator(f)` sau khi tạo hàm. Decorator phù hợp cho hành vi áp dụng xuyên suốt như đo thời gian, kiểm tra quyền, cache; không nên che giấu nghiệp vụ.

## 3. Nguyên lý và cơ chế từng bước

`nhat_ky()` nhận hàm gốc rồi tạo wrapper có `*args, **kwargs`; wrapper gọi hàm gốc và trả về kết quả. Decorator chạy khi định nghĩa được thực thi, còn wrapper chạy tại thời điểm gọi tên đã được trang trí.

## 4. Ví dụ tối thiểu có thể chạy

```python
def ghi_nhan(ham):
    def wrapper(*args, **kwargs):
        kq = ham(*args, **kwargs)
        return {'ket_qua': kq}
    return wrapper

@ghi_nhan
def cong(a, b):
    return a + b

assert cong(2, 5) == {'ket_qua': 7}
print(cong(2, 5))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
{'ket_qua': 7}
```

**Thực hành:** chạy file `07_MA_VI_DU/D02.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Decorator không phải cú pháp chỉ dành cho logging; và wrapper không truyền tham số/return sẽ âm thầm làm hỏng API.
- **Trường hợp biên:** Decorators xếp chồng chạy theo thứ tự từ dưới lên khi áp dụng; hành vi gọi hàm có thể thay đổi đáng kể.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn decorator khi hành vi áp dụng nhất quán, dễ giải thích và được phép thay đổi hợp đồng hàm.

## 7. Bài tập có yêu cầu kiểm chứng

Tạo decorator `kiem_tra_khong_am` từ chối số âm trước khi gọi hàm một đối số.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D02.01_loi_giai.md](LOI_GIAI/D02.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Decorator function và cú pháp @** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Decorator nhận callable và trả lại callable khác. Kết quả trang trí là đối tượng được gán cho tên hàm, không đơn thuần một câu lệnh được chạy khi gọi hàm.

### Cách suy luận và thiết kế lời giải

functools.wraps giúp bảo tồn tên và docstring để kiểm tra, logging và tài liệu API không bị méo. Trong bài tập, wrapper xác thực tham số trước khi gọi hàm gốc và giữ nguyên giá trị trả về.

### Phản ví dụ và ngộ nhận cần tránh

Không bỏ quên return wrapper hoặc return của hàm bọc; hai lỗi này khiến hàm trở thành None hoặc làm mất giá trị trả về.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`D02.01_bai_tap_da_giai_v25.py`](MA_MAU/D02.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`D02.01_loi_giai.md`](LOI_GIAI/D02.01_loi_giai.md).
5. **Bài mở rộng:** Hãy mở rộng decorator để kiểm tra nhiều tham số và giải thích vai trò của *args/**kwargs và inspect.signature.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/functools.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# D02.02 — functools.wraps và decorator có tham số

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D02 — Decorator và chức năng chéo · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **functools.wraps và decorator có tham số**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

## 2. Khái niệm — Bản chất

`functools.wraps` sao chép metadata thích hợp (`__name__`, `__doc__`, `__wrapped__`) từ hàm gốc sang wrapper, hỗ trợ debug và introspection. Decorator **có tham số** thường có thêm một lớp factory: `factory(config)` trả về decorator, rồi decorator nhận hàm.

## 3. Nguyên lý và cơ chế từng bước

Tại thời điểm định nghĩa hàm: Python tính `nhan_he_so(3)` trước, nhận decorator, rồi áp dụng decorator đó lên `cong`. `@wraps(fn)` giúp introspection thấy metadata gốc.

## 4. Ví dụ tối thiểu có thể chạy

```python
from functools import wraps

def nhan_he_so(he_so):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return he_so * fn(*args, **kwargs)
        return wrapper
    return decorator

@nhan_he_so(3)
def cong(a, b):
    """Cộng hai số."""
    return a + b

assert cong(2, 4) == 18
assert cong.__name__ == 'cong'
assert cong.__wrapped__(2, 4) == 6
print(cong.__doc__)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
Cộng hai số.
```

**Thực hành:** chạy file `07_MA_VI_DU/D02.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không nhầm `@factory` và `@factory(...)`: hàm đầu tiên là decorator trực tiếp còn mẫu thứ hai thường là factory.
- **Trường hợp biên:** `wraps` không thể bảo đảm toàn bộ chữ ký runtime vẫn giống hàm gốc; wrapper có thể thay đổi hành vi và typing.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Phù hợp cho instrumentation, retry policy; cần tài liệu hóa khi decorator đổi kiểu giá trị trả về.

## 7. Bài tập có yêu cầu kiểm chứng

Viết decorator factory `gioi_han(gioi_han_max)` để chặn kết quả lớn hơn giới hạn và bảo toàn tên hàm.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D02.02_loi_giai.md](LOI_GIAI/D02.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **functools.wraps và decorator có tham số** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# D02.03 — Sử dụng decorator đúng mục đích

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D02 — Decorator và chức năng chéo · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Sử dụng decorator đúng mục đích**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

## 2. Khái niệm — Bản chất

Decorator có thể làm hành vi khó lần vết nếu lạm dụng; đánh giá hiệu quả bằng độ lặp mã giảm và độ minh bạch hợp đồng. Decorator cho xác thực cần dựa trên identity và context đáng tin cậy, không chỉ dựa vào tham số do client truyền.

## 3. Nguyên lý và cơ chế từng bước

Với chức năng chéo, so sánh wrapper với gọi một hàm helper tường minh. Chỉ chọn decorator nếu phần chức năng đó thực sự áp dụng lặp lại qua nhiều endpoint.

## 4. Ví dụ tối thiểu có thể chạy

```python
from functools import wraps

def khong_rong(fn):
    @wraps(fn)
    def wrapper(text):
        if not text.strip(): raise ValueError('rỗng')
        return fn(text)
    return wrapper

@khong_rong
def viet_hoa(text): return text.strip().title()
assert viet_hoa('  python  ') == 'Python'
print(viet_hoa('  python  '))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
Python
```

**Thực hành:** chạy file `07_MA_VI_DU/D02.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không biến decorator thành nơi có network I/O/secret lookup khó test mà không có cách injection.
- **Trường hợp biên:** Nếu decorator áp lên async function nhưng wrapper không `await`, nó có thể làm khác mô hình thực thi dự kiến.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Cân nhắc thêm dòng code rõ ràng thay vì decorator khi chỉ dùng đúng một nơi.

## 7. Bài tập có yêu cầu kiểm chứng

Viết một test chứng minh wrapper không nuốt ValueError, rồi mô tả trường hợp dùng helper thường dễ bảo trì hơn decorator.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D02.03_loi_giai.md](LOI_GIAI/D02.03_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Sử dụng decorator đúng mục đích** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: D02.01, D02.02, D02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
