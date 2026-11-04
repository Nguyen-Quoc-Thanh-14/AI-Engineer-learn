# Chương B05 — Rẽ nhánh và pattern matching

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B05: Rẽ nhánh và pattern matching, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: if, elif, else; match/case, guard và phạm vi áp dụng.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B05.01 — if, elif, else](BAI_HOC/B05.01.md)
- [B05.02 — Điều kiện lồng nhau và kiểm tra dữ liệu](BAI_HOC/B05.02.md)
- [B05.03 — match/case, guard và phạm vi áp dụng](BAI_HOC/B05.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B05.01 — if, elif, else

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B05 — Rẽ nhánh và pattern matching.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **if, elif, else** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`if/elif/else` chọn một nhánh theo truthiness. Python kiểm tra điều kiện theo thứ tự, thực hiện nhánh đầu tiên đúng và bỏ qua nhánh còn lại. Indentation xác định khối lệnh; không có cặp ngoặc nhọn bao khối kiểu C.

### 3. Cơ chế hoạt động từng bước

Đặt các điều kiện loại trừ nhau theo thứ tự phù hợp; `elif` không được đánh giá nếu `if` trước đúng. Nếu không có `else`, có thể không nhánh nào thực thi.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
diem = 72
if diem >= 80:
    print("Giỏi")
elif diem >= 65:
    print("Khá")
else:
    print("Cần cải thiện")
```

**Kết quả thực thi trên Python 3.13.5**:

```text
Khá
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Đặt điều kiện điểm >= 65 trước >= 80 khiến nhánh giỏi không bao giờ tới được.
- **Tình huống biên:** Với điểm 65 và 80 cần kiểm tra biên chính xác; không tự giả định điểm âm hợp lệ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`if` điều khiển luồng; toán tử điều kiện `a if cond else b` là biểu thức.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm phân loại nhiệt độ: < 15 lạnh, <= 30 dễ chịu, > 30 nóng.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B05.01_loi_giai.md](LOI_GIAI/B05.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B05.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `if` điều khiển luồng; toán tử điều kiện `a if cond else b` là biểu thức.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B05](https://docs.python.org/3.15/reference/compound_stmts.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B05.02 — Điều kiện lồng nhau và kiểm tra dữ liệu

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B05 — Rẽ nhánh và pattern matching.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Điều kiện lồng nhau và kiểm tra dữ liệu** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Điều kiện lồng nhau xử lý nhiều quy tắc phụ thuộc, nhưng dễ phức tạp. Nên kiểm tra đầu vào không hợp lệ sớm (guard clause), sau đó xử lý trường hợp bình thường. Kiểm tra kiểu/giá trị phải phản ánh hợp đồng đầu vào, không chỉ dùng `if x:`.

### 3. Cơ chế hoạt động từng bước

Xác định ràng buộc, trả về hoặc raise khi vi phạm, rồi viết đường đi chính ít tầng lồng. Mỗi nhánh quan trọng phải có ít nhất một ca kiểm thử.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def phi_giao_hang(gia_tri, la_thanh_vien):
    if gia_tri < 0:
        raise ValueError("đơn hàng âm")
    if la_thanh_vien and gia_tri >= 100000:
        return 0
    return 15000
print(phi_giao_hang(100000, True))
print(phi_giao_hang(99999, True))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
0
15000
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không viết điều kiện quá tổng quát rồi che khuất nhánh cụ thể. Một `else` đặt sai mức thụt lề đổi hoàn toàn logic.
- **Tình huống biên:** Giá trị sát ngưỡng 199999, 200000 phải thử riêng.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Validation là kiểm tra ràng buộc dữ liệu; business condition là chính sách xử lý sau kiểm tra.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm phí: dưới 0 -> ValueError; >=200000 được miễn; các trường hợp còn lại 20000.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B05.02_loi_giai.md](LOI_GIAI/B05.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B05.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Validation là kiểm tra ràng buộc dữ liệu; business condition là chính sách xử lý sau kiểm tra.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B05](https://docs.python.org/3.15/reference/compound_stmts.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B05.03 — match/case, guard và phạm vi áp dụng

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B05 — Rẽ nhánh và pattern matching.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **match/case, guard và phạm vi áp dụng** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`match/case` (Python 3.10+) là structural pattern matching, không đơn giản là phép so sánh bằng nhiều lần. Pattern có thể giải cấu trúc tuple, list, mapping và class; guard (`if ...`) bổ sung điều kiện. Những tên trần trong pattern thường là capture patterns chứ không phải tham chiếu biến có sẵn.

### 3. Cơ chế hoạt động từng bước

Python thử case theo thứ tự; khi pattern và guard khớp, thực hiện nhánh đó. `case _` là wildcard. Đặt case cụ thể trước case tổng quát để tránh che khuất.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def phan_tich_lenh(cmd):
    match cmd:
        case ("add", x, y) if isinstance(x, int) and isinstance(y, int):
            return x + y
        case ("quit",):
            return "bye"
        case _:
            return "unknown"
print(phan_tich_lenh(("add", 2, 3)))
print(phan_tich_lenh(("quit",)))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
5
bye
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `case name:` không kiểm tra biến name có bằng dữ liệu không; nó bắt giá trị vào tên `name`. Dùng literal, enum hoặc qualified constant cho value pattern.
- **Tình huống biên:** Các guard trong ví dụ giả định dữ liệu số có thể so sánh với 0; ứng dụng thực tế nên xác minh kiểu trước.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Pattern matching là khớp cấu trúc; if/elif thích hợp khi kiểm tra điều kiện tổng quát không có cấu trúc cố định.

### 7. Bài tập thực hành

**Yêu cầu chính:** Xây hàm `tai_hinh_dang` xử lý `("square", canh)` và `("rectangle", dai, rong)`; trường hợp khác trả None.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B05.03_loi_giai.md](LOI_GIAI/B05.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B05.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Pattern matching là khớp cấu trúc; if/elif thích hợp khi kiểm tra điều kiện tổng quát không có cấu trúc cố định.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B05](https://docs.python.org/3.15/reference/compound_stmts.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B05.01, B05.02, B05.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
