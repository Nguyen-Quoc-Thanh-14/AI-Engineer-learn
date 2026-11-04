# Chương B06 — Vòng lặp và điều khiển luồng

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B06: Vòng lặp và điều khiển luồng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: for, while và range; Vòng lặp lồng nhau và vòng lặp vô hạn.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B06.01 — for, while và range](BAI_HOC/B06.01.md)
- [B06.02 — break, continue và loop else](BAI_HOC/B06.02.md)
- [B06.03 — Vòng lặp lồng nhau và vòng lặp vô hạn](BAI_HOC/B06.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B06.01 — for, while và range

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B06 — Vòng lặp và điều khiển luồng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **for, while và range** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Vòng `for` duyệt phần tử từ iterable; `while` lặp khi điều kiện còn đúng. `range(start, stop, step)` sinh một dãy số theo quy tắc, đầu stop không bao gồm. Trong Python, `for` không nhất thiết là bộ đếm tăng giống các ngôn ngữ khác.

### 3. Cơ chế hoạt động từng bước

`for` lấy iterator từ iterable, gọi lần lượt next cho đến StopIteration. `while` đánh giá lại điều kiện trước mỗi vòng; phải bảo đảm trạng thái tiến gần điểm dừng.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
tong = 0
for n in range(1, 5):
    tong += n
print(tong)
x = 3
while x > 0:
    print(x)
    x -= 1
```

**Kết quả thực thi trên Python 3.13.5**:

```text
10
3
2
1
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `range(1, 5)` chỉ có 1,2,3,4; thay đổi danh sách trong lúc for duyệt có thể làm bỏ sót phần tử.
- **Tình huống biên:** `range` với step bằng 0 phát sinh ValueError.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`for` hữu ích khi biết iterable; `while` phù hợp tiến trình phụ thuộc trạng thái.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm tính tổng số chẵn từ 0 tới n (kể cả n), yêu cầu n không âm.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B06.01_loi_giai.md](LOI_GIAI/B06.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B06.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `for` hữu ích khi biết iterable; `while` phù hợp tiến trình phụ thuộc trạng thái.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B06](https://docs.python.org/3.15/tutorial/controlflow.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B06.02 — break, continue và loop else

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B06 — Vòng lặp và điều khiển luồng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **break, continue và loop else** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

`break` dừng vòng lặp gần nhất, `continue` bỏ phần còn lại của lần lặp hiện tại, `else` của vòng lặp chạy nếu vòng kết thúc bình thường mà không bị `break`. `else` này không phải nhánh “điều kiện sai” theo cách hiểu của if.

### 3. Cơ chế hoạt động từng bước

Tìm kiếm tuyến tính: duyệt → gặp mục tiêu thì break → không gặp mục tiêu thì else chạy. Dùng hàm return có thể đơn giản hơn khi chỉ cần kết luận.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
data = [3, 8, 10]
for x in data:
    if x == 8:
        print("found")
        break
else:
    print("not found")
```

**Kết quả thực thi trên Python 3.13.5**:

```text
found
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Với `continue`, vòng vẫn có thể kết thúc bình thường và chạy else; else chỉ bị bỏ qua khi break.
- **Tình huống biên:** Vòng duyệt tập rỗng sẽ chạy else nếu có, vì không có break.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`break` rời vòng, không rời hàm; `return` rời hàm ngay lập tức.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm trả về vị trí số âm đầu tiên hoặc None khi không có số âm.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B06.02_loi_giai.md](LOI_GIAI/B06.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B06.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `break` rời vòng, không rời hàm; `return` rời hàm ngay lập tức.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B06](https://docs.python.org/3.15/tutorial/controlflow.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B06.03 — Vòng lặp lồng nhau và vòng lặp vô hạn

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B06 — Vòng lặp và điều khiển luồng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Vòng lặp lồng nhau và vòng lặp vô hạn** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Vòng lặp lồng nhau xử lý tích Descartes hoặc bảng hai chiều. Chi phí có thể tăng nhanh (ví dụ hai vòng n phần tử thường là O(n²)). Vòng lặp vô hạn thường do thiếu cập nhật trạng thái hoặc điều kiện dừng sai.

### 3. Cơ chế hoạt động từng bước

Với mỗi phần tử vòng ngoài, vòng trong chạy toàn bộ phần việc. Đếm số lần thực thi, đặt giới hạn số lượt nếu bài toán có nguy cơ không kết thúc.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
cap = []
for a in range(2):
    for b in range(3):
        cap.append((a, b))
print(cap)
print(len(cap))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
6
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `break` chỉ dừng vòng trong gần nhất; muốn dừng cả hai vòng cần return, cờ điều kiện hoặc cấu trúc khác.
- **Tình huống biên:** Vòng `while True` có thể hợp lệ nếu có điều kiện break rõ ràng và được kiểm thử.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Hai vòng lặp lồng nhau không tự động chậm; cần xét kích thước dữ liệu và chi phí thực tế.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm tìm tất cả cặp `(x,y)` với x trong [0,n), y trong [0,m) và x+y chẵn.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B06.03_loi_giai.md](LOI_GIAI/B06.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B06.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Hai vòng lặp lồng nhau không tự động chậm; cần xét kích thước dữ liệu và chi phí thực tế.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B06](https://docs.python.org/3.15/tutorial/controlflow.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B06.01, B06.02, B06.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
