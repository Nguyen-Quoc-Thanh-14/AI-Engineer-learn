# Chương G04 — I/O thực tế

> **Giai đoạn:** GD2 · **Học phần:** Tệp, Unicode và tuần tự hóa  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương G04: I/O thực tế, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Dữ liệu lớn và đọc theo khối; ZIP, gzip và format nhị phân phổ biến.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [G04.01 — Dữ liệu lớn và đọc theo khối](BAI_HOC/G04.01.md)
- [G04.02 — Atomic write, temp file và xử lý lỗi](BAI_HOC/G04.02.md)
- [G04.03 — ZIP, gzip và format nhị phân phổ biến](BAI_HOC/G04.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- S01: Python Crash Course
- S02: Python for Data Analysis
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

---

## G04.01 — Dữ liệu lớn và đọc theo khối

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD2 · **Chương:** G04 — I/O thực tế · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** B, C. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Dữ liệu lớn và đọc theo khối** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Đọc streaming theo chunk giúp giới hạn bộ nhớ khi file rất lớn; chunk size ảnh hưởng số lần I/O, không có một kích thước tối ưu phổ quát.

**Ngữ cảnh thực tế:** Trong chương **I/O thực tế**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Lặp `read(BLOCK_SIZE)` cho tới EOF; cập nhật digest/tổng thay vì nạp cả file vào RAM.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
from io import BytesIO
stream = BytesIO(b'abcde')
chunks = []
while True:
    block = stream.read(2)
    if not block: break
    chunks.append(block)
assert chunks == [b'ab', b'cd', b'e']
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`G04.01_demo.py`](MA_MAU/G04.01_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không giả định `read(size)` luôn trả đủ size trên stream hoặc network.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết hàm SHA-256 đọc từng khối, kiểm tra file 0 byte và file kích thước không chia hết block.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_G04_01.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/G04.01_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## G04.02 — Atomic write, temp file và xử lý lỗi

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD2 · **Chương:** G04 — I/O thực tế · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** B, C. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Atomic write, temp file và xử lý lỗi** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Atomic write trên cùng filesystem thường dùng ghi tệp tạm rồi `os.replace`; giúp người đọc không nhìn thấy file nửa ghi.

**Ngữ cảnh thực tế:** Trong chương **I/O thực tế**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Ghi dữ liệu, flush và cân nhắc fsync theo yêu cầu độ bền; tên temp đặt cùng thư mục đích để tối đa khả năng atomic rename.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
import os, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    final = Path(d) / 'out.txt'
    tmp = Path(d) / 'tmp.txt'
    tmp.write_text('complete', encoding='utf-8')
    os.replace(tmp, final)
    assert final.read_text(encoding='utf-8') == 'complete'
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`G04.02_demo.py`](MA_MAU/G04.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Atomic replacement không đồng nghĩa durable commit khi mất điện; permission và symlink vẫn cần xem xét.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết hàm atomic_write_text dùng tempfile.NamedTemporaryFile cùng thư mục và dọn tệp khi lỗi.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_G04_02.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/G04.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## G04.03 — ZIP, gzip và format nhị phân phổ biến

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD2 · **Chương:** G04 — I/O thực tế · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** B, C. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **ZIP, gzip và format nhị phân phổ biến** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

ZIP là archive nhiều entry; gzip là luồng nén, thường một stream; không đồng nhất archive format và compression algorithm.

**Ngữ cảnh thực tế:** Trong chương **I/O thực tế**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Sử dụng `zipfile` và `gzip` trong stdlib; giới hạn tổng kích thước giải nén từ dữ liệu không tin cậy.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
import gzip, io, zipfile
x = b'hello' * 20
assert gzip.decompress(gzip.compress(x)) == x
bio = io.BytesIO()
with zipfile.ZipFile(bio, 'w') as z: z.writestr('a.txt', 'ok')
with zipfile.ZipFile(bio) as z: assert z.read('a.txt') == b'ok'
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`G04.03_demo.py`](MA_MAU/G04.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Zip slip và zip bomb: không giải nén archive chưa kiểm định đường dẫn/tài nguyên.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tạo ZIP bằng BytesIO với 2 file và so sánh danh sách entry sau đóng/mở.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_G04_03.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/G04.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: G04.01, G04.02, G04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
