# Chương B08 — Đệ quy nhập môn

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B08: Đệ quy nhập môn, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Bài toán con và điều kiện dừng; Đệ quy so với vòng lặp.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B08.01 — Bài toán con và điều kiện dừng](BAI_HOC/B08.01.md)
- [B08.02 — Call stack và lần vết lời gọi](BAI_HOC/B08.02.md)
- [B08.03 — Đệ quy so với vòng lặp](BAI_HOC/B08.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B08.01 — Bài toán con và điều kiện dừng

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B08 — Đệ quy nhập môn.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Bài toán con và điều kiện dừng** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Đệ quy là giải bài toán bằng lời gọi hàm cho một bài toán cùng cấu trúc nhưng nhỏ hơn. Cần điều kiện dừng (base case) và bảo đảm bước đệ quy tiến dần về điều kiện dừng. Không có hai điều này sẽ lặp vô hạn cho đến khi vượt giới hạn recursion.

### 3. Cơ chế hoạt động từng bước

Khi tính giai thừa, `fact(n)` gọi `fact(n-1)` cho tới `fact(0)`. Sau khi chạm base case, kết quả quay lại lần lượt qua các lời gọi trước.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def fact(n):
    if n < 0:
        raise ValueError("n âm")
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(4))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
24
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng đệ quy cho dữ liệu quá sâu nếu độ sâu vượt giới hạn interpreter; vòng lặp thường tránh chi phí call stack.
- **Tình huống biên:** Với n rất lớn, đệ quy có thể gặp RecursionError; đó không phải lỗi phép cộng.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Base case là trường hợp giải trực tiếp; recursive case thu nhỏ bài toán.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm đệ quy tính tổng từ 1 tới n, với n không âm.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B08.01_loi_giai.md](LOI_GIAI/B08.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B08.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Base case là trường hợp giải trực tiếp; recursive case thu nhỏ bài toán.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B08](https://docs.python.org/3.15/reference/executionmodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B08.02 — Call stack và lần vết lời gọi

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B08 — Đệ quy nhập môn.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Call stack và lần vết lời gọi** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Mỗi lần gọi hàm có frame lưu trạng thái thực thi và biến cục bộ. Khi lời gọi đệ quy diễn ra, nhiều frame cùng tồn tại cho tới lúc unwind. Theo dõi “vào hàm” và “trở về” giúp đọc traceback và tìm lỗi điều kiện dừng.

### 3. Cơ chế hoạt động từng bước

Ví dụ `count(3)` tạo 3 lời gọi nối tiếp về phía `count(0)`; sau đó return trả giá trị về gọi trước theo thứ tự ngược. Độ sâu call stack tăng theo số tầng đệ quy.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def dem_xuong(n):
    print("vao", n)
    if n == 0:
        return
    dem_xuong(n - 1)
    print("ra", n)
dem_xuong(2)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
vao 2
vao 1
vao 0
ra 1
ra 2
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không suy ra đệ quy luôn nhanh hơn vòng lặp; Python không bảo đảm tail-call optimization.
- **Tình huống biên:** Đệ quy không có giới hạn được kiểm soát có thể gây RecursionError.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Call stack khác với heap lưu đối tượng; đệ quy tiêu thụ stack cho từng lời gọi.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm `do_sau(n)` trả số frame lời gọi của chính nó tính từ n tới 0, kể cả base case.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B08.02_loi_giai.md](LOI_GIAI/B08.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B08.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Call stack khác với heap lưu đối tượng; đệ quy tiêu thụ stack cho từng lời gọi.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B08](https://docs.python.org/3.15/reference/executionmodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B08.03 — Đệ quy so với vòng lặp

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B08 — Đệ quy nhập môn.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Đệ quy so với vòng lặp** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Đệ quy và vòng lặp có thể giải cùng bài toán nhưng chi phí và độ dễ đọc khác nhau. Đệ quy diễn đạt tốt cấu trúc phân cấp như cây; vòng lặp thường thích hợp cho tích lũy tuyến tính và đầu vào rất lớn. Không phải thuật toán đệ quy nào cũng dễ chuyển đổi mà không dùng stack riêng.

### 3. Cơ chế hoạt động từng bước

So sánh hai cách bằng cùng hợp đồng đầu vào, kiểm thử các trường hợp n=0, n=1, n lớn và đo số lời gọi / bộ nhớ nếu cần.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def tong_vong_lap(n):
    total = 0
    for x in range(n + 1):
        total += x
    return total
print(tong_vong_lap(10))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
55
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Python không tự tối ưu tail-recursion; không dùng đệ quy thuần cho n vài chục nghìn.
- **Tình huống biên:** Với n âm cần phát sinh lỗi thay vì trả kết quả 1 ngoài ý muốn.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Đệ quy là cách biểu diễn lời giải; độ phức tạp thuật toán phụ thuộc lượng công việc, không chỉ cú pháp.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm tính giai thừa bằng vòng lặp; so sánh với cách đệ quy cho n=0,5.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B08.03_loi_giai.md](LOI_GIAI/B08.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B08.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Đệ quy là cách biểu diễn lời giải; độ phức tạp thuật toán phụ thuộc lượng công việc, không chỉ cú pháp.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B08](https://docs.python.org/3.15/reference/executionmodel.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B08.01, B08.02, B08.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
