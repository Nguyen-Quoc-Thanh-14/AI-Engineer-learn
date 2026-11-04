# Chương D01 — Hàm là đối tượng

> **Giai đoạn:** GD2 · **Học phần:** Hàm và mô hình lập trình nâng cao  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương D01: Hàm là đối tượng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: First-class functions và callback; Closure và ứng dụng.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [D01.01 — First-class functions và callback](BAI_HOC/D01.01.md)
- [D01.02 — Higher-order function, map và filter](BAI_HOC/D01.02.md)
- [D01.03 — Closure và ứng dụng](BAI_HOC/D01.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)
- [R10: Python typing specification](https://typing.python.org/en/latest/spec/)
- [R19: mypy Documentation](https://mypy.readthedocs.io/en/stable/)

---

## D01.01 — First-class functions và callback

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D01 — Hàm là đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **First-class functions và callback**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Một **hàm là đối tượng hạng nhất** (first-class object): có thể gán cho tên, đặt vào cấu trúc dữ liệu, truyền làm đối số và trả về từ hàm khác. **Callback** là đối tượng callable mà một hàm khác sẽ gọi tại thời điểm do nó quyết định. Điều này cho phép tách phần *cố định* (quy trình xử lý) khỏi phần *biến đổi* (chính sách).

### 3. Nguyên lý và cơ chế từng bước

Hàm `xu_ly` nhận dữ liệu và một callback. Python liên kết tên `phep_bien_doi` tới cùng đối tượng hàm được truyền vào; khi chạy `phep_bien_doi(x)`, call expression mới thực thi callback. Việc chỉ viết `xu_ly([1, 2], nhan_doi)` **không** tự gọi `nhan_doi` trước khi truyền.

### 4. Ví dụ tối thiểu có thể chạy

```python
def xu_ly(du_lieu, phep_bien_doi):
    return [phep_bien_doi(x) for x in du_lieu]

def nhan_doi(x):
    return x * 2

assert xu_ly([2, 3], nhan_doi) == [4, 6]
assert xu_ly([], nhan_doi) == []
print(xu_ly([2, 3], nhan_doi))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
[4, 6]
```

**Thực hành:** chạy file `07_MA_VI_DU/D01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** `callback` có thể tạo side effect; quy trình sẽ khó kiểm thử nếu callback đổi trạng thái toàn cục hoặc truy cập mạng mà không kiểm soát.
- **Trường hợp biên:** Callback có thể ném ngoại lệ; giao diện cần xác định có chuyển tiếp lỗi hay xử lý cục bộ. Vòng lặp với đầu vào trống vẫn hợp lệ.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng callback để giảm rẽ nhánh khi cùng luồng xử lý có nhiều cách biến đổi; không cần callback nếu chỉ có một hành vi rõ ràng.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo hàm `ap_dung(gia_tri, xu_ly)` trả về kết quả gọi `xu_ly(gia_tri)`. Kiểm thử callback nhân ba và callback chuyển số thành chuỗi.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D01.01_loi_giai.md](LOI_GIAI/D01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **First-class functions và callback** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## D01.02 — Higher-order function, map và filter

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D01 — Hàm là đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Higher-order function, map và filter**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Higher-order function** là hàm nhận hàm khác, trả về hàm khác, hoặc cả hai. `map(func, iterable)` tạo iterator áp dụng hàm cho từng phần tử; `filter(predicate, iterable)` chỉ giữ giá trị có kết quả kiểm tra truthy. Cả hai xử lý lười; một comprehension thường dễ đọc hơn trong trường hợp đơn giản.

### 3. Nguyên lý và cơ chế từng bước

`map()` không tạo list ngay. `list(...)` buộc iterator phát sinh kết quả. Khi `filter` nhận predicate, nó gọi predicate theo từng giá trị trong lúc duyệt.

### 4. Ví dụ tối thiểu có thể chạy

```python
nums = [0, 1, 2, 3, 4]
ket_qua = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
assert ket_qua == [0, 4, 16]
print(ket_qua)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
[0, 4, 16]
```

**Thực hành:** chạy file `07_MA_VI_DU/D01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không đồng nhất iterator và list: in `map(...)` không in ra kết quả số học đã duyệt.
- **Trường hợp biên:** Một iterator đã tiêu thụ không thể tái duyệt tự động; muốn lặp lại cần tạo iterator mới hoặc vật hóa dữ liệu.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng higher-order functions nếu chính sách biến đổi phải là đối số; ưu tiên comprehension khi truyền đạt ý nghĩa rõ hơn.

### 7. Bài tập có yêu cầu kiểm chứng

Viết `tong_binh_phuong_so_le(ds)` bằng `filter` và `map`, sau đó so sánh với comprehension. Kiểm thử danh sách rỗng.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D01.02_loi_giai.md](LOI_GIAI/D01.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Higher-order function, map và filter** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## D01.03 — Closure và ứng dụng

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D01 — Hàm là đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Closure và ứng dụng**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Closure** là function object giữ được binding tới các biến tự do trong môi trường lexical nơi nó được định nghĩa. Hàm lồng nhau có thể đọc biến đó sau khi hàm ngoài kết thúc. Với `nonlocal`, có thể gán lại binding ở scope ngoài gần nhất.

### 3. Nguyên lý và cơ chế từng bước

Mỗi lời gọi `tao_bo_dem()` tạo một cell riêng cho `dem`. Hàm trả về giữ cell này, nên trạng thái của hai bộ đếm không bị trộn. `nonlocal dem` có nghĩa là phép gán cập nhật binding bên ngoài, không tạo tên cục bộ mới.

### 4. Ví dụ tối thiểu có thể chạy

```python
def tao_bo_dem():
    dem = 0
    def tang():
        nonlocal dem
        dem += 1
        return dem
    return tang

a, b = tao_bo_dem(), tao_bo_dem()
assert [a(), a(), b(), a()] == [1, 2, 1, 3]
print(a(), b())
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
4 2
```

**Thực hành:** chạy file `07_MA_VI_DU/D01.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Trong vòng lặp, closure thường giữ binding chứ không tự động chụp giá trị tại mỗi lượt. Đây là late binding, có thể xử lý bằng tham số mặc định khi phù hợp.
- **Trường hợp biên:** Nếu closure giữ tài nguyên lớn, đối tượng liên quan có thể không được giải phóng khi vẫn còn tham chiếu tới closure.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Dùng closure cho cấu hình cục bộ nhỏ; class thường rõ hơn khi cần nhiều thao tác trên trạng thái.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo `tao_bo_nhan(he_so)` trả về hàm nhân một số với `he_so`. Kiểm tra hệ số âm và 0.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D01.03_loi_giai.md](LOI_GIAI/D01.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Closure và ứng dụng** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.
- [R10] [Python typing specification](https://typing.python.org/en/latest/spec/) — Đặc tả.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: D01.01, D01.02, D01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
