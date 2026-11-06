# Chương C02 — Mapping và tập hợp

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C02: Mapping và tập hợp, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: dict và kỹ thuật tra cứu; Hashable và lỗi KeyError.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C02.01 — dict và kỹ thuật tra cứu](BAI_HOC/C02.01.md)
- [C02.02 — set, frozenset và phép tập hợp](BAI_HOC/C02.02.md)
- [C02.03 — Hashable và lỗi KeyError](BAI_HOC/C02.03.md)

## Tiên quyết

B

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## C02.01 — dict và kỹ thuật tra cứu

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C02 — Mapping và tập hợp.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **dict và kỹ thuật tra cứu** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Dictionary (`dict`) ánh xạ khóa hashable tới giá trị; giữ thứ tự chèn theo chuẩn ngôn ngữ từ Python 3.7. Truy cập bằng `d[k]` phát sinh KeyError khi thiếu; `get` trả giá trị mặc định và không phân biệt được thiếu với khóa có None nếu dùng mặc định None.

### 3. Cơ chế hoạt động từng bước

Thêm hoặc gán khóa bằng `d[k] = v`; duyệt trực tiếp dict cho ra khóa; `items()` cho cặp khóa/giá trị. Tra cứu có kỳ vọng O(1) trong điều kiện thông thường, không bảo đảm cho mọi tình huống.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
d = {"ao": 2, "quan": 3}
print(d["ao"])
print(d.get("giay", 0))
print(list(d.items()))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
2
0
[('ao', 2), ('quan', 3)]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Duyệt `for v in d` cho ra các khóa chứ không phải các giá trị.
- **Tình huống biên:** Giá trị None có thể là một giá trị hợp lệ của khóa hiện có.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Dict dùng khóa; list dùng vị trí số nguyên để truy cập.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm cộng lượng hàng khi nhập một mục; không sửa dict gốc.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C02.01_loi_giai.md](LOI_GIAI/C02.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C02.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Dict dùng khóa; list dùng vị trí số nguyên để truy cập.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C02](https://docs.python.org/3.15/library/stdtypes.html#mapping-types-dict)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C02.02 — set, frozenset và phép tập hợp

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C02 — Mapping và tập hợp.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **set, frozenset và phép tập hợp** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

`set` chứa các phần tử hashable duy nhất, không cung cấp indexing. `frozenset` là tập bất biến, có thể dùng làm phần tử của set khác nếu các thành viên đều hashable. Các phép toán tập hợp giúp diễn đạt giao, hợp và hiệu rõ ràng.

### 3. Cơ chế hoạt động từng bước

Set dựa trên hashing; thứ tự lặp không phải giao kèo thứ tự. Đối với kết quả cần thứ tự, dùng sorted với các phần tử có thể so sánh được.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
a = {1, 2, 3}
b = {3, 4}
print(sorted(a | b))
print(sorted(a & b))
print(sorted(a - b))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[1, 2, 3, 4]
[3]
[1, 2]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Đừng giả định `list(set(items))` giữ nguyên thứ tự hay luôn cùng thứ tự trên môi trường khác nhau.
- **Tình huống biên:** `{}` tạo dict rỗng; tạo set rỗng bằng `set()`.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`set` dùng membership và phép tập hợp; `dict` ánh xạ khóa thành giá trị.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm trả tên môn học có trong hai danh sách học kỳ, sắp theo bảng chữ cái.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C02.02_loi_giai.md](LOI_GIAI/C02.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C02.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `set` dùng membership và phép tập hợp; `dict` ánh xạ khóa thành giá trị.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C02](https://docs.python.org/3.15/library/stdtypes.html#mapping-types-dict)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C02.03 — Hashable và lỗi KeyError

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C02 — Mapping và tập hợp.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Hashable và lỗi KeyError** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Hashable nghĩa là đối tượng có giá trị hash ổn định theo vòng đời và các đối tượng bằng nhau phải có cùng hash. Đây là điều kiện để dùng làm khóa dict hoặc phần tử set. Kiểu bất biến thường dễ hashable nhưng không phải mọi đối tượng bất biến đều hash được.

### 3. Cơ chế hoạt động từng bước

Dict sử dụng hash để tìm bucket rồi so sánh equality khi cần; KeyError khác TypeError: KeyError do thiếu khóa, TypeError có thể do khóa không hashable.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
d = {(1, 2): "điểm"}
print(d[(1, 2)])
try:
    d[[1, 2]] = "sai"
except TypeError:
    print("unhashable")
```

**Kết quả thực thi trên Python 3.13.5**:

```text
điểm
unhashable
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng list làm dict key; dùng tuple các phần tử hashable, hoặc chuyển kiểu có chủ đích.
- **Tình huống biên:** Tuple chứa list là unhashable do phần tử bên trong.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Hashable khác immutable: một instance tùy biến có thể bất biến logic nhưng cấu hình `__hash__` không hợp lệ.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm kiểm tra một khóa có tồn tại và trả giá trị hoặc chuỗi "thiếu".

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C02.03_loi_giai.md](LOI_GIAI/C02.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C02.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Hashable khác immutable: một instance tùy biến có thể bất biến logic nhưng cấu hình `__hash__` không hợp lệ.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C02](https://docs.python.org/3.15/library/stdtypes.html#mapping-types-dict)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C02.01, C02.02, C02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
