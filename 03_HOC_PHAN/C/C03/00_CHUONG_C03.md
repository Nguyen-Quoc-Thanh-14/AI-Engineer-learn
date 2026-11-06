# Chương C03

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# C03.01 — Mutable và immutable

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C03 — Tính khả biến và sao chép.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Mutable và immutable** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

## 2. Khái niệm và bản chất

Tính khả biến (mutability) là khả năng thay đổi trạng thái đối tượng sau khi tạo. List, dict, set thường mutable; tuple, str, int thường immutable. Phép `+=` có hành vi khác tùy kiểu: list thường sửa tại chỗ, tuple tạo đối tượng mới. Tuy nhiên không dựa vào `id()` trong ví dụ để suy luận mọi tối ưu triển khai.

## 3. Cơ chế hoạt động từng bước

Xác định đối tượng trước và sau thao tác, tách tên và đối tượng. Khi dùng object mutable làm tham số, quyết định rõ hàm có được phép sửa đầu vào không.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
a = [1]
b = a
a += [2]
print(b)
x = (1,)
y = x
x += (2,)
print(y, x)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[1, 2]
(1,) (1, 2)
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `tuple` bất biến không có nghĩa nội dung của list con trong tuple không thể thay đổi.
- **Tình huống biên:** Không giả định mọi phép `+=` đều tạo bản sao hoặc đều sửa tại chỗ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Tên là binding; mutability là thuộc tính đối tượng.

## 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nối một phần tử vào tuple và kiểm tra tuple ban đầu giữ nguyên.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C03.01_loi_giai.md](LOI_GIAI/C03.01_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C03.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Tên là binding; mutability là thuộc tính đối tượng.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C03](https://docs.python.org/3.15/library/copy.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Mutable là khả năng thay đổi trạng thái của cùng một đối tượng; aliasing xảy ra khi nhiều tên trỏ tới cùng đối tượng. Thao tác tạo bản sao không tương đương thay đổi trực tiếp đối tượng cũ.

### Cách suy luận và thiết kế lời giải

Cho hai tên cùng tham chiếu list ban đầu, append bằng alias sẽ làm cả hai cùng quan sát thay đổi. Tạo list mới trước khi append giúp bảo toàn dữ liệu đầu vào; tuy nhiên đây chỉ là shallow copy, phần tử lồng nhau vẫn có thể được chia sẻ.

### Phản ví dụ và ngộ nhận cần tránh

Nhầm `b = a` thành sao chép; hoặc cho rằng copy một list tự động sao chép sâu tất cả phần tử con.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`C03.01_bai_tap_da_giai_v25.py`](MA_MAU/C03.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`C03.01_loi_giai.md`](LOI_GIAI/C03.01_loi_giai.md).
5. **Bài mở rộng:** Kiểm thử với list chứa dict, chứng minh shallow copy vẫn dùng chung dict bên trong; tìm khi nào cần copy.deepcopy.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/copy.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# C03.02 — is, ==, aliasing

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C03 — Tính khả biến và sao chép.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **is, ==, aliasing** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

## 2. Khái niệm và bản chất

`is` hỏi hai tham chiếu có trỏ đúng cùng đối tượng không; `==` hỏi hai đối tượng có bằng nhau theo phép so sánh của kiểu không. Aliasing là hiện tượng nhiều tên tham chiếu chung một đối tượng. Aliasing có ích khi muốn cùng cập nhật, nhưng có thể tạo bug khó phát hiện.

## 3. Cơ chế hoạt động từng bước

Tạo hai list bằng hai literal tương đương: nội dung bằng nhau nhưng identity khác. Nếu gán `b=a`, hai tên trỏ chung đối tượng; thay đổi phần tử có thể ảnh hưởng cả hai.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b)
print(a is c)
c[0] = 9
print(a)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
True False
True
[9, 2]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không so sánh chuỗi/số bằng `is`: caching và interning không phải hợp đồng cho chương trình.
- **Tình huống biên:** `None` là singleton; dùng `x is None` thay cho `x == None`.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Identity dùng cho sentinel và cùng đối tượng; equality dùng so sánh dữ liệu.

## 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm trả về bản sao list (top-level), chứng minh bằng `is not` và `==`.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C03.02_loi_giai.md](LOI_GIAI/C03.02_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C03.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Identity dùng cho sentinel và cùng đối tượng; equality dùng so sánh dữ liệu.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C03](https://docs.python.org/3.15/library/copy.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


---

# C03.03 — Shallow copy và deep copy nhập môn

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C03 — Tính khả biến và sao chép.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Shallow copy và deep copy nhập môn** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** B.

## 2. Khái niệm và bản chất

Sao chép nông (`copy.copy`, list.copy) tạo container ngoài mới nhưng giữ tham chiếu tới phần tử. Sao chép sâu (`copy.deepcopy`) cố gắng đệ quy tạo các bản sao của đối tượng có thể thay đổi bên trong, đồng thời giữ quan hệ tham chiếu bằng memo. Không nên deep copy bừa bãi các đối tượng chứa tài nguyên hệ thống.

## 3. Cơ chế hoạt động từng bước

Với list lồng nhau, sửa list con qua bản sao nông cũng thay đổi list con của bản gốc; bản sao sâu tách các list con.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
import copy
x = [[1], [2]]
y = copy.copy(x)
z = copy.deepcopy(x)
y[0].append(3)
print(x)
print(z)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
[[1, 3], [2]]
[[1], [2]]
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `list(x)` không tạo bản sao sâu. Deepcopy có thể tốn bộ nhớ và có hành vi đặc biệt cho custom objects.
- **Tình huống biên:** Deepcopy không phải thao tác tuần tự hóa tài nguyên như file handle hay socket.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Đổi binding khác với shallow copy; shallow copy khác với deep copy.

## 7. Bài tập thực hành

**Yêu cầu chính:** Sao chép sâu list lồng nhau, sửa bản sao và chứng minh nguồn giữ nguyên.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C03.03_loi_giai.md](LOI_GIAI/C03.03_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C03.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Đổi binding khác với shallow copy; shallow copy khác với deep copy.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C03](https://docs.python.org/3.15/library/copy.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C03.01, C03.02, C03.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
