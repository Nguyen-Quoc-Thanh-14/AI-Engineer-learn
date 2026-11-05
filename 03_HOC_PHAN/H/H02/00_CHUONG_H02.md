# Chương H02

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# H02.01 — Arrange-Act-Assert và test case

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** H02 — Kiểm thử cơ bản · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Arrange-Act-Assert và test case**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, F01.

## 2. Khái niệm — Bản chất

Arrange-Act-Assert chia test thành thiết lập dữ liệu, gọi hành vi và xác nhận kết quả. Test tốt phát hiện lỗi khi quy tắc nghiệp vụ thay đổi, không chỉ xác nhận ví dụ hạnh phúc.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
def tinh_thanh_tien(gia,sl):
    if min(gia,sl)<0:raise ValueError()
    return gia*sl
# Arrange
gia,so_luong=100,2
# Act
actual=tinh_thanh_tien(gia,so_luong)
# Assert
assert actual==200
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/H02.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** `assert x` mơ hồ hơn `assert x == expected` trong nhiều test; pytest hiển thị rõ khác biệt.
- **Trường hợp biên:** Không dựa vào thứ tự chạy test; mỗi test nên độc lập.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Viết test cho chức năng trừ hàng tồn kho gồm ca thường, số lượng 0 và âm.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [H02.01_loi_giai.md](LOI_GIAI/H02.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Arrange-Act-Assert và test case** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R16] [pytest Documentation](https://docs.pytest.org/en/stable/) — Chính thức thư viện.
- [R17] [Hypothesis Documentation](https://hypothesis.readthedocs.io/en/latest/) — Chính thức thư viện.
- [R18] [Ruff Documentation](https://docs.astral.sh/ruff/) — Chính thức thư viện.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Arrange–Act–Assert tách chuẩn bị dữ liệu, thao tác và kiểm tra kỳ vọng; ca thử tốt mô tả hợp đồng, không chỉ gọi hàm rồi không kiểm tra gì.

### Cách suy luận và thiết kế lời giải

Đặt kiểm thử trong unittest, mỗi ca có tên nêu tình huống; ca sai kiểu kiểm tra ngoại lệ chính xác. Khi thay đổi logic normalize_username, các test trở thành regression suite giúp phát hiện thay đổi hành vi.

### Phản ví dụ và ngộ nhận cần tránh

Đừng dùng `try: ... except Exception: pass` khi cần kiểm thử ngoại lệ vì có thể che lỗi không liên quan; hãy dùng assertRaises với đúng loại lỗi.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`H02.01_bai_tap_da_giai_v25.py`](MA_MAU/H02.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`H02.01_loi_giai.md`](LOI_GIAI/H02.01_loi_giai.md).
5. **Bài mở rộng:** Tạo thêm test cho Unicode casefold (ví dụ một tên tiếng Đức) và so sánh với `.lower()`; xác định hợp đồng của hệ thống tài khoản trước khi áp dụng.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/unittest.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# H02.02 — unittest và pytest

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** H02 — Kiểm thử cơ bản · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **unittest và pytest**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, F01.

## 2. Khái niệm — Bản chất

unittest có trong standard library; pytest là công cụ ngoài. Test discovery chạy hàm/method theo quy ước; `pytest` dùng assert expression và fixtures khi cài đặt.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+3,5)
case=TestMath('test_add')
res=unittest.TestResult(); case.run(res)
assert res.wasSuccessful()
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/H02.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Test không được cho luôn pass vì quên lệnh assert; có thể kiểm tra bằng deliberately breaking implementation.
- **Trường hợp biên:** Chưa cài pytest không có nghĩa unittest không chạy được.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Viết một unittest.TestCase kiểm tra hàm nhân; nêu cách chạy `python -m unittest`.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [H02.02_loi_giai.md](LOI_GIAI/H02.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **unittest và pytest** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R16] [pytest Documentation](https://docs.pytest.org/en/stable/) — Chính thức thư viện.
- [R17] [Hypothesis Documentation](https://hypothesis.readthedocs.io/en/latest/) — Chính thức thư viện.
- [R18] [Ruff Documentation](https://docs.astral.sh/ruff/) — Chính thức thư viện.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# H02.03 — Boundary cases và regression tests

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** H02 — Kiểm thử cơ bản · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Boundary cases và regression tests**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, F01.

## 2. Khái niệm — Bản chất

Boundary testing thử sát ranh giới hợp đồng, regression testing lưu một trường hợp từng phát hiện lỗi để ngăn lỗi quay lại. Test đáng tin cậy kiểm tra cả đầu vào sai.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
def is_adult(age):
    if not isinstance(age,int) or isinstance(age,bool):raise TypeError()
    if age<0: raise ValueError()
    return age>=18
assert not is_adult(17)
assert is_adult(18)
assert is_adult(19)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/H02.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Chỉ test 5, 6 với điểm 0..10 không đánh giá được ranh giới.
- **Trường hợp biên:** Một test regression có thể trở thành lỗi thời nếu đặc tả thay đổi; sửa test cùng đặc tả.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Viết test 0, 1, max, max+1 cho hàm nhận điểm 0..10.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [H02.03_loi_giai.md](LOI_GIAI/H02.03_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Boundary cases và regression tests** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R16] [pytest Documentation](https://docs.pytest.org/en/stable/) — Chính thức thư viện.
- [R17] [Hypothesis Documentation](https://hypothesis.readthedocs.io/en/latest/) — Chính thức thư viện.
- [R18] [Ruff Documentation](https://docs.astral.sh/ruff/) — Chính thức thư viện.
- [R19] [mypy Documentation](https://mypy.readthedocs.io/en/stable/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: H02.01, H02.02, H02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
