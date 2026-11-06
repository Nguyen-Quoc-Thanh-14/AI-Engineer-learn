# Chương C07 — Collections hiện đại và Python 3.15

> **Giai đoạn:** GD2 · **Học phần:** Cấu trúc và xử lý dữ liệu Python  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương C07: Collections hiện đại và Python 3.15, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: collections.abc, Mapping và hashability; Unpacking trong comprehensions (Python 3.15).
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [C07.01 — collections.abc, Mapping và hashability](BAI_HOC/C07.01.md)
- [C07.02 — frozendict và cấu trúc mapping bất biến](BAI_HOC/C07.02.md)
- [C07.03 — sentinel và phân biệt None với trạng thái thiếu](BAI_HOC/C07.03.md)
- [C07.04 — Unpacking trong comprehensions (Python 3.15)](BAI_HOC/C07.04.md)

## Tiên quyết

C02, C04

## Nguồn đối chiếu

- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)

---

## C07.01 — collections.abc, Mapping và hashability

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** C07 — Collections hiện đại và Python 3.15.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **collections.abc, Mapping và hashability** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** C02, C04.

### 2. Khái niệm và bản chất

`collections.abc.Mapping` định nghĩa giao diện ánh xạ chỉ đọc ở mức phương thức; `MutableMapping` bổ sung thao tác ghi. Đây là API protocol, không bảo đảm dữ liệu thật sự immutable. Hashability thuộc hợp đồng `__hash__` và `__eq__`, độc lập với việc một đối tượng thỏa Mapping.

### 3. Cơ chế hoạt động từng bước

Có thể nhận một đối tượng Mapping trong hàm để giảm phụ thuộc vào dict cụ thể. Dùng `isinstance(x, Mapping)` khi yêu cầu runtime và cân nhắc type hint `Mapping[K,V]`.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
from collections.abc import Mapping
print(isinstance({"x": 1}, Mapping))
print(isinstance([1], Mapping))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
True
False
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không coi `Mapping` là kiểu `dict` cụ thể; code phụ thuộc `.update()` sẽ không chạy với mọi Mapping.
- **Tình huống biên:** Mapping tùy biến có thể có khóa không so sánh được để sorted; bài tập giả định khóa str.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`Mapping` thể hiện giao diện đọc; `MutableMapping` thể hiện khả năng thay đổi.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận bất kỳ Mapping và trả list khóa đã sắp.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C07.01_loi_giai.md](LOI_GIAI/C07.01_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C07.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `Mapping` thể hiện giao diện đọc; `MutableMapping` thể hiện khả năng thay đổi.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C07](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C07.02 — frozendict và cấu trúc mapping bất biến

> **Trạng thái:** ĐÃ BIÊN SOẠN — CHỜ KIỂM THỬ PYTHON 3.15.
> **Giai đoạn:** GD2 · **Chương:** C07 — Collections hiện đại và Python 3.15.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **frozendict và cấu trúc mapping bất biến** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** C02, C04.

### 2. Khái niệm và bản chất

Python 3.15 giới thiệu built-in `frozendict`, một mapping bất biến và giữ thứ tự chèn; không phải phân lớp của `dict`. Đối tượng frozendict chỉ hashable khi toàn bộ khóa và giá trị hashable. Khác với `MappingProxyType` là view bảo vệ cách ghi thông qua proxy, `frozendict` giữ mapping riêng bất biến.

### 3. Cơ chế hoạt động từng bước

Khởi tạo từ dữ liệu rồi chỉ đọc; thao tác `d[k]=v` gây TypeError. Dùng frozendict cho cấu hình nhỏ, khóa cache hay cấu trúc có ngữ nghĩa bất biến khi các phần tử thích hợp.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
## Chỉ chạy với CPython 3.15+
d = frozendict({"env": "prod", "retry": 3})
print(d["retry"])
print(hash(d) == hash(frozendict({"retry": 3, "env": "prod"})))
```

**Kết quả:** Chưa chạy thực tế vì ví dụ đòi hỏi Python 3.15+; không coi đoạn mã là đã kiểm thử trên 3.15.
Trước khi dùng làm bài kiểm tra chính thức, hãy cài CPython 3.15.2 và chạy lại cả ví dụ lẫn lời giải.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng được trên Python 3.13; không được coi một frozendict chứa list là hashable.
- **Tình huống biên:** Test runtime 3.15 bắt buộc; tài liệu từ Python What’s New 3.15.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`frozendict` là built-in bất biến; `types.MappingProxyType` là read-only view phản ánh thay đổi dict nguồn.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận dict số nguyên và trả frozendict chứa giá trị được tăng một đơn vị.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C07.02_loi_giai.md](LOI_GIAI/C07.02_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C07.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `frozendict` là built-in bất biến; `types.MappingProxyType` là read-only view phản ánh thay đổi dict nguồn.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C07](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C07.03 — sentinel và phân biệt None với trạng thái thiếu

> **Trạng thái:** ĐÃ BIÊN SOẠN — CHỜ KIỂM THỬ PYTHON 3.15.
> **Giai đoạn:** GD2 · **Chương:** C07 — Collections hiện đại và Python 3.15.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **sentinel và phân biệt None với trạng thái thiếu** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** C02, C04.

### 2. Khái niệm và bản chất

Python 3.15 bổ sung `sentinel`, một kiểu built-in dành cho giá trị đánh dấu độc nhất theo danh tính. Khi `None` là dữ liệu hợp lệ, một sentinel riêng giúp phân biệt “không truyền đối số/không có khóa” với giá trị None thực. Trước 3.15 thường dùng `object()` hoặc sentinel tùy biến.

### 3. Cơ chế hoạt động từng bước

Tạo sentinel có tên rõ; so sánh bằng `is` thay vì `==`. Dùng `dict.get(key, NOT_FOUND)` rồi kiểm tra identity để biết khóa có tồn tại.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
## Chỉ chạy với Python 3.15+
MISSING = sentinel("MISSING")
data = {"x": None}
print(data.get("x", MISSING) is MISSING)
print(data.get("y", MISSING) is MISSING)
```

**Kết quả:** Chưa chạy thực tế vì ví dụ đòi hỏi Python 3.15+; không coi đoạn mã là đã kiểm thử trên 3.15.
Trước khi dùng làm bài kiểm tra chính thức, hãy cài CPython 3.15.2 và chạy lại cả ví dụ lẫn lời giải.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không thay thế mọi `None` bằng sentinel; chỉ dùng khi bài toán cần trạng thái khác biệt.
- **Tình huống biên:** Phiên bản 3.13 không có built-in sentinel, cần runtime 3.15 để kiểm chứng API.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

`None` là built-in singleton có ngữ nghĩa thiếu trong nhiều API; sentinel riêng phù hợp khi None cũng là dữ liệu.

### 7. Bài tập thực hành

**Yêu cầu chính:** Tạo hàm lấy khóa: nếu vắng khóa trả sentinel; nếu có khóa với None thì trả None.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C07.03_loi_giai.md](LOI_GIAI/C07.03_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C07.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `None` là built-in singleton có ngữ nghĩa thiếu trong nhiều API; sentinel riêng phù hợp khi None cũng là dữ liệu.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C07](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## C07.04 — Unpacking trong comprehensions (Python 3.15)

> **Trạng thái:** ĐÃ BIÊN SOẠN — CHỜ KIỂM THỬ PYTHON 3.15.
> **Giai đoạn:** GD2 · **Chương:** C07 — Collections hiện đại và Python 3.15.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

### 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Unpacking trong comprehensions (Python 3.15)** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** C02, C04.

### 2. Khái niệm và bản chất

Python 3.15 hỗ trợ cú pháp unpacking `*` và `**` trong các comprehension để nối các iterable hoặc ánh xạ. Đây là phần mở rộng cú pháp; trên Python 3.13, `[ *items for items in groups ]` gây SyntaxError. Các cách viết tương đương ở bản cũ là comprehension lồng hoặc itertools.chain.

### 3. Cơ chế hoạt động từng bước

Trong comprehension unpacking, từng iterable được mở rộng và đưa phần tử vào kết quả theo thứ tự duyệt. Dictionary unpacking xử lý khóa trùng theo quy tắc giá trị xuất hiện sau ghi đè trước.

### 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
## Chỉ chạy với Python 3.15+
groups = [[1,2],[3],[4,5]]
print([*group for group in groups])
print({**item for item in [{"a":1},{"b":2}]})
```

**Kết quả:** Chưa chạy thực tế vì ví dụ đòi hỏi Python 3.15+; không coi đoạn mã là đã kiểm thử trên 3.15.
Trước khi dùng làm bài kiểm tra chính thức, hãy cài CPython 3.15.2 và chạy lại cả ví dụ lẫn lời giải.

### 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không viết cú pháp mới vào tài liệu yêu cầu chạy trên 3.13 mà không ghi chú version; khi cần tương thích dùng `[x for group in groups for x in group]`.
- **Tình huống biên:** Bản thân `[*iterable]` không mới; dấu `*` *bên trong vòng for của comprehension* mới được thêm ở 3.15.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

### 6. Phân biệt khái niệm dễ nhầm

Comprehension cũ với 2 for hỗ trợ tất cả phiên bản hiện đại; unpacking comprehension là cú pháp ngắn mới.

### 7. Bài tập thực hành

**Yêu cầu chính:** Viết một list comprehension 3.15 hợp nhất ba list, và so sánh với phiên bản tương thích Python 3.13.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [C07.04_loi_giai.md](LOI_GIAI/C07.04_loi_giai.md) — đọc sau khi tự làm.

### 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ C07.04, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Comprehension cũ với 2 for hỗ trợ tất cả phiên bản hiện đại; unpacking comprehension là cú pháp ngắn mới.

### 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

### 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho C07](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: C07.01, C07.02, C07.03, C07.04. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
