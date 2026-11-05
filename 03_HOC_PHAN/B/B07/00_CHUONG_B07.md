# Chương B07 — Hàm cơ bản

> **Giai đoạn:** GD1 · **Học phần:** Ngôn ngữ Python nền tảng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương B07: Hàm cơ bản, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: def, call, return; Hàm thuần, side effect và phạm vi biến.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [B07.01 — def, call, return](BAI_HOC/B07.01.md)
- [B07.02 — Tham số, đối số và giá trị mặc định](BAI_HOC/B07.02.md)
- [B07.03 — Hàm thuần, side effect và phạm vi biến](BAI_HOC/B07.03.md)

## Tiên quyết

A

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## B07.01 — def, call, return

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B07 — Hàm cơ bản.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **def, call, return** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Hàm tạo đơn vị tái sử dụng với đầu vào qua tham số và kết quả qua `return`. Thực thi `def` tạo đối tượng hàm và liên kết tới tên; thân hàm chỉ chạy khi được gọi. Hàm không có return rõ ràng trả về `None`.

### 3. Cơ chế hoạt động từng bước

Khi gọi, đối số được đánh giá, tham số liên kết tới đối tượng tương ứng; thân hàm chạy và return chuyển quyền điều khiển cho nơi gọi.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def hinh_chu_nhat(dai, rong):
    return dai * rong
print(hinh_chu_nhat(4, 5))
print(hinh_chu_nhat(0, 5))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
20
0
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Nhầm `print(kq)` với `return kq`: print không tự làm hàm trả về kết quả tính toán.
- **Tình huống biên:** Nhầm thứ tự đối số có thể không gây lỗi cú pháp nhưng gây sai nghiệp vụ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Hàm là một giá trị; gọi hàm dùng dấu ngoặc `f()`, còn `f` là chính đối tượng hàm.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm `gia_sau_giam(gia, phan_tram)` có kiểm tra giá và phần trăm giảm trong [0,100].

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B07.01_loi_giai.md](LOI_GIAI/B07.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B07.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Hàm là một giá trị; gọi hàm dùng dấu ngoặc `f()`, còn `f` là chính đối tượng hàm.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B07](https://docs.python.org/3.15/tutorial/controlflow.html#defining-functions)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B07.02 — Tham số, đối số và giá trị mặc định

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B07 — Hàm cơ bản.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Tham số, đối số và giá trị mặc định** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Parameter (tham số) là tên trong định nghĩa, argument (đối số) là giá trị khi gọi. Python hỗ trợ positional, keyword, default, `*args`, `**kwargs`, positional-only (`/`), keyword-only (`*`). Giá trị mặc định được đánh giá một lần khi `def` chạy, không được tính lại mỗi lần gọi.

### 3. Cơ chế hoạt động từng bước

Python gán đối số vào các tham số theo chữ ký hàm và kiểm tra thiếu, thừa hoặc trùng lặp. Thiết kế keyword-only cho tham số dễ nhầm lẫn làm lời gọi dễ đọc hơn.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def tinh_gia(gia, so_luong=1, *, thue=0.1):
    return gia * so_luong * (1 + thue)
print(tinh_gia(100))
print(tinh_gia(100, 2, thue=0))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
110.00000000000001
200
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng list/dict có thể thay đổi làm default nếu sẽ sửa chúng trong hàm: dùng None rồi tạo đối tượng mới bên trong.
- **Tình huống biên:** Đưa cùng một tham số cả vị trí và keyword gây TypeError.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Đối số vị trí xác định theo vị trí; đối số từ khóa xác định theo tên; giá trị mặc định không phải tham số bắt buộc.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm `them_item(item, danh_sach=None)` trả danh sách mới và không chia sẻ dữ liệu default giữa hai lần gọi.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B07.02_loi_giai.md](LOI_GIAI/B07.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B07.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Đối số vị trí xác định theo vị trí; đối số từ khóa xác định theo tên; giá trị mặc định không phải tham số bắt buộc.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B07](https://docs.python.org/3.15/tutorial/controlflow.html#defining-functions)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## B07.03 — Hàm thuần, side effect và phạm vi biến

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B07 — Hàm cơ bản.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Hàm thuần, side effect và phạm vi biến** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

### 2. Khái niệm và bản chất

Hàm thuần (pure function) có cùng kết quả khi nhận cùng đầu vào và không tạo hiệu ứng phụ quan sát được. Python không ép hàm phải thuần; đọc/ghi file, print, biến đổi list đầu vào hoặc đọc trạng thái toàn cục thường tạo side effect. Biết phân biệt giúp kiểm thử và tái sử dụng dễ hơn.

### 3. Cơ chế hoạt động từng bước

Để giảm side effect, truyền dữ liệu cần thiết qua tham số và trả kết quả thay vì thay đổi tài nguyên bên ngoài. Biến cục bộ được tạo trong phạm vi hàm; đọc tên có thể tuân theo quy tắc tra cứu scope.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def them_thue(gia, ti_le):
    return gia * (1 + ti_le)
base = 100
print(them_thue(base, 0.1))
print(base)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
110.00000000000001
100
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Hàm có print bên trong khác hàm return kết quả; “không sửa tham số tên” không đủ để đảm bảo không sửa đối tượng truyền vào.
- **Tình huống biên:** Các phép toán trên mutable object có thể có side effect dù không dùng global.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Hàm thuần là thuộc tính hành vi; local/global là cơ chế phạm vi tên, không đồng nghĩa thuần/không thuần.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận danh sách điểm và trả list điểm cộng 1 mà không thay đổi đầu vào.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B07.03_loi_giai.md](LOI_GIAI/B07.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B07.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Hàm thuần là thuộc tính hành vi; local/global là cơ chế phạm vi tên, không đồng nghĩa thuần/không thuần.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B07](https://docs.python.org/3.15/tutorial/controlflow.html#defining-functions)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B07.01, B07.02, B07.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
