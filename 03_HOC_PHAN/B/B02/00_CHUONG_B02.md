# Chương B02 — Số, Boolean và None

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B02: Số, Boolean và None, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: int, float và các phép toán; Sai số số thực và chuyển đổi kiểu.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B02.01 — int, float và các phép toán](BAI_HOC/B02.01.md)
- [B02.02 — bool, None và truthiness](BAI_HOC/B02.02.md)
- [B02.03 — Sai số số thực và chuyển đổi kiểu](BAI_HOC/B02.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B02.01 — int, float và các phép toán

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B02 — Số, Boolean và None.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **int, float và các phép toán** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`int` lưu số nguyên chính xác với độ lớn giới hạn chủ yếu bởi tài nguyên; `float` dùng biểu diễn dấu phẩy động nhị phân, có sai số. `/` là phép chia tạo thương dạng số thực; `//` làm tròn xuống theo âm vô cực, không chỉ cắt phần thập phân. `%` liên quan tới phép chia lấy phần dư, `**` là lũy thừa.

### 3. Cơ chế hoạt động từng bước

Biểu thức số học được đánh giá theo quy tắc ưu tiên. Với `a // b` và `a % b` (b khác 0), có hệ thức `a == (a // b) * b + (a % b)`. So sánh với trường hợp âm để tránh hiểu sai.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
print(7 / 2)
print(7 // 2)
print(-7 // 2)
print(-7 % 2)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
3.5
3
-4
1
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng float để biểu diễn chính xác tiền tệ có yêu cầu làm tròn chặt chẽ; ưu tiên số nguyên đơn vị nhỏ nhất hoặc `Decimal` với quy tắc nghiệp vụ rõ.
- **Tình huống biên:** Phép chia cho 0 gây `ZeroDivisionError`; giá trị `float("nan")` có quy tắc so sánh đặc biệt.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`/` không tương đương `//`; `//` của số âm có thể khác kết quả của `int(a / b)`.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm trả về số hộp đầy và số vật còn lại khi chia n vật thành hộp chứa k vật; k phải dương.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B02.01_loi_giai.md](LOI_GIAI/B02.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B02.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `/` không tương đương `//`; `//` của số âm có thể khác kết quả của `int(a / b)`.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B02](https://docs.python.org/3.15/library/stdtypes.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B02.02 — bool, None và truthiness

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B02 — Số, Boolean và None.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **bool, None và truthiness** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`bool` có hai đối tượng `True`, `False`. Ngữ cảnh Boolean như `if x:` gọi quy tắc truth value testing: nhiều đối tượng rỗng (`""`, `[]`, `{}`) là false, số 0 là false; `None` cũng false. Tuy vậy *false* không đồng nghĩa *không tồn tại*: danh sách rỗng có thể là một giá trị hợp lệ.

### 3. Cơ chế hoạt động từng bước

`if x:` kiểm tra truthiness, còn `x is None` kiểm tra đúng sentinel thiếu giá trị. Toán tử `and` và `or` có thể trả về chính toán hạng thay vì một `bool` mới.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
print(bool([]))
print(bool([0]))
print(None is None)
print("" or "mặc định")
```

**Kết quả thực thi trên Python 3.13.5**:

```text
False
True
True
mặc định
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Đừng dùng `if not so_luong:` khi muốn chỉ phát hiện `None`: số lượng 0 cũng sẽ bị xem là thiếu.
- **Tình huống biên:** Một object có `__bool__` hoặc `__len__` tùy biến có thể có quy tắc truthiness riêng.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`None` thường biểu diễn không có giá trị; `False` là một giá trị logic có nghĩa.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận số lượng hoặc None; trả 0 nếu là None nhưng giữ nguyên 0 và các số hợp lệ.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B02.02_loi_giai.md](LOI_GIAI/B02.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B02.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `None` thường biểu diễn không có giá trị; `False` là một giá trị logic có nghĩa.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B02](https://docs.python.org/3.15/library/stdtypes.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B02.03 — Sai số số thực và chuyển đổi kiểu

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B02 — Số, Boolean và None.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Sai số số thực và chuyển đổi kiểu** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`float` theo IEEE 754 nhị phân thường không biểu diễn chính xác các phân số thập phân như 0.1. Lỗi là đặc tính biểu diễn, không tự động có nghĩa Python cộng sai. `int()` đối với float hữu hạn sẽ loại phần thập phân theo hướng về 0; `round()` có chính sách làm tròn cần hiểu và vẫn chịu sai số biểu diễn.

### 3. Cơ chế hoạt động từng bước

Khi chuyển kiểu, cần tách kiểm tra đầu vào, chuyển đổi và chính sách làm tròn. `math.isclose` so sánh xấp xỉ với `rel_tol` và `abs_tol`; chọn tolerance theo miền ứng dụng.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
import math
print(0.1 + 0.2 == 0.3)
print(math.isclose(0.1 + 0.2, 0.3))
print(int(-2.9))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
False
True
-2
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng so sánh bằng tuyệt đối giữa kết quả float khi bài toán yêu cầu xấp xỉ; không chọn tolerance tùy ý mà không hiểu đơn vị.
- **Tình huống biên:** `int("3.2")` phát sinh ValueError; `float("nan")` không phải một số hữu hạn.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`float` phù hợp mô phỏng đo lường; `decimal.Decimal` phù hợp các phép tính thập phân cần kiểm soát.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết kiểm tra tổng ba phần bằng 1.0 với ngưỡng tuyệt đối 1e-9.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B02.03_loi_giai.md](LOI_GIAI/B02.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B02.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `float` phù hợp mô phỏng đo lường; `decimal.Decimal` phù hợp các phép tính thập phân cần kiểm soát.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B02](https://docs.python.org/3.15/library/stdtypes.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B02.01, B02.02, B02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
