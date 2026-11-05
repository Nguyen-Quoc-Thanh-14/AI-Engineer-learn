# Chương I01 — Phân tích thuật toán

> **Giai đoạn:** GD4 · **Học phần:** Thuật toán và cấu trúc dữ liệu chuyên sâu  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương I01: Phân tích thuật toán, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Big-O, Big-Theta và Big-Omega; Amortized analysis nhập môn.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [I01.01 — Big-O, Big-Theta và Big-Omega](BAI_HOC/I01.01.md)
- [I01.02 — Time-space tradeoff](BAI_HOC/I01.02.md)
- [I01.03 — Amortized analysis nhập môn](BAI_HOC/I01.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- [R22: MIT OCW Introduction to Algorithms](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)

---

## I01.01 — Big-O, Big-Theta và Big-Omega

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** I01 — Phân tích thuật toán · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Big-O, Big-Theta và Big-Omega**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Độ phức tạp tiệm cận** mô tả tốc độ tăng của lượng tài nguyên theo kích thước đầu vào, không trực tiếp cho biết thời gian chạy tính bằng giây. Với hàm không âm, Big-O biểu diễn cận trên tiệm cận; Big-Omega là cận dưới; Big-Theta là cận chặt cả hai phía. Khi nói một thao tác `O(n)`, cần nói rõ mô hình chi phí và biến n. Một thuật toán O(n) có thể chậm hơn O(n log n) trên đầu vào nhỏ.

### 3. Nguyên lý và cơ chế từng bước

Với `sum(xs)`, vòng duyệt đọc mỗi phần tử một lần, nên thời gian là Θ(n) trong mô hình chi phí số học hằng số; không gian phụ trợ ngoài đầu vào thường O(1). Một list copy tốn O(n) bộ nhớ. Phân biệt worst-case, average-case, amortized và số phép toán thực tế.

### 4. Ví dụ tối thiểu có thể chạy

```python
def tong(xs):
    total = 0
    for x in xs:
        total += x
    return total
assert tong([])==0
assert tong([2,3,5])==10
print(tong([2,3,5]))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
10
```

**Thực hành:** chạy file `07_MA_VI_DU/I01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không viết O(1) chỉ vì một lệnh Python: bên trong lệnh có thể có vòng lặp hoặc độ dài dữ liệu.
- **Trường hợp biên:** Tính với số nguyên lớn không còn giả định chi phí phép cộng là hằng số theo số bit.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng phân tích tiệm cận để chọn hướng giải trước khi tối ưu; đo hiệu năng thực tế ở bước sau.

### 7. Bài tập có yêu cầu kiểm chứng

So sánh độ phức tạp thời gian và không gian của hàm cộng dồn và `list(reversed(xs))`; giải thích lý do.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [I01.01_loi_giai.md](LOI_GIAI/I01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Big-O, Big-Theta và Big-Omega** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R22] [MIT OCW Introduction to Algorithms](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/) — Giáo dục học thuật.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## I01.02 — Time-space tradeoff

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** I01 — Phân tích thuật toán · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Time-space tradeoff**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Time–space tradeoff** là lựa chọn sử dụng thêm bộ nhớ để giảm số phép tính hoặc ngược lại. Một set hỗ trợ membership kiểm tra trung bình gần O(1) nhưng phải trả chi phí xây dựng và lưu trữ; duyệt list là O(n) trong trường hợp xấu với ít bộ nhớ phụ trợ hơn.

### 3. Nguyên lý và cơ chế từng bước

Nếu cần nhiều lần tìm kiếm trong cùng tập giá trị, chuyển từ list sang set một lần thường có lợi. Nếu chỉ tìm một lần trên vài phần tử, chi phí tạo set có thể lớn hơn lợi ích. Luôn giữ nguyên ý nghĩa dữ liệu: set bỏ trùng và không giữ thứ tự theo giao diện sequence.

### 4. Ví dụ tối thiểu có thể chạy

```python
values=[2,3,5,7,11]
queries=[3,4,5]
lookup=set(values)
assert [q in values for q in queries]==[q in lookup for q in queries]
print([q in lookup for q in queries])
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
[True, False, True]
```

**Thực hành:** chạy file `07_MA_VI_DU/I01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không biến mọi list thành set: có thể cần phần tử trùng hoặc thứ tự xuất hiện.
- **Trường hợp biên:** Các giá trị unhashable như list không thể đưa trực tiếp vào set.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Cân nhắc cả chi phí chuyển đổi và ngữ nghĩa, không chỉ Big-O.

### 7. Bài tập có yêu cầu kiểm chứng

Giải thích 2 trường hợp nên dùng list, 2 trường hợp nên dùng set khi kiểm tra membership.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [I01.02_loi_giai.md](LOI_GIAI/I01.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Time-space tradeoff** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R22] [MIT OCW Introduction to Algorithms](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/) — Giáo dục học thuật.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## I01.03 — Amortized analysis nhập môn

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** I01 — Phân tích thuật toán · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Amortized analysis nhập môn**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Amortized analysis** xét tổng chi phí của một dãy thao tác, không bảo đảm mỗi thao tác đều rẻ. Với dynamic array, đôi khi append cần cấp phát và sao chép vùng chứa, nhưng tổng chi phí tăng dần thường dẫn tới chi phí trung bình phân bổ O(1) cho một lần append theo mô hình lý thuyết.

### 3. Nguyên lý và cơ chế từng bước

Xét chiến lược nhân đôi dung lượng: các lần sao chép xảy ra ở kích thước 1,2,4,... Tổng số phần tử từng sao chép nhỏ hơn khoảng 2n cho n lần chèn; do đó tổng O(n), trung bình O(1). Đây là phân tích mô hình, không phải lời hứa về số lần realloc cụ thể của CPython.

### 4. Ví dụ tối thiểu có thể chạy

```python
def so_phan_tu_duoc_sao_chep(n):
    capacity=1; copies=0
    for length in range(n):
        if length==capacity:
            copies+=length
            capacity*=2
    return copies
assert so_phan_tu_duoc_sao_chep(1)==0
assert so_phan_tu_duoc_sao_chep(8)<2*8
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/I01.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không diễn giải amortized O(1) là mọi append đều thực hiện trong thời gian bằng nhau.
- **Trường hợp biên:** Chiến lược thực tế của list CPython khác mô hình nhân đôi đơn giản.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng amortized analysis khi thao tác thỉnh thoảng đắt nhưng ít xảy ra.

### 7. Bài tập có yêu cầu kiểm chứng

Chứng minh vì sao tổng chi phí sao chép theo chiến lược nhân đôi là O(n).

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [I01.03_loi_giai.md](LOI_GIAI/I01.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Amortized analysis nhập môn** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R22] [MIT OCW Introduction to Algorithms](https://www.ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/) — Giáo dục học thuật.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: I01.01, I01.02, I01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
