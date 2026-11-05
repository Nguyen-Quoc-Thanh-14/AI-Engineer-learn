# Chương C01 — Sequence nền tảng

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C01: Sequence nền tảng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: list, tuple và range; So sánh sequence và lựa chọn loại phù hợp.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C01.01 — list, tuple và range](BAI_HOC/C01.01.md)
- [C01.02 — Truy cập, cập nhật và duyệt](BAI_HOC/C01.02.md)
- [C01.03 — So sánh sequence và lựa chọn loại phù hợp](BAI_HOC/C01.03.md)

## Tiên quyết

B

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## C01.01 — list, tuple và range

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C01 — Sequence nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **list, tuple và range** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

`list` là sequence có thể thay đổi; `tuple` là sequence bất biến ở cấp container; `range` biểu diễn chuỗi số nguyên lười và có tính toán chiều dài, indexing. Cả ba hỗ trợ duyệt, phép `in` và nhiều thao tác sequence, nhưng mục đích khác nhau. Tuple chứa list vẫn có thể quan sát thay đổi trong list con.

### 3. Cơ chế hoạt động từng bước

Tạo list bằng dấu ngoặc vuông, tuple bằng dấu phẩy hoặc `tuple()`, range theo start/stop/step. Lựa chọn theo nhu cầu cập nhật và quy tắc dữ liệu, không theo số lượng dấu ngoặc.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
a = [1, 2]
b = (1, 2)
c = range(1, 5, 2)
print(a, b, list(c))
a.append(3)
print(a)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[1, 2] (1, 2) [1, 3]
[1, 2, 3]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `(4)` là int chứ không phải tuple một phần tử; phải dùng `(4,)`.
- **Tình huống biên:** Với ít hơn ba phần tử, lời giải trên phát sinh StopIteration; hợp đồng đầu vào phải ghi rõ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Tuple bất biến ở cấp tham chiếu phần tử, không nhất thiết mọi đối tượng bên trong bất biến.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm trả tuple ba giá trị đầu tiên từ iterable có ít nhất ba phần tử.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C01.01_loi_giai.md](LOI_GIAI/C01.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C01.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Tuple bất biến ở cấp tham chiếu phần tử, không nhất thiết mọi đối tượng bên trong bất biến.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C01](https://docs.python.org/3.15/library/stdtypes.html#sequence-types-list-tuple-range)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C01.02 — Truy cập, cập nhật và duyệt

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C01 — Sequence nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Truy cập, cập nhật và duyệt** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Indexing truy cập một phần tử, slicing tạo sequence con theo quy tắc. List có thể sửa qua index, `append`, `extend`, `pop`; tuple không cho gán phần tử. Khi duyệt cần tránh sửa kích thước container nếu hành vi duyệt không rõ.

### 3. Cơ chế hoạt động từng bước

Python chuyển index âm thành vị trí từ cuối, rồi kiểm tra hợp lệ. Slicing giới hạn ngoài biên một cách an toàn đối với nhiều sequence chuẩn.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
items = ["a", "b", "c"]
print(items[-1])
items[1] = "B"
print(items[:2])
print(items)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
c
['a', 'B']
['a', 'B', 'c']
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `append([1,2])` thêm một list; `extend([1,2])` thêm từng phần tử. Dễ gây lỗi dữ liệu lồng nhau.
- **Tình huống biên:** List rỗng không có phần tử cuối; cần kiểm tra trước khi cập nhật.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Indexing một phần tử có thể IndexError; slicing hợp lệ dù phạm vi trống.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm thay phần tử cuối thành "done" trên một bản sao; không sửa input.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C01.02_loi_giai.md](LOI_GIAI/C01.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C01.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Indexing một phần tử có thể IndexError; slicing hợp lệ dù phạm vi trống.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C01](https://docs.python.org/3.15/library/stdtypes.html#sequence-types-list-tuple-range)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C01.03 — So sánh sequence và lựa chọn loại phù hợp

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C01 — Sequence nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **So sánh sequence và lựa chọn loại phù hợp** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Chọn loại sequence theo ngữ nghĩa: list cho danh sách sẽ thay đổi, tuple cho một bản ghi cấu trúc cố định, range cho miền số nguyên tuần tự không cần lưu toàn bộ. `str` cũng là sequence nhưng dành cho văn bản, không nên dùng làm danh sách đối tượng.

### 3. Cơ chế hoạt động từng bước

Xét các thao tác cần thiết (thêm, cập nhật, tra cứu, đếm, lặp lại), xác định kích thước đầu vào và yêu cầu bất biến trước khi quyết định.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
toa_do = (10, 20)
lich = ["T2", "T3"]
so_le = range(1, 10, 2)
print(toa_do[0])
print(len(so_le))
print(5 in so_le)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
10
5
True
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Tuple không tự động đảm bảo hashable; tuple chứa list sẽ không hash được.
- **Tình huống biên:** `range` không chứa số thực; cần tạo số thực bằng công thức nếu cần bước phân số.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

List/tuple đều duyệt theo thứ tự; set không giữ ý nghĩa vị trí như sequence.

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo hàm nhận hai điểm `(x,y)` và trả tuple hiệu tọa độ.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C01.03_loi_giai.md](LOI_GIAI/C01.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C01.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. List/tuple đều duyệt theo thứ tự; set không giữ ý nghĩa vị trí như sequence.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C01](https://docs.python.org/3.15/library/stdtypes.html#sequence-types-list-tuple-range)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C01.01, C01.02, C01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
