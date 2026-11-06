# Chương G01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# G01.01 — open, read, write

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** G01 — Hệ thống tệp · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **open, read, write**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

## 2. Khái niệm — Bản chất

`open()` trả về file object, và `with` bảo đảm gọi phương thức thoát scope để giải phóng tài nguyên kể cả khi exception xảy ra. `encoding` cần được chỉ rõ khi yêu cầu truyền tệp qua nhiều môi trường.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
from io import StringIO
with StringIO('dòng 1\n') as f:
    assert f.readline()=='dòng 1\n'
print('đóng')
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
đóng
```

**Thực hành:** chạy file `07_MA_VI_DU/G01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `f.read()` cho file khổng lồ khi có thể streaming.
- **Trường hợp biên:** File object có thể ném OSError do quyền, đĩa đầy, hoặc thay đổi filesystem.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Dùng pathlib + tempfile ghi và đọc text UTF-8 với with.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [G01.01_loi_giai.md](LOI_GIAI/G01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **open, read, write** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Mở tệp qua context manager đảm bảo đóng tài nguyên ngay cả khi có ngoại lệ; encoding là phần hợp đồng của file văn bản, không nên phụ thuộc hệ điều hành.

### Cách suy luận và thiết kế lời giải

Sử dụng Path và open(encoding="utf-8") để ghi và đọc. Tách hàm ghi/đọc làm hai bước cho phép kiểm thử riêng; pathlib.Path thực hiện ánh xạ đường dẫn mà không tự tạo các thư mục cha.

### Phản ví dụ và ngộ nhận cần tránh

Không dùng `open(..., "w")` trên đường dẫn chưa kiểm tra trong hệ thống quan trọng: chế độ w sẽ cắt dữ liệu cũ. Khi ghi dữ liệu cần tính atomicity, hãy cân nhắc ghi tệp tạm và os.replace.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`G01.01_bai_tap_da_giai_v25.py`](MA_MAU/G01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`G01.01_loi_giai.md`](LOI_GIAI/G01.01_loi_giai.md).
5. **Bài mở rộng:** Viết bản atomic write bằng NamedTemporaryFile cùng thư mục đích; kiểm thử việc thay nội dung khi một bước ghi có lỗi.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/tutorial/inputoutput.html#reading-and-writing-files. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# G01.02 — with và context manager nhập môn

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD2 · **Chương:** G01 — Hệ thống tệp · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **with và context manager nhập môn**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

## 2. Khái niệm — Bản chất

`pathlib.Path` mô tả đường dẫn độc lập với chuỗi ghép tay. Với path do người dùng cung cấp, cần xác định trust boundary; thao tác normalize không tự bảo đảm chặn path traversal.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
from pathlib import Path
p=Path('du_lieu')/'report.csv'
assert p.suffix=='.csv'
print(p.name)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
report.csv
```

**Thực hành:** chạy file `07_MA_VI_DU/G01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Chặn `..` trong chuỗi chưa đủ chống symlink TOCTOU cho hệ thống nhạy cảm.
- **Trường hợp biên:** Path.resolve() có thể phát sinh lỗi với môi trường hoặc đường dẫn không tồn tại.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Viết hàm chỉ nhận tên tệp không có đường dẫn và kiểm thử `../secret` bị từ chối.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [G01.02_loi_giai.md](LOI_GIAI/G01.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **with và context manager nhập môn** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [S02] Python for Data Analysis — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R07] [What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html) — Chính thức.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# G01.03 — pathlib, đường dẫn và filesystem errors

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD2 · **Chương:** G01 — Hệ thống tệp · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** B, C. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **pathlib, đường dẫn và filesystem errors** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

`pathlib.Path` biểu diễn đường dẫn theo OS; `resolve()` thường chuẩn hóa đường dẫn tuyệt đối và xử lý symlink theo quy tắc môi trường.

**Ngữ cảnh thực tế:** Trong chương **Hệ thống tệp**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Tách thao tác dựng đường dẫn với thao tác đọc/ghi; luôn chuẩn bị cho FileNotFoundError, PermissionError, IsADirectoryError.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as d:
    p = Path(d) / 'item.txt'
    p.write_text('abc', encoding='utf-8')
    assert p.read_text(encoding='utf-8') == 'abc'
    assert p.is_file()
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`G01.03_demo.py`](MA_MAU/G01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Nối đường dẫn do người dùng cung cấp với thư mục gốc mà không kiểm tra có thể tạo path traversal.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tạo hàm chỉ đọc file đuôi `.txt` trong thư mục tạm, tránh đi ra ngoài root.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_G01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/G01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- S02: Python for Data Analysis (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R07: What’s New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: G01.01, G01.02. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
