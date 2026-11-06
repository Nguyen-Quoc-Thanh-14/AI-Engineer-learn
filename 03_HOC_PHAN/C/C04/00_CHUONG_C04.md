# Chương C04 — Thao tác sequence nâng cao

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C04: Thao tác sequence nâng cao, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Indexing, slicing và unpacking; List, set và dict comprehension.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C04.01 — Indexing, slicing và unpacking](BAI_HOC/C04.01.md)
- [C04.02 — enumerate, zip và sorted](BAI_HOC/C04.02.md)
- [C04.03 — List, set và dict comprehension](BAI_HOC/C04.03.md)

## Tiên quyết

B

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## C04.01 — Indexing, slicing và unpacking

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C04 — Thao tác sequence nâng cao.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Indexing, slicing và unpacking** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Indexing, slicing và unpacking là cú pháp giúp tách và cấu trúc dữ liệu. `a[start:stop:step]` sử dụng mốc loại trừ stop, step có thể âm. Unpacking có thể phân phần tử vào nhiều tên, `*rest` thu phần còn lại thành list.

### 3. Cơ chế hoạt động từng bước

Ở phép gán `x, y = pair`, số phần tử phải khớp nếu không có starred target. Slicing không tạo lỗi IndexError khi biên nằm ngoài chiều dài đối với sequence thông dụng.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
items = [0, 1, 2, 3, 4]
print(items[::-1])
first, *middle, last = items
print(first, middle, last)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[4, 3, 2, 1, 0]
0 [1, 2, 3] 4
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `a[::0]` phát sinh ValueError vì bước không thể bằng 0.
- **Tình huống biên:** Unpacking `a,b = [1]` làm phát sinh ValueError do thiếu phần tử.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Slicing là tạo vùng sequence, unpacking là gán nhiều tên theo cấu trúc.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm đổi chỗ phần tử đầu và cuối của list đầu vào mà không sửa nguồn.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C04.01_loi_giai.md](LOI_GIAI/C04.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C04.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Slicing là tạo vùng sequence, unpacking là gán nhiều tên theo cấu trúc.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C04](https://docs.python.org/3.15/tutorial/datastructures.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C04.02 — enumerate, zip và sorted

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C04 — Thao tác sequence nâng cao.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **enumerate, zip và sorted** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

`enumerate` ghép chỉ số và giá trị khi duyệt; `zip` ghép các iterable theo thứ tự, mặc định dừng khi iterable ngắn nhất cạn; `zip(..., strict=True)` có thể kiểm tra độ dài không khớp. `sorted` trả list mới, trong khi `list.sort` sửa list tại chỗ.

### 3. Cơ chế hoạt động từng bước

Khi cần sắp xếp phức tạp, truyền `key` để tạo tiêu chí; Python sort ổn định, các phần tử có cùng key giữ thứ tự tương đối.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
ten = ["An", "Bình", "Chi"]
diem = [9, 7, 9]
print(list(enumerate(ten, start=1)))
print(sorted(zip(ten, diem), key=lambda x: (-x[1], x[0])))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[(1, 'An'), (2, 'Bình'), (3, 'Chi')]
[('An', 9), ('Chi', 9), ('Bình', 7)]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `sorted` không sửa list ban đầu; `list.sort()` trả None, không phải list đã sắp.
- **Tình huống biên:** `zip` mặc định bỏ phần dư mà không báo lỗi; dùng strict khi ràng buộc kích thước.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`enumerate` trả (index, value), `zip` trả tuple các phần tử từ nhiều iterable.

### 7. Bài tập thực hành

**Yêu cầu chính:** Ghép hai danh sách tên/điểm theo index thành dict; báo lỗi nếu độ dài khác nhau.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C04.02_loi_giai.md](LOI_GIAI/C04.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C04.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `enumerate` trả (index, value), `zip` trả tuple các phần tử từ nhiều iterable.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C04](https://docs.python.org/3.15/tutorial/datastructures.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C04.03 — List, set và dict comprehension

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C04 — Thao tác sequence nâng cao.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **List, set và dict comprehension** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Comprehension tạo list, set, dict từ iterable bằng cú pháp biểu thức kết hợp for và if. Không nên dùng comprehension chỉ để tạo side effect (ví dụ gọi print) vì dễ giảm độ dễ đọc. Generator expression `(...)` không lập tức tạo toàn bộ list.

### 3. Cơ chế hoạt động từng bước

Quy trình: duyệt các phần tử, áp dụng bộ lọc if, tính biểu thức, thêm kết quả vào container. Khi dùng nhiều for, thứ tự tương ứng với vòng lặp lồng nhau.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
data = [1,2,3,4]
print([x*x for x in data if x%2 == 0])
print({x: x*x for x in data if x<3})
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[4, 16]
{1: 1, 2: 4}
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Với phần tử lớn hoặc pipeline dài, comprehension tạo list có thể tốn bộ nhớ; cân nhắc generator.
- **Tình huống biên:** Các khóa trùng trong dict comprehension sẽ ghi đè giá trị cũ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Comprehension tạo dữ liệu ngay; generator expression tạo một iterator lười.

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo dict đếm chiều dài từng tên trong list, bỏ tên rỗng.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C04.03_loi_giai.md](LOI_GIAI/C04.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C04.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Comprehension tạo dữ liệu ngay; generator expression tạo một iterator lười.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C04](https://docs.python.org/3.15/tutorial/datastructures.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C04.01, C04.02, C04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
