# Chương D04 — Hệ kiểu tĩnh

> **Giai đoạn:** GD2 · **Học phần:** Hàm và mô hình lập trình nâng cao  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương D04: Hệ kiểu tĩnh, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Annotation và type hint; Protocol, duck typing và static type checker.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [D04.01 — Annotation và type hint](BAI_HOC/D04.01.md)
- [D04.02 — Union, generic và TypedDict](BAI_HOC/D04.02.md)
- [D04.03 — Protocol, duck typing và static type checker](BAI_HOC/D04.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)
- [R10: Python typing specification](https://typing.python.org/en/latest/spec/)
- [R19: mypy Documentation](https://mypy.readthedocs.io/en/stable/)

---

## D04.01 — Annotation và type hint

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D04 — Hệ kiểu tĩnh · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Annotation và type hint**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Type annotation** mô tả ý định về kiểu và phục vụ công cụ kiểm tra tĩnh, editor, tài liệu. Python runtime mặc định không ép kiểu chỉ vì có annotation. `typing.get_type_hints()` có thể truy vấn annotation với cách xử lý phụ thuộc phiên bản.

### 3. Nguyên lý và cơ chế từng bước

Hàm nhận `int` rồi cộng một. `-> int` không tự làm `isinstance` hay báo lỗi trước khi thực hiện phép cộng; hành vi phụ thuộc thân hàm.

### 4. Ví dụ tối thiểu có thể chạy

```python
def cong_mot(x: int) -> int:
    return x + 1

assert cong_mot(2)==3
assert cong_mot.__annotations__['x'] is int
print(cong_mot(2))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
3
```

**Thực hành:** chạy file `07_MA_VI_DU/D04.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Type checker tĩnh không chứng minh dữ liệu JSON mạng đúng hợp đồng; cần kiểm tra runtime ở trust boundary.
- **Trường hợp biên:** `bool` là subclass của `int`, nên yêu cầu chấp nhận số mà loại bool cần quy tắc validation riêng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn annotations để giảm nhầm API và hỗ trợ CI type check, không dùng thay test hay validation.

### 7. Bài tập có yêu cầu kiểm chứng

Viết `dien_tich(hinh_vuong: float) -> float`, thêm validation số âm và nêu giới hạn của annotation.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D04.01_loi_giai.md](LOI_GIAI/D04.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Annotation và type hint** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## D04.02 — Union, generic và TypedDict

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D04 — Hệ kiểu tĩnh · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Union, generic và TypedDict**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Union biểu diễn nhiều kiểu thay thế (`str | None`); Generic cho biết quan hệ giữa kiểu tham số và kiểu kết quả; TypedDict mô tả các key của object kiểu dictionary trong hệ kiểu tĩnh. Các cấu trúc này không tự đảm bảo schema runtime.

### 3. Nguyên lý và cơ chế từng bước

`first` trả về phần tử cùng kiểu với danh sách input nếu không rỗng; kiểu tổng quát nên làm rõ tiền điều kiện. `None` yêu cầu được xử lý độc lập.

### 4. Ví dụ tối thiểu có thể chạy

```python
from typing import TypeVar
T = TypeVar('T')
def first(items: list[T]) -> T | None:
    return items[0] if items else None
assert first(['a','b'])=='a'
assert first([]) is None
print(first([10,20]))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
10
```

**Thực hành:** chạy file `07_MA_VI_DU/D04.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng type hint để kết luận runtime sẽ ném TypeError khi nhận dict thiếu key.
- **Trường hợp biên:** TypeVar cấp kiểu giúp bắt lỗi tĩnh nhưng không ngăn truy cập `items[0]` với list rỗng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng TypedDict cho dữ liệu dict truyền giữa các lớp có kiểm định runtime riêng ở biên hệ thống.

### 7. Bài tập có yêu cầu kiểm chứng

Mô tả `TypedDict` cho dữ liệu người dùng gồm id và tên; viết validation runtime độc lập.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D04.02_loi_giai.md](LOI_GIAI/D04.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Union, generic và TypedDict** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## D04.03 — Protocol, duck typing và static type checker

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D04 — Hệ kiểu tĩnh · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Protocol, duck typing và static type checker**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Protocol** mô tả kiểu theo tập phương thức/thuộc tính cần có (structural typing). **Duck typing** là thực hành kiểm tra hành vi thay vì tên class: đối tượng hoạt động nếu nó hỗ trợ phương thức mong đợi. Type checker có thể kiểm Protocol ở thời gian phát triển.

### 3. Nguyên lý và cơ chế từng bước

Chức năng phụ thuộc giao diện `.write(text)` hơn là một class cụ thể. Test doubles dễ cài đặt nhờ cùng giao diện.

### 4. Ví dụ tối thiểu có thể chạy

```python
from typing import Protocol
class Writer(Protocol):
    def write(self, text: str) -> None: ...

class Buffer:
    def __init__(self): self.messages=[]
    def write(self, text: str) -> None: self.messages.append(text)

def gui(w: Writer, text: str) -> None: w.write(text)
b = Buffer(); gui(b,'xin chao')
assert b.messages == ['xin chao']
print(b.messages)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
['xin chao']
```

**Thực hành:** chạy file `07_MA_VI_DU/D04.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** `@runtime_checkable` nếu dùng chỉ kiểm hạn chế về sự hiện diện thành phần, không xác thực đầy đủ chữ ký hoặc điều kiện nghiệp vụ.
- **Trường hợp biên:** Một đối tượng thỏa Protocol tĩnh vẫn có thể báo lỗi logic, I/O hoặc sai hợp đồng khi thực thi.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Protocol hữu ích để tách lớp khỏi cơ chế lưu trữ; không cần tạo interface cho mỗi hàm đơn giản.

### 7. Bài tập có yêu cầu kiểm chứng

Viết Protocol cho đối tượng có `save(text) -> None` và class InMemorySaver; test bằng assert.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D04.03_loi_giai.md](LOI_GIAI/D04.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Protocol, duck typing và static type checker** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

Đã cập nhật file bài lẻ: D04.01, D04.02, D04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
