# Chương N01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# N01.01 — Input validation và trust boundary

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** N01 — Bảo mật dữ liệu đầu vào · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Input validation và trust boundary**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** F, G, M.

## 2. Khái niệm — Bản chất

Trust boundary đánh dấu nơi dữ liệu đi từ miền kém tin cậy sang miền có quyền. Validate kiểu, độ dài, miền, tính nhất quán tại biên; sanitize chung chung không bảo đảm an toàn với mọi sink.

## 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

## 4. Ví dụ tối thiểu có thể chạy

```python
def limit_name(x):
    if not isinstance(x,str) or not 1<=len(x)<=20:
        raise ValueError('Tên không hợp lệ')
    return x
assert limit_name('An')=='An'
try:limit_name('')
except ValueError:pass
else:raise AssertionError()
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/N01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không biến dữ liệu đầu vào thành trusted chỉ vì người dùng ở nội bộ.
- **Trường hợp biên:** `float("nan")` khiến nhiều so sánh phạm vi đều False, cần kiểm tra isfinite.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

## 7. Bài tập có yêu cầu kiểm chứng

Thiết kế schema cho điểm số 0..10 và test NaN không được lọt.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [N01.01_loi_giai.md](LOI_GIAI/N01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Input validation và trust boundary** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R21] [OWASP Top 10](https://owasp.org/projects/top-ten) — Tiêu chuẩn cộng đồng.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R01] [Python 3.15.2 release](https://www.python.org/downloads/release/python-3152/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Trust boundary là ranh giới nơi dữ liệu từ nguồn không đáng tin được chuyển thành giá trị dùng trong hệ thống; kiểm tra cú pháp, miền và độ dài trước khi sử dụng.

### Cách suy luận và thiết kế lời giải

API parse_age nhận chuỗi ASCII digits 0..130, bỏ khoảng trắng đầu/cuối, từ chối mọi ký tự còn lại bằng fullmatch. Việc hợp đồng chỉ nhận chuỗi tránh tự động chấp nhận số thực hoặc bool ngoài dự kiến.

### Phản ví dụ và ngộ nhận cần tránh

Không dùng int() trên mọi dữ liệu rồi cho rằng đã đủ validation: chuỗi quá dài, định dạng bất ngờ hoặc giá trị ngoài miền vẫn là vấn đề.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`N01.01_bai_tap_da_giai_v25.py`](MA_MAU/N01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`N01.01_loi_giai.md`](LOI_GIAI/N01.01_loi_giai.md).
5. **Bài mở rộng:** Thêm giới hạn kích thước request và normalize dữ liệu nhập từ HTTP; phân biệt validation và escaping đầu ra theo từng ngữ cảnh.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/re.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# N01.02 — Injection, path traversal và command execution

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD4 · **Chương:** N01 — Bảo mật dữ liệu đầu vào · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Injection, path traversal và command execution**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** F, G, M.

## 2. Khái niệm — Bản chất

Trust boundary là ranh giới giữa dữ liệu chưa được tin cậy và hệ thống nội bộ. Input validation kiểm tra kiểu, phạm vi và ý nghĩa; không thể thay thế parameterized SQL hoặc escaping theo đúng ngữ cảnh đầu ra. Nguyên tắc allowlist chặt hơn blocklist các chuỗi nguy hiểm cụ thể.

## 3. Nguyên lý và cơ chế từng bước

Kiểm tra một mã định danh kinh doanh bằng regex `fullmatch`, từ chối giá trị không đúng định dạng. Validation nên được thực hiện gần nơi dữ liệu đi vào boundary; hợp đồng cần ghi rõ Unicode hay ASCII.

## 4. Ví dụ tối thiểu có thể chạy

```python
import re
def ma_hop_le(text):
    return isinstance(text,str) and re.fullmatch(r'[A-Z]{2}-[0-9]{4}',text) is not None
assert ma_hop_le('AB-1234')
assert not ma_hop_le('../etc/passwd')
assert not ma_hop_le('AB-1234 extra')
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/N01.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Regex không biến đầu vào hợp lệ thành an toàn với mọi API khác, nhất là SQL và shell.
- **Trường hợp biên:** Quá dài cũng có thể gây tiêu thụ tài nguyên; bổ sung giới hạn độ dài.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Xác định trust boundary trong hệ thống thật trước khi chọn cơ chế kiểm tra.

## 7. Bài tập có yêu cầu kiểm chứng

Tạo allowlist mã hàng gồm ba chữ cái ASCII và 5 chữ số; tạo ca chứa newline.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [N01.02_loi_giai.md](LOI_GIAI/N01.02_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Injection, path traversal và command execution** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R21] [OWASP Top 10](https://owasp.org/projects/top-ten) — Tiêu chuẩn cộng đồng.
- [R04] [Python Standard Library 3.15](https://docs.python.org/3.15/library/) — Gốc.
- [R01] [Python 3.15.2 release](https://www.python.org/downloads/release/python-3152/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# N01.03 — Authentication, authorization và least privilege

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD4 · **Chương:** N01 — Bảo mật dữ liệu đầu vào · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** F, G, M. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Authentication, authorization và least privilege** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Authentication xác định danh tính; authorization xác định quyền hành động; least privilege cấp đúng quyền tối thiểu.

**Ngữ cảnh thực tế:** Trong chương **Bảo mật dữ liệu đầu vào**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Kiểm tra quyền ở server ngay trước truy cập resource, không chỉ ẩn button ở UI.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
roles={'alice':{'read'},'bob':{'read','write'}}
def allowed(user,action): return action in roles.get(user,set())
assert allowed('alice','read') and not allowed('alice','write')
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`N01.03_demo.py`](MA_MAU/N01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không tin role/client_id do người dùng tự gửi lên mà không có chữ ký/session đáng tin cậy.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Thiết kế RBAC hai vai trò với resource ownership check.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_N01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/N01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R21: OWASP Top 10](https://owasp.org/projects/top-ten)
- [R04: Python Standard Library 3.15](https://docs.python.org/3.15/library/)
- [R01: Python 3.15.2 release](https://www.python.org/downloads/release/python-3152/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: N01.01, N01.02, N01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
