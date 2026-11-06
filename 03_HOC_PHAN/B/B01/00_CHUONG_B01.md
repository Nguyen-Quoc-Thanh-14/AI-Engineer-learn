# Chương B01 — Giá trị, đối tượng và tên

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B01: Giá trị, đối tượng và tên, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Giá trị, kiểu và đối tượng; Quy tắc đặt tên và chú thích.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B01.01 — Giá trị, kiểu và đối tượng](BAI_HOC/B01.01.md)
- [B01.02 — Tên, phép gán và tham chiếu](BAI_HOC/B01.02.md)
- [B01.03 — Quy tắc đặt tên và chú thích](BAI_HOC/B01.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B01.01 — Giá trị, kiểu và đối tượng

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B01 — Giá trị, đối tượng và tên.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Giá trị, kiểu và đối tượng** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Python biểu diễn mọi giá trị sử dụng trong chương trình bằng đối tượng (object). Mỗi đối tượng có danh tính (identity), kiểu (type) và giá trị (value). Kiểu quyết định những thao tác được phép; chẳng hạn đối tượng số nguyên hỗ trợ phép cộng số học, trong khi chuỗi hỗ trợ phép nối. `type(x)` cho biết kiểu runtime, `isinstance(x, T)` kiểm tra tương thích kiểu, bao gồm phân lớp. Người mới thường nhầm rằng chỉ class tự tạo mới là đối tượng; thực tế cả `3`, `True` và `None` đều là đối tượng.

### 3. Cơ chế hoạt động từng bước

Khi biểu thức được đánh giá, Python tạo hoặc tìm đối tượng biểu diễn kết quả. Tên như `gia` được liên kết tới đối tượng đó; tên không phải chiếc hộp chứa các byte giá trị theo mô hình cố định. Không lấy địa chỉ bộ nhớ làm định nghĩa chính thức của `id`.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
gia = 12000
nhan = "Sách"
print(type(gia).__name__)
print(isinstance(gia, int))
print(type(nhan).__name__)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
int
True
str
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng `type(x) is int` để thay cho mọi phép kiểm tra số nguyên: trong Python, `bool` là phân lớp của `int`. Cần xác định rõ quy tắc chấp nhận đầu vào.
- **Tình huống biên:** `isinstance(True, int)` trả True, nhưng mọi bài toán nhận số nguyên không nhất thiết muốn chấp nhận Boolean.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Giá trị là nội dung biểu diễn, kiểu là tập ngữ nghĩa và thao tác; tên là phương tiện tham chiếu, không đồng nghĩa với đối tượng.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm `mo_ta(x)` trả về tên kiểu runtime và chuỗi thể hiện giá trị của x. Kiểm tra với 5, "A" và None.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B01.01_loi_giai.md](LOI_GIAI/B01.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B01.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Giá trị là nội dung biểu diễn, kiểu là tập ngữ nghĩa và thao tác; tên là phương tiện tham chiếu, không đồng nghĩa với đối tượng.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B01](https://docs.python.org/3.15/reference/datamodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B01.02 — Tên, phép gán và tham chiếu

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B01 — Giá trị, đối tượng và tên.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Tên, phép gán và tham chiếu** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Phép gán liên kết một tên với đối tượng; nó không nhất thiết tạo bản sao. Khi hai tên cùng tham chiếu một list, sửa list qua một tên có thể quan sát được qua tên còn lại. Gán lại tên là việc khác với thay đổi nội dung đối tượng. Đây là nền tảng giải thích aliasing, mutable defaults và tham số hàm.

### 3. Cơ chế hoạt động từng bước

Đầu tiên `a` liên kết với list. Lệnh `b = a` tạo thêm tên cùng tham chiếu. `b.append()` sửa đối tượng chung; `b = [9]` sẽ chỉ liên kết lại `b` sang list khác. Dấu `is` so sánh identity, `==` so sánh giá trị.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
a = [1, 2]
b = a
b.append(3)
print(a)
print(a is b)
b = [9]
print(a, b)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[1, 2, 3]
True
[1, 2, 3] [9]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không diễn giải `a = b` mặc định như thao tác sao chép dữ liệu. Tránh kiểm tra identity của literal số nguyên/chuỗi để suy ra quy tắc caching.
- **Tình huống biên:** Với list lồng nhau, `.copy()` chỉ sao chép nông: list con vẫn có thể dùng chung.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Gán lại biến (`x = ...`) khác với biến đổi đối tượng có thể thay đổi (`x.append(...)`).

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo `goc = [2]`, gán `ban_sao = goc.copy()`, thêm 4 vào bản sao. Chứng minh hai list độc lập ở cấp ngoài.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B01.02_loi_giai.md](LOI_GIAI/B01.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B01.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Gán lại biến (`x = ...`) khác với biến đổi đối tượng có thể thay đổi (`x.append(...)`).

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B01](https://docs.python.org/3.15/reference/datamodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B01.03 — Quy tắc đặt tên và chú thích

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B01 — Giá trị, đối tượng và tên.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Quy tắc đặt tên và chú thích** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Tên biến phải tuân theo cú pháp identifier của Python, phân biệt chữ hoa/chữ thường và không trùng từ khóa. Theo PEP 8, tên biến/hàm thường dùng `snake_case`, tên class dùng `CapWords`; đây là quy ước phong cách, không phải cú pháp bắt buộc. Comment `#` giải thích *vì sao* hoặc bối cảnh, không lặp lại một dòng code tự hiển nhiên.

### 3. Cơ chế hoạt động từng bước

Interpreter phân tích các token hợp lệ rồi liên kết tên theo phạm vi. Tên rõ ý nghĩa giúp đọc và bảo trì; tên hợp cú pháp vẫn có thể rất khó hiểu. Dùng `keyword.iskeyword` khi kiểm tra từ khóa hiện hành.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
import keyword
so_luong = 4
thanh_tien = so_luong * 8500
print(keyword.iskeyword("class"))
print(thanh_tien)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
True
34000
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `list = [1]` hợp cú pháp nhưng che khuất hàm built-in `list`; cần tránh các tên trùng built-in.
- **Tình huống biên:** Unicode identifier được hỗ trợ, nhưng tên thuần ASCII có thể thuận tiện hơn khi cộng tác đa môi trường.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Tên hợp lệ thuộc ngữ pháp; tên tốt thuộc thiết kế giao tiếp giữa các lập trình viên.

### 7. Bài tập thực hành

**Yêu cầu chính:** Đổi các tên `a`, `b`, `c` trong phép tính diện tích hình chữ nhật sang tên có nghĩa; thêm comment giải thích đơn vị.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B01.03_loi_giai.md](LOI_GIAI/B01.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B01.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Tên hợp lệ thuộc ngữ pháp; tên tốt thuộc thiết kế giao tiếp giữa các lập trình viên.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B01](https://docs.python.org/3.15/reference/datamodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B01.01, B01.02, B01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
