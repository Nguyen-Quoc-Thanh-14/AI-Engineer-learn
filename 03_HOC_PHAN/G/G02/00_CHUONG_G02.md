# Chương G02 — Văn bản và dữ liệu nhị phân

> **Giai đoạn:** GD2 · **Học phần:** Tệp, Unicode và tuần tự hóa  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương G02: Văn bản và dữ liệu nhị phân, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: bytes, str và encoding; Binary I/O và format dữ liệu.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [G02.01 — bytes, str và encoding](BAI_HOC/G02.01.md)
- [G02.02 — UTF-8, newline và decode errors](BAI_HOC/G02.02.md)
- [G02.03 — Binary I/O và format dữ liệu](BAI_HOC/G02.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## G02.01 — bytes, str và encoding

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** G02 — Văn bản và dữ liệu nhị phân · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **bytes, str và encoding**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

`str` là chuỗi ký tự Unicode; `bytes` là chuỗi byte. Encoding biến str thành bytes, decoding biến bytes thành str; không mặc nhiên 1 ký tự ứng với 1 byte trong UTF-8.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
text='Tiếng Việt'
raw=text.encode('utf-8')
assert raw.decode('utf-8')==text
assert len(raw)>len(text)
print(len(text),len(raw))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
10 14
```

**Thực hành:** chạy file `07_MA_VI_DU/G02.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không sử dụng len(bytes) để suy ra số ký tự của chuỗi gốc.
- **Trường hợp biên:** UTF-8 decode có thể thất bại nếu chuỗi byte bị hỏng.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Viết hàm nhận bytes UTF-8 và trả về str, xử lý dữ liệu không hợp lệ bằng ngoại lệ rõ.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [G02.01_loi_giai.md](LOI_GIAI/G02.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **bytes, str và encoding** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## G02.02 — UTF-8, newline và decode errors

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** G02 — Văn bản và dữ liệu nhị phân · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **UTF-8, newline và decode errors**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

UTF-8 là encoding mặc định cho nhiều text I/O trong Python 3.15; để code rõ ràng giữa phiên bản, khai báo encoding. `newline` liên quan đến biểu diễn kết thúc dòng và CSV.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
from io import TextIOWrapper,BytesIO
b=BytesIO('xin chào\n'.encode('utf-8'))
f=TextIOWrapper(b,encoding='utf-8')
assert f.readline()=='xin chào\n'
print('ok')
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
ok
```

**Thực hành:** chạy file `07_MA_VI_DU/G02.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** errors="ignore" có thể lặng lẽ mất dữ liệu nên không dùng nếu yêu cầu toàn vẹn.
- **Trường hợp biên:** Khác biệt newline giữa hệ điều hành có thể làm test byte-by-byte sai.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Viết hàm decode strict rồi tạo test bytes lỗi và giải thích errors="replace" khác strict.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [G02.02_loi_giai.md](LOI_GIAI/G02.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **UTF-8, newline và decode errors** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## G02.03 — Binary I/O và format dữ liệu

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD2 · **Chương:** G02 — Văn bản và dữ liệu nhị phân · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** B, C. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Binary I/O và format dữ liệu** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Với binary I/O, byte sequence không mang ý nghĩa encoding; file format quyết định cách diễn giải byte.

**Ngữ cảnh thực tế:** Trong chương **Văn bản và dữ liệu nhị phân**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

`open(path, "rb")` trả bytes; `struct` mã hóa số theo endianness/size xác định; luôn xác thực độ dài dữ liệu trước unpack.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
import struct
encoded = struct.pack('>HI', 7, 500)
assert len(encoded) == 6
assert struct.unpack('>HI', encoded) == (7, 500)
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`G02.03_demo.py`](MA_MAU/G02.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không dùng `.decode()` cho ảnh/file nén; không đoán format chỉ bằng phần mở rộng.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Định nghĩa header phiên bản 2 bytes, payload length 4 bytes, thử gói và giải gói.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_G02_03.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/G02.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: G02.01, G02.02, G02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
