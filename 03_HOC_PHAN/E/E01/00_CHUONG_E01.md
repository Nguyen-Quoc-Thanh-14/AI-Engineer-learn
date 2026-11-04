# Chương E01 — Class và instance

> **Giai đoạn:** GD3 · **Học phần:** Lập trình hướng đối tượng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương E01: Class và instance, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Định nghĩa class, __init__ và self; Trạng thái đối tượng và vòng đời.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [E01.01 — Định nghĩa class, __init__ và self](BAI_HOC/E01.01.md)
- [E01.02 — Instance/class attribute và method](BAI_HOC/E01.02.md)
- [E01.03 — Trạng thái đối tượng và vòng đời](BAI_HOC/E01.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## E01.01 — Định nghĩa class, __init__ và self

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E01 — Class và instance · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Định nghĩa class, __init__ và self**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Class là đối tượng tạo ra instance; `__init__` khởi tạo trạng thái trên instance đã được tạo. `self` là quy ước cho tham số đại diện instance, không phải từ khóa Python.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class TaiKhoan:
    def __init__(self, so_du): self.so_du=so_du

tk=TaiKhoan(100)
assert tk.so_du==100
print(tk.so_du)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
100
```

**Thực hành:** chạy file `07_MA_VI_DU/E01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** `__init__` phải trả None; không dùng làm constructor trả instance mới.
- **Trường hợp biên:** Hai instance tạo từ cùng class vẫn có trạng thái riêng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Viết lớp `SanPham` giữ tên và giá; tạo hai instance độc lập.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E01.01_loi_giai.md](LOI_GIAI/E01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Định nghĩa class, __init__ và self** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## E01.02 — Instance/class attribute và method

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E01 — Class và instance · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Instance/class attribute và method**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Instance attribute thường nằm trên từng instance; class attribute là thuộc tính trên class và có thể được đọc qua instance nếu chưa bị shadow. Method thường được bind để truyền instance khi truy cập qua đối tượng.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class Gio:
    loai='hop'
    def __init__(self,ten): self.ten=ten
    def xem(self): return self.ten
x=Gio('A'); y=Gio('B')
assert (x.xem(),y.xem(),Gio.loai)==('A','B','hop')
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/E01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `items=[]` ở class body nếu mỗi instance phải có list riêng.
- **Trường hợp biên:** Gán `x.loai` có thể che class attribute mà không đổi `Gio.loai`.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Giải thích vì sao danh sách mutable làm class attribute có thể bị dùng chung, rồi sửa.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E01.02_loi_giai.md](LOI_GIAI/E01.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Instance/class attribute và method** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## E01.03 — Trạng thái đối tượng và vòng đời

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E01 — Class và instance · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Trạng thái đối tượng và vòng đời**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Vòng đời đối tượng phụ thuộc tham chiếu và cơ chế quản lý bộ nhớ của implementation. Không dựa vào thời điểm `__del__` để giải phóng file/socket; dùng `with` hoặc close tường minh.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class X:
    def __init__(self): self.ready=True
x=X()
assert x.ready
print(x.__dict__)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
{'ready': True}
```

**Thực hành:** chạy file `07_MA_VI_DU/E01.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Thời điểm hủy object không được đảm bảo giống nhau ở mọi implementation.
- **Trường hợp biên:** Cyclic references và traceback có thể giữ object sống lâu hơn dự kiến.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Dùng context manager tự viết để giải phóng tài nguyên, không dùng `__del__`.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E01.03_loi_giai.md](LOI_GIAI/E01.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Trạng thái đối tượng và vòng đời** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: E01.01, E01.02, E01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
