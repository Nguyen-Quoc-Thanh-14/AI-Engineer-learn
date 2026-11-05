# Chương B09

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# B09.01 — int, float, decimal và sai số

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B09 — Độ chính xác dữ liệu và sai lầm nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **int, float, decimal và sai số** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

## 2. Khái niệm và bản chất

Chọn biểu diễn số theo yêu cầu chính xác và đơn vị: `int` thích hợp đếm và lưu tiền theo đơn vị nhỏ nhất; `float` thích hợp số đo xấp xỉ; `decimal.Decimal` thao tác thập phân có ngữ cảnh độ chính xác/làm tròn. `Decimal("0.1")` giữ giá trị thập phân đã nhập; `Decimal(0.1)` tiếp nhận sự xấp xỉ float sẵn có.

## 3. Cơ chế hoạt động từng bước

Tách giá trị thực, đơn vị và quy tắc làm tròn. Khi trình bày tiền tệ, sử dụng `quantize` theo định dạng bắt buộc, kiểm tra tình huống tăng/giảm một đơn vị nhỏ.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
print(0.1 + 0.2 == 0.3)
```

**Kết quả thực thi trên Python 3.13.5**:

```text
0.3
False
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Trộn float với Decimal thiếu kiểm soát có thể gây TypeError và phá vỡ mục tiêu chính xác.
- **Tình huống biên:** Quy tắc `ROUND_HALF_EVEN` mặc định có thể khác yêu cầu của bài toán nghiệp vụ.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Bản chất `float` không phải lỗi lập trình; lỗi là chọn biểu diễn không đáp ứng hợp đồng.

## 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận chuỗi tiền và thuế suất, trả tổng tiền đã làm tròn hai chữ số theo ROUND_HALF_UP.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B09.01_loi_giai.md](LOI_GIAI/B09.01_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B09.01, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Bản chất `float` không phải lỗi lập trình; lỗi là chọn biểu diễn không đáp ứng hợp đồng.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B09](https://docs.python.org/3.15/library/decimal.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Floating-point arithmetic: issues and limitations](https://docs.python.org/3.15/tutorial/floatingpoint.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

float lưu số theo biểu diễn nhị phân hữu hạn, nên nhiều giá trị thập phân không thể biểu diễn chính xác; Decimal chỉ giúp khi được khởi tạo đúng cách và dùng quy tắc làm tròn cụ thể.

### Cách suy luận và thiết kế lời giải

Tính tổng tiền bằng Decimal(str(value)) để tránh đưa nhiễu float đã tồn tại vào phép tính; quantize đến hai chữ số sau dấu phẩy với ROUND_HALF_UP. Phân biệt phép so sánh gần đúng dành cho đo lường và phép tính decimal dành cho tiền.

### Phản ví dụ và ngộ nhận cần tránh

Không tạo Decimal trực tiếp từ float rồi cho rằng giá trị gốc đã chính xác: Decimal(0.1) phản ánh giá trị float gần 0.1, không phải chuỗi thập phân 0.1.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`B09.01_bai_tap_da_giai_v25.py`](MA_MAU/B09.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`B09.01_loi_giai.md`](LOI_GIAI/B09.01_loi_giai.md).
5. **Bài mở rộng:** Thử ROUND_HALF_EVEN thay ROUND_HALF_UP trên 1.005; trình bày quy tắc dùng trong hệ thống kế toán thực tế.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/decimal.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# B09.02 — Boolean logic và lỗi ranh giới

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B09 — Độ chính xác dữ liệu và sai lầm nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Boolean logic và lỗi ranh giới** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

## 2. Khái niệm và bản chất

Lỗi ranh giới (off-by-one) xuất hiện khi dùng `<` thay cho `<=`, hoặc lẫn khoảng đóng/mở trong điều kiện và range. Python hỗ trợ chained comparisons `0 <= x <= 100`, giúp diễn đạt mạch lạc, nhưng vẫn phải quyết định rõ đầu/cuối được chấp nhận.

## 3. Cơ chế hoạt động từng bước

Lập bảng kiểm thử với ngưỡng-1, ngưỡng, ngưỡng+1 trước khi viết hàm. Tách việc kiểm tra miền giá trị với logic nghiệp vụ xử lý dữ liệu đã hợp lệ.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def du_tuoi(tuoi):
    return tuoi >= 18
for age in (17, 18, 19):
    print(age, du_tuoi(age))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
17 False
18 True
19 True
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không kiểm thử duy nhất một trường hợp “đẹp” bên trong miền, vì điều đó bỏ sót hầu hết lỗi biên.
- **Tình huống biên:** Các giá trị ngoài miền, NaN hoặc kiểu không tương thích cần đặc tả riêng.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

`range(10,20)` lấy 10 đến 19 đối với step 1, giống điều kiện 10 <= n < 20 nếu n là số nguyên.

## 7. Bài tập thực hành

**Yêu cầu chính:** Tạo hàm `trong_doan(n)` trả True đúng khi 10 <= n < 20, và kiểm thử ở 9,10,19,20.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B09.02_loi_giai.md](LOI_GIAI/B09.02_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B09.02, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. `range(10,20)` lấy 10 đến 19 đối với step 1, giống điều kiện 10 <= n < 20 nếu n là số nguyên.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B09](https://docs.python.org/3.15/library/decimal.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Floating-point arithmetic: issues and limitations](https://docs.python.org/3.15/tutorial/floatingpoint.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


---

# B09.03 — Nhập dữ liệu không hợp lệ và kiểm tra

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B09 — Độ chính xác dữ liệu và sai lầm nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Nhập dữ liệu không hợp lệ và kiểm tra** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

## 2. Khái niệm và bản chất

Dữ liệu ngoài chương trình là không tin cậy cho tới khi được xác thực. Có ba bước: chuẩn hóa bề mặt (khoảng trắng), phân tích cú pháp (parse thành kiểu), xác minh ràng buộc nghiệp vụ. Sai cấu trúc và sai miền giá trị nên có thông báo phân biệt để người dùng sửa được.

## 3. Cơ chế hoạt động từng bước

`int(text)` có thể phát sinh ValueError; sau khi chuyển, vẫn phải kiểm tra số âm và giới hạn. Trong giao diện người dùng, có thể bọc try/except rồi yêu cầu nhập lại thay vì làm toàn chương trình dừng.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
def doc_so_luong(text):
    try:
        value = int(text.strip())
    except ValueError as exc:
        raise ValueError("phải nhập số nguyên") from exc
    if not 0 <= value <= 100:
        raise ValueError("ngoài [0, 100]")
    return value
print(doc_so_luong(" 12 "))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
12
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** Không dùng `except:` trống rồi âm thầm thay đầu vào lỗi bằng 0 vì che giấu sự cố và tạo quyết định nghiệp vụ sai.
- **Tình huống biên:** `int("1.0")` lỗi dù người đọc có thể coi là 1.0; không tự động làm tròn nếu chưa có yêu cầu.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Parsing trả lời “biểu diễn này thành kiểu gì?”; validation trả lời “giá trị này có được phép không?”.

## 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm chuyển một chuỗi điểm từ 0 tới 10 sang int, từ chối chuỗi rỗng, chữ và giá trị ngoài miền.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B09.03_loi_giai.md](LOI_GIAI/B09.03_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B09.03, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Parsing trả lời “biểu diễn này thành kiểu gì?”; validation trả lời “giá trị này có được phép không?”.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B09](https://docs.python.org/3.15/library/decimal.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Floating-point arithmetic: issues and limitations](https://docs.python.org/3.15/tutorial/floatingpoint.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


---

# B09.04 — Kiểm soát chuyển đổi kiểu và quy tắc làm tròn

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO — MÃ ĐÃ CHẠY PYTHON 3.13.5.
> **Giai đoạn:** GD1 · **Chương:** B09 — Độ chính xác dữ liệu và sai lầm nền tảng.
> **Chuẩn ngôn ngữ:** Python 3.15.2; mã tương thích đã chạy trên Python 3.13.5 nếu không được ghi khác.

## 1. Mục tiêu và điều kiện tiên quyết

- Mô tả bằng lời bản chất của **Kiểm soát chuyển đổi kiểu và quy tắc làm tròn** và nêu được một tình huống cần dùng.
- Dự đoán được kết quả của ví dụ trước khi chạy và giải thích mỗi bước.
- Hoàn thành bài tập tự làm, xử lý tình huống biên và so sánh với một cách làm dễ nhầm.
- **Tiên quyết:** A.

## 2. Khái niệm và bản chất

Chuyển đổi kiểu có mất mát thông tin: float → int bỏ phần lẻ; str → int yêu cầu chuỗi hợp lệ; Decimal → float có thể mất chính xác. Làm tròn là một chính sách riêng và phải phân biệt với chỉ hiển thị ít chữ số. `round` sử dụng cách làm tròn đến số chẵn gần nhất trong trường hợp hòa nhưng float có giới hạn biểu diễn.

## 3. Cơ chế hoạt động từng bước

Đặc tả độ chính xác, cách xử lý dữ liệu không hợp lệ, phép làm tròn, rồi kiểm thử quanh điểm nửa đơn vị; không dùng định dạng f-string làm dữ liệu để tính tiếp trừ khi có chủ ý.

## 4. Ví dụ tối thiểu và kết quả kiểm chứng

```python
from decimal import Decimal, ROUND_HALF_UP
x = Decimal("2.345")
print(x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
print(int(-2.9))
```

**Kết quả thực thi trên Python 3.13.5**:

```text
2.35
-2
```

Kiểm tra nhanh: chạy lại bằng lệnh `python <tên_tệp>.py` trong môi trường thực hành để đối chiếu.

## 5. Trường hợp biên, lỗi thường gặp và cách gỡ lỗi

- **Sai lầm thường gặp:** `f"{x:.2f}"` trả chuỗi, không đồng nghĩa thay đổi số gốc hay bảo đảm chính sách làm tròn nghiệp vụ.
- **Tình huống biên:** Làm tròn số âm theo HALF_UP là ra xa 0 khi đúng nửa đơn vị; cần ghi rõ yêu cầu.
- **Quy trình gỡ lỗi:** tái hiện bằng đầu vào tối giản → dự đoán tại từng dòng → đọc traceback từ dưới lên → tạo kiểm thử hồi quy sau sửa lỗi.

## 6. Phân biệt khái niệm dễ nhầm

Format để trình bày khác với quantize để tính/ghi giá trị đã làm tròn.

## 7. Bài tập thực hành

**Yêu cầu chính:** Viết hàm nhận chuỗi số và trả Decimal làm tròn một chữ số với ROUND_HALF_UP.

**Bài tập tự lực (chưa có đáp án):** Tạo ít nhất ba ca kiểm thử (bình thường, giá trị biên, dữ liệu sai hoặc không thuộc hợp đồng). Giải thích vì sao cách xử lý đúng hoặc cần chủ động báo lỗi. Viết thêm một ví dụ ứng dụng khác với ví dụ trên.

**Lời giải tham khảo:** [B09.04_loi_giai.md](LOI_GIAI/B09.04_loi_giai.md) — đọc sau khi tự làm.

## 8. Câu hỏi đánh giá

1. Nếu bỏ điều kiện hoặc thay đổi bước xử lý chủ chốt trong ví dụ B09.04, điều gì thay đổi?
2. Tại sao một trường hợp chạy không báo lỗi vẫn có thể không đáp ứng hợp đồng của bài toán?
3. Format để trình bày khác với quantize để tính/ghi giá trị đã làm tròn.

## 9. Tiêu chí hoàn thành

- [ ] Giải thích được cơ chế mà không nhìn tài liệu.
- [ ] Dự đoán đúng mã ví dụ, chạy và ghi lại phiên bản Python.
- [ ] Viết được một lời giải riêng, không sao chép file đáp án.
- [ ] Tạo và giải thích được ít nhất ba ca kiểm thử.
- [ ] Nêu được giới hạn, phản ví dụ và quy tắc lựa chọn phù hợp.

## 10. Nguồn chính thức và nguồn bổ sung

- [Python 3.15: tài liệu chính thức cho B09](https://docs.python.org/3.15/library/decimal.html)
- [Python 3.15: What’s New](https://docs.python.org/3.15/whatsnew/3.15.html)
- [Floating-point arithmetic: issues and limitations](https://docs.python.org/3.15/tutorial/floatingpoint.html)

**Nguồn gốc biên soạn:** giải thích, bài tập và đáp án do giáo trình tự biên soạn; các quy tắc ngôn ngữ tham chiếu Python Docs. Sách PDF đã cung cấp dùng để đối chiếu nền tảng, không sao chép nguyên văn.

**Giới hạn chất lượng:** Chưa thực hiện vòng đánh giá sư phạm độc lập; Python 3.15.2 chưa có trong môi trường kiểm thử hiện tại.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: B09.01, B09.02, B09.03, B09.04. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
