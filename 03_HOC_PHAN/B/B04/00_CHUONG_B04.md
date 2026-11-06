# Chương B04 — Biểu thức và toán tử

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B04: Biểu thức và toán tử, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: So sánh, logic và short-circuit; Toán tử membership, identity và assignment expression.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B04.01 — So sánh, logic và short-circuit](BAI_HOC/B04.01.md)
- [B04.02 — Thứ tự ưu tiên và thứ tự đánh giá](BAI_HOC/B04.02.md)
- [B04.03 — Toán tử membership, identity và assignment expression](BAI_HOC/B04.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B04.01 — So sánh, logic và short-circuit

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B04 — Biểu thức và toán tử.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **So sánh, logic và short-circuit** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Các phép `==`, `<`, `>=` tạo kết quả logic theo quy tắc kiểu; `and`, `or`, `not` phối hợp điều kiện. `and` và `or` đánh giá lười: dừng khi kết quả logic đã xác định. Chúng trả về toán hạng tương ứng, không bắt buộc là bool.

### 3. Cơ chế hoạt động từng bước

Kiểm tra điều kiện từ trái sang phải. Ví dụ `x != 0 and 10 / x > 2` an toàn với x=0 vì phần chia không chạy; đảo thứ tự làm thay đổi kết quả/ngoại lệ.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
x = 0
print(x != 0 and 10 / x > 2)
print("" or "không có tên")
print(not [])
```

**Kết quả thực thi trên Python 3.13.5**:

```text
False
không có tên
True
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng `a == 1 or 2` để kiểm tra a có bằng 1 hoặc 2; `or 2` truthy. Dùng `a in (1, 2)`.
- **Tình huống biên:** `float("nan") == float("nan")` là False theo đặc tính NaN.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`and/or` là toán tử logic điều khiển đánh giá; `&/|` là phép bitwise hoặc quá tải theo kiểu.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm xác định một điểm có nằm trong khoảng [0,100] và là int (không nhận bool).

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B04.01_loi_giai.md](LOI_GIAI/B04.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B04.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `and/or` là toán tử logic điều khiển đánh giá; `&/|` là phép bitwise hoặc quá tải theo kiểu.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B04](https://docs.python.org/3.15/reference/expressions.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B04.02 — Thứ tự ưu tiên và thứ tự đánh giá

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B04 — Biểu thức và toán tử.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Thứ tự ưu tiên và thứ tự đánh giá** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Biểu thức Python được phân tích theo ngữ pháp và thứ tự ưu tiên toán tử; đây không hoàn toàn đồng nghĩa thứ tự các hàm được gọi. Dùng ngoặc để làm rõ ý định. Ví dụ lũy thừa `**` kết hợp từ phải sang trái; phép gọi và truy cập thuộc tính có độ ưu tiên cao.

### 3. Cơ chế hoạt động từng bước

Để dự đoán kết quả, xác định nhóm theo precedence rồi xét quy tắc đánh giá toán hạng. Không dựa vào “chạy thử vài lần” để suy ra ngữ nghĩa tổng quát.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
14
20
512
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `-2 ** 2` cho -4 vì được hiểu là `-(2 ** 2)`; đây là bẫy phổ biến.
- **Tình huống biên:** Chia cho 0 trong nhánh không được short-circuit sẽ gây ngoại lệ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Độ ưu tiên (precedence) khác với thứ tự đánh giá; ngoặc là công cụ thể hiện ý định.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết biểu thức tính diện tích hình vành khăn theo công thức pi × (R² - r²); dùng ngoặc rõ ràng.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B04.02_loi_giai.md](LOI_GIAI/B04.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B04.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Độ ưu tiên (precedence) khác với thứ tự đánh giá; ngoặc là công cụ thể hiện ý định.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B04](https://docs.python.org/3.15/reference/expressions.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B04.03 — Toán tử membership, identity và assignment expression

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B04 — Biểu thức và toán tử.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Toán tử membership, identity và assignment expression** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`in` kiểm tra thành viên, ý nghĩa phụ thuộc container; đối với dict nó kiểm tra khóa. `is` kiểm tra danh tính đối tượng, không phải giá trị. `:=` (assignment expression) đặt tên cho kết quả biểu thức tại vị trí phù hợp, có thể giảm tính toán lặp nhưng không nên lạm dụng.

### 3. Cơ chế hoạt động từng bước

Bộ kiểm tra thành viên sẽ dùng giao thức thích hợp. Cú pháp walrus có các hạn chế ngữ pháp; trong bài nền tảng, ưu tiên phép gán bình thường khi cách viết đó dễ đọc hơn.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
d = {"a": 1}
print("a" in d)
print(1 in d)
a = [1]
b = [1]
print(a == b, a is b)
if (n := len(d)) > 0:
    print(n)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
True
False
True False
1
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng `is` thay cho `==` với số và chuỗi. Chỉ dùng `is None` để kiểm tra None.
- **Tình huống biên:** Dict có khóa "x" giá trị None vẫn chứa khóa "x".
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Equality dựa trên `__eq__`; identity là đồng nhất đối tượng.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm cho biết một tên có tồn tại dưới dạng khóa trong dict mà không nhầm với giá trị.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B04.03_loi_giai.md](LOI_GIAI/B04.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B04.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Equality dựa trên `__eq__`; identity là đồng nhất đối tượng.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B04](https://docs.python.org/3.15/reference/expressions.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B04.01, B04.02, B04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
