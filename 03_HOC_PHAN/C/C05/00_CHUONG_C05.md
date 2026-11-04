# Chương C05 — Lặp và xử lý lười

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C05: Lặp và xử lý lười, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Iterable và iterator; Duyệt một lần, bộ nhớ và lỗi cạn iterator.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C05.01 — Iterable và iterator](BAI_HOC/C05.01.md)
- [C05.02 — Generator, yield và generator expression](BAI_HOC/C05.02.md)
- [C05.03 — Duyệt một lần, bộ nhớ và lỗi cạn iterator](BAI_HOC/C05.03.md)

## Tiên quyết

B

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## C05.01 — Iterable và iterator

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C05 — Lặp và xử lý lười.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Iterable và iterator** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Iterable có khả năng cung cấp iterator; iterator có `__next__()` trả từng phần tử và báo hết qua StopIteration. `for` dùng iterator protocol, vì vậy có thể duyệt file, generator, list theo cách thống nhất. Iterable không nhất thiết có indexing.

### 3. Cơ chế hoạt động từng bước

`iter(items)` lấy iterator; mỗi `next(it)` tiến trạng thái. Iterator có thể là đối tượng một lượt; gọi iter() lại với list cho lượt mới, với generator đã cạn thường không hồi phục.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
items = ["a", "b"]
it = iter(items)
print(next(it))
print(next(it))
print(list(items))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
a
b
['a', 'b']
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không gọi `next` trên list trực tiếp vì list là iterable nhưng không phải iterator (`next(iter(list))`).
- **Tình huống biên:** `None` có thể là phần tử đầu hợp lệ; cần sentinel khác nếu phải phân biệt với rỗng.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Iterable cung cấp iterator; iterator giữ trạng thái tiến từng phần tử.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm lấy phần tử đầu của iterable, trả None nếu rỗng.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C05.01_loi_giai.md](LOI_GIAI/C05.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C05.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Iterable cung cấp iterator; iterator giữ trạng thái tiến từng phần tử.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C05](https://docs.python.org/3.15/library/stdtypes.html#iterator-types)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C05.02 — Generator, yield và generator expression

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C05 — Lặp và xử lý lười.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Generator, yield và generator expression** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Generator function sử dụng `yield` để tạm dừng, giữ trạng thái cục bộ và tiếp tục khi iterator yêu cầu giá trị tiếp theo. Generator expression là cú pháp ngắn tạo iterator lười. Cả hai giảm nhu cầu giữ toàn bộ kết quả trong bộ nhớ nếu tiêu thụ theo luồng.

### 3. Cơ chế hoạt động từng bước

Gọi generator function trả generator object, không thực thi toàn bộ thân; `next`/`for` mới thúc đẩy thực thi đến `yield` tiếp theo.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def binh_phuong(n):
    for x in range(n):
        yield x*x
g = binh_phuong(4)
print(next(g))
print(list(g))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
0
[1, 4, 9]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Generator thường chỉ duyệt một lần; sau khi cạn cần tạo generator mới để lặp lại.
- **Tình huống biên:** Có thể phát sinh lỗi giữa quá trình tiêu thụ generator chứ không ngay lúc tạo.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`yield` trao từng giá trị; `return` kết thúc generator, không tương đương với `yield`.

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo generator phát sinh các số chẵn từ 0 đến n, kể cả n.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C05.02_loi_giai.md](LOI_GIAI/C05.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C05.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `yield` trao từng giá trị; `return` kết thúc generator, không tương đương với `yield`.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C05](https://docs.python.org/3.15/library/stdtypes.html#iterator-types)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C05.03 — Duyệt một lần, bộ nhớ và lỗi cạn iterator

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C05 — Lặp và xử lý lười.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Duyệt một lần, bộ nhớ và lỗi cạn iterator** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Iterator một lượt như generator, luồng đọc file hoặc zip iterator có thể cạn. Dùng `list(it)` để quan sát sẽ tiêu thụ dữ liệu; đo length bằng cách duyệt có thể gây mất dữ liệu cho bước sau. Thiết kế API nên ghi rõ đầu vào dùng được nhiều lần hay không.

### 3. Cơ chế hoạt động từng bước

Với generator, sau mỗi lần next, cursor tiến lên; khi hết sẽ phát sinh StopIteration. Nếu cần lặp lại, tái tạo generator bằng hàm factory hoặc lưu kết quả với chi phí bộ nhớ.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
g = (x for x in [1,2])
print(list(g))
print(list(g))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[1, 2]
[]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không gọi `len(generator)` hay duyệt lại mong dữ liệu tự xuất hiện.
- **Tình huống biên:** Iterator có side effect (I/O, network) nên tránh tiêu thụ thử trong validation.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

List có thể lặp lại nhiều lần; generator thường duyệt một lượt.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm tạo generator từ danh sách và chứng minh hai lời gọi factory độc lập.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C05.03_loi_giai.md](LOI_GIAI/C05.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C05.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. List có thể lặp lại nhiều lần; generator thường duyệt một lượt.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C05](https://docs.python.org/3.15/library/stdtypes.html#iterator-types)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C05.01, C05.02, C05.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
