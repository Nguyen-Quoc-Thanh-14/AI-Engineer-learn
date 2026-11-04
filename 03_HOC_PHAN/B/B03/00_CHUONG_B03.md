# Chương B03 — Chuỗi và nhập xuất

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B03: Chuỗi và nhập xuất, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: str, Unicode cơ bản; input, print và f-string.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B03.01 — str, Unicode cơ bản](BAI_HOC/B03.01.md)
- [B03.02 — Truy cập ký tự và xử lý chuỗi](BAI_HOC/B03.02.md)
- [B03.03 — input, print và f-string](BAI_HOC/B03.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B03.01 — str, Unicode cơ bản

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B03 — Chuỗi và nhập xuất.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **str, Unicode cơ bản** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`str` là một chuỗi bất biến gồm các điểm mã Unicode (Unicode code points), không tương đương mảng byte và không nhất thiết một code point là một ký tự nhìn thấy trên màn hình. Mã hóa UTF-8 chuyển văn bản sang bytes. Chọn encoding rõ ràng khi trao đổi tệp với hệ thống ngoài.

### 3. Cơ chế hoạt động từng bước

`len(s)` đếm số code point trong Python string, `len(s.encode("utf-8"))` đếm byte. Hai chuỗi nhìn giống nhau có thể khác biểu diễn do ký tự kết hợp; chuẩn hóa Unicode được cung cấp bởi `unicodedata`.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
s = "cà phê"
print(len(s))
print(len(s.encode("utf-8")))
print(s.upper())
```

**Kết quả thực thi trên Python 3.13.5**:

```text
6
8
CÀ PHÊ
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không cắt bytes UTF-8 theo chỉ số tùy ý rồi giải mã: có thể cắt giữa một mã ký tự. Với văn bản người dùng, cần tính tới grapheme cluster.
- **Tình huống biên:** Unicode combining marks có thể khiến số code point khác số ký tự người đọc cảm nhận.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`str` là văn bản; `bytes` là dữ liệu nhị phân đã mã hóa.

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo hàm `so_byte_utf8(text)` đếm số byte khi lưu chuỗi theo UTF-8; kiểm tra chữ Việt.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B03.01_loi_giai.md](LOI_GIAI/B03.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B03.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `str` là văn bản; `bytes` là dữ liệu nhị phân đã mã hóa.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B03](https://docs.python.org/3.15/library/stdtypes.html#text-sequence-type-str)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B03.02 — Truy cập ký tự và xử lý chuỗi

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B03 — Chuỗi và nhập xuất.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Truy cập ký tự và xử lý chuỗi** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Chuỗi bất biến hỗ trợ indexing, slicing, tìm kiếm, `split`, `join`, `strip`, `replace`. Chỉ số bắt đầu từ 0 và chỉ số âm đếm từ cuối. `s[a:b]` lấy tới trước b; slicing ngoài giới hạn không gây lỗi như indexing.

### 3. Cơ chế hoạt động từng bước

Các phương thức biến đổi chuỗi tạo chuỗi mới chứ không sửa tại chỗ; đây là lý do `s.upper()` không làm `s` thay đổi nếu không gán lại.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
s = "  Python,SQL  "
print(s.strip())
print(s.strip().split(","))
print("ab"[0:10])
```

**Kết quả thực thi trên Python 3.13.5**:

```text
Python,SQL
['Python', 'SQL']
ab
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `strip()` không phải hàm loại bỏ tiền tố cố định; cần `removeprefix` khi muốn loại một prefix nguyên vẹn.
- **Tình huống biên:** Index `s[100]` gây IndexError; slicing `s[:100]` hợp lệ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`split` xử lý ranh giới ký tự, không thay thế parser CSV đầy đủ.

### 7. Bài tập thực hành

**Yêu cầu chính:** Chuẩn hóa một dòng CSV tối giản "  Táo ; Cam ; Ổi  " thành danh sách tên đã loại khoảng trắng (không xử lý CSV quoting).

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B03.02_loi_giai.md](LOI_GIAI/B03.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B03.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `split` xử lý ranh giới ký tự, không thay thế parser CSV đầy đủ.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B03](https://docs.python.org/3.15/library/stdtypes.html#text-sequence-type-str)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B03.03 — input, print và f-string

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B03 — Chuỗi và nhập xuất.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **input, print và f-string** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`input()` trả về chuỗi, ngay cả khi người dùng nhập chữ số. `print()` ghi biểu diễn người đọc được ra luồng xuất; f-string chèn giá trị của biểu thức, có thể kết hợp định dạng số và căn lề. Không nên nhầm thông điệp hiển thị với dữ liệu nội bộ.

### 3. Cơ chế hoạt động từng bước

Quy trình I/O: nhận chuỗi → kiểm tra/chuyển kiểu → tính toán → định dạng đầu ra. `format` và f-string cho phép định dạng mà không tự thay đổi giá trị lưu trong biến.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
ten = "Lan"
gia = 12500
so_luong = 2
print(f"{ten}: {so_luong} x {gia:,} = {gia * so_luong:,}")
```

**Kết quả thực thi trên Python 3.13.5**:

```text
Lan: 2 x 12,500 = 25,000
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không cộng trực tiếp chuỗi từ `input()` với số nguyên; hãy bắt lỗi ValueError khi chuyển kiểu.
- **Tình huống biên:** Nhập rỗng hoặc chữ gây ValueError khi gọi int; ứng dụng cần thông báo rõ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Định dạng đầu ra không phải phép chuyển dữ liệu đầu vào; `input` luôn cho str.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận văn bản số lượng và trả câu thông báo với tổng tiền 8.500 đồng/sản phẩm.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B03.03_loi_giai.md](LOI_GIAI/B03.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B03.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Định dạng đầu ra không phải phép chuyển dữ liệu đầu vào; `input` luôn cho str.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B03](https://docs.python.org/3.15/library/stdtypes.html#text-sequence-type-str)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B03.01, B03.02, B03.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
