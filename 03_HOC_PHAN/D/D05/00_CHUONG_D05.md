# Chương D05 — Thiết kế hàm/API

> **Giai đoạn:** GD2 · **Học phần:** Hàm và mô hình lập trình nâng cao  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương D05: Thiết kế hàm/API, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Chữ ký hàm và keyword-only; Tính dễ kiểm thử, tái sử dụng và tài liệu hóa.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [D05.01 — Chữ ký hàm và keyword-only](BAI_HOC/D05.01.md)
- [D05.02 — Hợp đồng đầu vào/đầu ra và lỗi](BAI_HOC/D05.02.md)
- [D05.03 — Tính dễ kiểm thử, tái sử dụng và tài liệu hóa](BAI_HOC/D05.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)
- [R10: Python typing specification](https://typing.python.org/en/latest/spec/)
- [R19: mypy Documentation](https://mypy.readthedocs.io/en/stable/)

---

## D05.01 — Chữ ký hàm và keyword-only

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D05 — Thiết kế hàm/API · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Chữ ký hàm và keyword-only**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Chữ ký hàm** thể hiện tham số positional-only (`/`), positional-or-keyword, keyword-only (`*`), varargs và kiểu giá trị mặc định. Keyword-only hữu ích để API nhiều tham số tùy chọn khó bị đảo vị trí.

### 3. Nguyên lý và cơ chế từng bước

`giam_gia(gia, *, ty_le)` yêu cầu ty_le được truyền theo tên. Dấu `*` không có nghĩa là phép nhân trong chữ ký.

### 4. Ví dụ tối thiểu có thể chạy

```python
def gia_sau_giam(gia: float, *, ty_le: float=0.1) -> float:
    if not 0 <= ty_le <= 1: raise ValueError('ty_le phải từ 0 đến 1')
    return gia * (1 - ty_le)
assert gia_sau_giam(100, ty_le=0.2)==80.0
print(gia_sau_giam(100))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
90.0
```

**Thực hành:** chạy file `07_MA_VI_DU/D05.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Giá trị mặc định mutable như `[]` được tạo khi định nghĩa, không phải mỗi lần gọi; dùng None sentinel phù hợp.
- **Trường hợp biên:** Thay đổi vị trí tham số trong public API có thể phá vỡ mã gọi cũ dù tên hàm vẫn như cũ.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Chọn keyword-only cho options mơ hồ hoặc dễ truyền nhầm vị trí.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo API `thanh_tien(gia, so_luong, *, phi=0)` và ca test phi âm theo hợp đồng tự chọn.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D05.01_loi_giai.md](LOI_GIAI/D05.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Chữ ký hàm và keyword-only** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## D05.02 — Hợp đồng đầu vào/đầu ra và lỗi

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D05 — Thiết kế hàm/API · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Hợp đồng đầu vào/đầu ra và lỗi**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

**Hợp đồng hàm** (contract) mô tả tiền điều kiện, hậu điều kiện và hành vi lỗi. Type hint chỉ phản ánh một phần hợp đồng; hợp đồng còn nêu miền giá trị, tác dụng phụ, tính xác định và cách xử lý dữ liệu sai.

### 3. Nguyên lý và cơ chế từng bước

Hàm chia yêu cầu mẫu khác 0. Không lặng lẽ trả 0 khi mẫu bằng 0, vì như vậy che giấu sai dữ liệu.

### 4. Ví dụ tối thiểu có thể chạy

```python
def ty_le(tu: float, mau: float) -> float:
    if mau == 0: raise ValueError('mẫu phải khác 0')
    return tu / mau
assert ty_le(4,2)==2.0
try:ty_le(1,0)
except ValueError: pass
else: raise AssertionError('thiếu tiền điều kiện')
print(ty_le(9,3))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
3.0
```

**Thực hành:** chạy file `07_MA_VI_DU/D05.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không nhầm lỗi kỹ thuật với lỗi nghiệp vụ: `ZeroDivisionError` mặc định ít giải thích hơn ValueError có thông điệp hợp đồng.
- **Trường hợp biên:** Nếu dùng số thực so sánh bằng 0 rất sát 0, cần đánh giá độ ổn định số theo yêu cầu miền.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Viết contract trước để tạo test có ý nghĩa hơn chỉ chạy theo dòng code.

### 7. Bài tập có yêu cầu kiểm chứng

Đặc tả và triển khai hàm tính tỷ suất lợi nhuận; viết test input bình thường, mẫu 0 và số âm.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D05.02_loi_giai.md](LOI_GIAI/D05.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Hợp đồng đầu vào/đầu ra và lỗi** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

## D05.03 — Tính dễ kiểm thử, tái sử dụng và tài liệu hóa

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** D05 — Thiết kế hàm/API · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Tính dễ kiểm thử, tái sử dụng và tài liệu hóa**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Thiết kế hàm để dễ kiểm thử dựa trên đầu vào/đầu ra rõ, phụ thuộc được truyền từ ngoài, tác dụng phụ có kiểm soát và tài liệu mô tả trường hợp lỗi. Hàm thuần có cùng input sẽ trả cùng output và không đổi trạng thái ngoài.

### 3. Nguyên lý và cơ chế từng bước

`tao_thong_bao` nhận thời điểm từ tham số thay vì tự gọi đồng hồ. Nhờ vậy test xác định và không cần mock thời gian.

### 4. Ví dụ tối thiểu có thể chạy

```python
def tao_thong_bao(ten: str, ngay: str) -> str:
    return f'{ngay}: Xin chào {ten.strip()}'
assert tao_thong_bao(' An ','02/11') == '02/11: Xin chào An'
print(tao_thong_bao('Binh','03/11'))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
03/11: Xin chào Binh
```

**Thực hành:** chạy file `07_MA_VI_DU/D05.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Đọc file hoặc gọi API trong hàm biến đổi khiến unit test lệ thuộc môi trường và khó tái hiện.
- **Trường hợp biên:** Dependency injection nên tối giản; không tạo hàng chục lớp trừ khi thực sự có nhiều chiến lược kiểm thử.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Ưu tiên chức năng nhỏ có một trách nhiệm, nhưng không tách hàm thành vụn vặt không có lợi ích bảo trì.

### 7. Bài tập có yêu cầu kiểm chứng

Tách chức năng đọc file khỏi logic lọc điểm; viết hàm thuần lọc điểm >= ngưỡng.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [D05.03_loi_giai.md](LOI_GIAI/D05.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Tính dễ kiểm thử, tái sử dụng và tài liệu hóa** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

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

Đã cập nhật file bài lẻ: D05.01, D05.02, D05.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
