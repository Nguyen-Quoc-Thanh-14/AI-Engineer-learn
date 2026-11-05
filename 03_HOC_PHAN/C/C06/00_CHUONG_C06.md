# Chương C06 — Biến đổi dữ liệu và Big-O

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C06: Biến đổi dữ liệu và Big-O, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Lọc, nhóm, đếm và tổng hợp; Độ phức tạp thao tác list, dict và set.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C06.01 — Lọc, nhóm, đếm và tổng hợp](BAI_HOC/C06.01.md)
- [C06.02 — collections, itertools, functools cơ bản](BAI_HOC/C06.02.md)
- [C06.03 — Độ phức tạp thao tác list, dict và set](BAI_HOC/C06.03.md)

## Tiên quyết

B

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## C06.01 — Lọc, nhóm, đếm và tổng hợp

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C06 — Biến đổi dữ liệu và Big-O.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Lọc, nhóm, đếm và tổng hợp** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Lọc, đếm, nhóm và tổng hợp là chuỗi thao tác dữ liệu thường gặp. Trước khi chọn công cụ, xác định đầu vào, khóa nhóm, yêu cầu thứ tự và cách xử lý giá trị thiếu. `collections.Counter` đếm phần tử hashable; `defaultdict(list)` tạo nhóm.

### 3. Cơ chế hoạt động từng bước

Mẫu pipeline: lọc bản ghi không hợp lệ → tạo khóa → đếm/nhóm → trả cấu trúc dễ kiểm thử. Tránh biến đổi danh sách đang duyệt gây bỏ qua phần tử.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
from collections import Counter
mon = ["cà phê", "trà", "cà phê"]
print(sorted(Counter(mon).items()))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[('cà phê', 2), ('trà', 1)]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Đừng dùng đếm dựa trên `list.count` trong vòng lặp lớn khi Counter có thể làm việc trong một lượt.
- **Tình huống biên:** Văn bản tiếng Việt có dấu có thể cần chuẩn hóa trước khi nhóm theo ký tự đầu.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Counter là bảng tần suất; defaultdict là dict tự tạo giá trị thiếu từ factory.

### 7. Bài tập thực hành

**Yêu cầu chính:** Nhóm tên theo chữ cái đầu, bỏ chuỗi rỗng.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C06.01_loi_giai.md](LOI_GIAI/C06.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C06.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Counter là bảng tần suất; defaultdict là dict tự tạo giá trị thiếu từ factory.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C06](https://docs.python.org/3.15/library/collections.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C06.02 — collections, itertools, functools cơ bản

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C06 — Biến đổi dữ liệu và Big-O.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **collections, itertools, functools cơ bản** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

`collections`, `itertools`, `functools` là thư viện chuẩn cho container, iterator và hàm bậc cao. `deque` phù hợp thao tác hai đầu; `itertools.chain` nối nguồn lặp lười; `functools.lru_cache` ghi nhớ kết quả hàm thuần theo đối số hashable.

### 3. Cơ chế hoạt động từng bước

Chọn đúng abstraction: dữ liệu nhỏ có thể dùng list đơn giản; xử lý nhiều chuỗi dữ liệu dùng iterator và chain; cache phải xét thay đổi trạng thái và bộ nhớ.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
from collections import deque
from itertools import chain
q = deque([1,2]); q.appendleft(0)
print(list(q))
print(list(chain([1,2], [3])))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[0, 1, 2]
[1, 2, 3]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Cache một hàm đọc dữ liệu thay đổi liên tục có thể trả kết quả lỗi thời; cache không phù hợp cho mọi hàm.
- **Tình huống biên:** Với iterator một lượt, `chain` tiêu thụ dần và không thể tua lại.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`chain` duyệt lười; `a+b` chỉ khả dụng cho một số loại sequence tương thích.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận hai iterable và trả list nối bằng `itertools.chain`.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C06.02_loi_giai.md](LOI_GIAI/C06.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C06.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `chain` duyệt lười; `a+b` chỉ khả dụng cho một số loại sequence tương thích.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C06](https://docs.python.org/3.15/library/collections.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C06.03 — Độ phức tạp thao tác list, dict và set

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C06 — Biến đổi dữ liệu và Big-O.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Độ phức tạp thao tác list, dict và set** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

### 2. Khái niệm và bản chất

Big-O mô tả tốc độ tăng thời gian/bộ nhớ theo kích thước đầu vào; không đo trực tiếp số mili giây. Với các cấu trúc chuẩn CPython, truy cập list theo index và tra dict có kỳ vọng gần O(1), duyệt list O(n), tìm `x in list` O(n); thực tế còn phụ thuộc dữ liệu và implementation.

### 3. Cơ chế hoạt động từng bước

Đầu tiên mô tả n, sau đó đếm số phép toán nổi trội; xét best/average/worst khi có khác biệt. Đừng tối ưu cú pháp trước khi chọn đúng cấu trúc dữ liệu.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
items = list(range(1000))
need = {3, 500, 999}
print(500 in items)
print(500 in need)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
True
True
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Dict/set không có bảo đảm O(1) cho mọi đầu vào; va chạm hash và tấn công có thể ảnh hưởng worst-case.
- **Tình huống biên:** Việc tạo set tốn O(m) thời gian và bộ nhớ; với đầu vào rất nhỏ, không nhất thiết tối ưu hơn.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Big-O là mô hình tiệm cận; benchmarking là đo trên máy và đầu vào cụ thể.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm lọc các phần tử `values` thuộc `allowed` bằng cách chuyển allowed sang set để tra cứu nhanh.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C06.03_loi_giai.md](LOI_GIAI/C06.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C06.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Big-O là mô hình tiệm cận; benchmarking là đo trên máy và đầu vào cụ thể.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C06](https://docs.python.org/3.15/library/collections.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C06.01, C06.02, C06.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
