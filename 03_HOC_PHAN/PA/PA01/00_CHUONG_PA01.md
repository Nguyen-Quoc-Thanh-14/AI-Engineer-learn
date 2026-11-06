# Chương PA01 — Tệp và công việc văn phòng

> **Giai đoạn:** GD6 · **Học phần:** Tự động hóa và scripting  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương PA01: Tệp và công việc văn phòng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Tự động xử lý thư mục; Thiết kế CLI nhỏ.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [PA01.01 — Tự động xử lý thư mục](BAI_HOC/PA01.01.md)
- [PA01.02 — CSV, JSON và tài liệu văn phòng](BAI_HOC/PA01.02.md)
- [PA01.03 — Thiết kế CLI nhỏ](BAI_HOC/PA01.03.md)

## Tiên quyết

F, G, H, M02

## Nguồn đối chiếu

- S01: Python Crash Course
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R11: Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [R20: uv Documentation](https://docs.astral.sh/uv/)

---

## PA01.01 — Tự động xử lý thư mục

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PA01 — Tệp và công việc văn phòng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Tự động xử lý thư mục**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** F, G, H, M02.

### 2. Khái niệm — Bản chất

Tự động hóa thư mục gồm: duyệt đầu vào, phân loại, tạo kế hoạch thay đổi, chạy dry-run, ghi log và chỉ thực thi thay đổi sau khi kiểm tra. Không đổi/xóa file hàng loạt khi chưa có backup hoặc chiến lược rollback.

### 3. Nguyên lý và cơ chế từng bước

Dùng `TemporaryDirectory()` tạo dữ liệu giả. `Path.iterdir()` không bảo đảm thứ tự nên `sorted()` nếu thứ tự cần ổn định. Ví dụ đếm loại tệp mà không đụng vào thư mục thật.

### 4. Ví dụ tối thiểu có thể chạy

```python
from tempfile import TemporaryDirectory
from pathlib import Path
with TemporaryDirectory() as d:
    p=Path(d)
    (p/'a.txt').write_text('a')
    (p/'b.csv').write_text('x,y')
    counts={ext:sum(x.suffix==ext for x in p.iterdir()) for ext in ['.txt','.csv']}
    assert counts=={'.txt':1,'.csv':1}
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/PA01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không dùng `rglob('*')` rồi xóa tự động các file không rõ nguồn gốc.
- **Trường hợp biên:** Symlink, quyền truy cập và tên trùng có thể làm thao tác rename thất bại.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

Tự động hóa tốt phải idempotent hoặc có cơ chế phát hiện thực thi lại.

### 7. Bài tập có yêu cầu kiểm chứng

Viết trình quét đếm file theo suffix, bổ sung dry-run trước khi đổi tên.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PA01.01_loi_giai.md](LOI_GIAI/PA01.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Tự động xử lý thư mục** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R11] [Python Packaging User Guide](https://packaging.python.org/en/latest/) — Gốc.
- [R20] [uv Documentation](https://docs.astral.sh/uv/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## PA01.02 — CSV, JSON và tài liệu văn phòng

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PA01 — Tệp và công việc văn phòng · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** F, G, H, M02. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **CSV, JSON và tài liệu văn phòng** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

Automation dữ liệu dùng CSV/JSON với schema rõ; tài liệu văn phòng cần xử lý encoding và dung lượng.

**Ngữ cảnh thực tế:** Trong chương **Tệp và công việc văn phòng**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Parse → validate → transform → serialize; ghi atomically khi ghi file quan trọng.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
import csv,io,json
rows=list(csv.DictReader(io.StringIO('name,qty\nAn,2\n')))
assert json.loads(json.dumps(rows))[0]['name']=='An'
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PA01.02_demo.py`](MA_MAU/PA01.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không tách CSV bằng split dấu phẩy vì có trường quoted.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết converter CSV→JSON có validate qty số nguyên.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PA01_02.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PA01.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R11: Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [R20: uv Documentation](https://docs.astral.sh/uv/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## PA01.03 — Thiết kế CLI nhỏ

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PA01 — Tệp và công việc văn phòng · **Python đích:** CPython 3.15.2.

### 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** F, G, H, M02. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Thiết kế CLI nhỏ** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

### 2. Khái niệm và vì sao cần học

CLI tốt có `--help`, tham số hợp lệ và exit code; argparse xử lý phân tích đối số.

**Ngữ cảnh thực tế:** Trong chương **Tệp và công việc văn phòng**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

### 3. Cơ chế — mô hình thực thi

Tách parse args khỏi logic để test không cần terminal.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

### 4. Ví dụ độc lập, có assertion

```python
import argparse
p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=1)
assert p.parse_args(['--count','3']).count==3
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PA01.03_demo.py`](MA_MAU/PA01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

### 5. Trường hợp biên và lỗi thường gặp

Không ghi secrets vào argv nếu hệ thống có thể liệt kê process args.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

### 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tạo CLI `--input`, `--dry-run` và kiểm invalid option.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PA01_03.py`. Không viết `except: pass` để che lỗi.

### 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PA01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

### 8. Tài liệu kiểm chứng

- S01: Python Crash Course (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R11: Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [R20: uv Documentation](https://docs.astral.sh/uv/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: PA01.01. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.


## Bổ sung lời giải B độc lập — v2.8

- [PA01.02 — lời giải](LOI_GIAI/PA01.02_loi_giai.md)
- [PA01.03 — lời giải](LOI_GIAI/PA01.03_loi_giai.md)

Các lời giải chương trình và thiết kế có trạng thái nghiệm thu khác nhau; xem báo cáo v2.8.
