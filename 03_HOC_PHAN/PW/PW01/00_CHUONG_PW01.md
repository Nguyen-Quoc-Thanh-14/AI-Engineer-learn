# Chương PW01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# PW01.01 — HTTP lifecycle và web architecture

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PW01 — Nền tảng backend · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **HTTP lifecycle và web architecture**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** M, N, O.

## 2. Khái niệm — Bản chất

HTTP là giao thức request/response: method, target, header, body và status code. Backend thực tế gồm routing, validation, logic nghiệp vụ, I/O, error handling và quan sát hệ thống. Giao thức stateless không đồng nghĩa ứng dụng không có session; session được quản lý qua lớp khác.

## 3. Nguyên lý và cơ chế từng bước

Dùng `http.HTTPStatus` phân loại status thay vì chạy web server. Đánh giá response 2xx/4xx/5xx phải xem contract API, không chỉ đoán theo số.

## 4. Ví dụ tối thiểu có thể chạy

```python
from http import HTTPStatus
assert HTTPStatus.OK==200
assert HTTPStatus.BAD_REQUEST==400
assert HTTPStatus.INTERNAL_SERVER_ERROR==500
print(HTTPStatus.OK.phrase)
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
OK
```

**Thực hành:** chạy file `07_MA_VI_DU/PW01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không gửi stack trace, mật khẩu, nội dung token trong lỗi HTTP công khai.
- **Trường hợp biên:** Retry tự động một request POST có side effect cần idempotency key hoặc contract phù hợp.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Cần hiểu HTTP trước khi chọn FastAPI, Django, ASGI hoặc ORM.

## 7. Bài tập có yêu cầu kiểm chứng

Định nghĩa bảng ánh xạ input validation lỗi -> HTTP 400, không tìm thấy -> 404, lỗi hệ thống -> 500; giải thích không rò rỉ nội bộ.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PW01.01_loi_giai.md](LOI_GIAI/PW01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **HTTP lifecycle và web architecture** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [R31] [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — Chính thức thư viện.
- [R32] [Django 6.1 Documentation](https://docs.djangoproject.com/en/6.1/) — Chính thức thư viện.
- [R33] [SQLAlchemy 2.1 Documentation](https://docs.sqlalchemy.org/en/21/) — Chính thức thư viện.
- [R36] [Docker Python Guide](https://docs.docker.com/guides/python/) — Chính thức công cụ.
- [R40] [SQLAlchemy Release Status](https://www.sqlalchemy.org/download.html) — Chính thức thư viện.
- [R41] [Django Release Announcements](https://www.djangoproject.com/weblog/2026/aug/05/django-61-released/) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

HTTP tách URL, method, header, body và status. Query string có thể chứa nhiều giá trị cho cùng một key; không nên đồng nhất việc parse query với xác thực đầu vào hoặc kiểm soát truy cập.

### Cách suy luận và thiết kế lời giải

Phân tích URL và các query parameters bằng urllib.parse, chỉ cho phép http/https và hostname không rỗng. Giữ danh sách giá trị của một key thay vì tự động lấy phần tử đầu tiên; hành vi duplicate keys cần được API spec quy định.

### Phản ví dụ và ngộ nhận cần tránh

Không dùng urlsplit rồi cho rằng URL luôn an toàn cho HTTP fetch: SSRF còn đòi hỏi kiểm tra DNS/IP/redirect ở lớp kết nối, không chỉ kiểm tra scheme.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`PW01.01_bai_tap_da_giai_v25.py`](MA_MAU/PW01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`PW01.01_loi_giai.md`](LOI_GIAI/PW01.01_loi_giai.md).
5. **Bài mở rộng:** Viết mô tả API GET /items?page=1 với các mã 200, 400, 404; xây ma trận hợp đồng và test không có network.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/library/urllib.parse.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# PW01.02 — FastAPI hoặc Django fundamentals

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PW01 — Nền tảng backend · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** M, N, O. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **FastAPI hoặc Django fundamentals** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

FastAPI sử dụng type annotations và Pydantic validation; Django tích hợp ORM/auth; lựa chọn phụ thuộc bài toán.

**Ngữ cảnh thực tế:** Trong chương **Nền tảng backend**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Tách routing khỏi business logic, tạo endpoint/test client trong môi trường kiểm soát.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
from fastapi import FastAPI
app=FastAPI()
@app.get('/health')
def health():return {'ok':True}
assert health()=={'ok':True}
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PW01.02_demo.py`](MA_MAU/PW01.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Không chọn framework chỉ theo benchmarks hello-world.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Viết FastAPI endpoint GET /items với response model và test validation.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PW01_02.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PW01.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R31: FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [R32: Django 6.1 Documentation](https://docs.djangoproject.com/en/6.1/)
- [R33: SQLAlchemy 2.1 Documentation](https://docs.sqlalchemy.org/en/21/)
- [R36: Docker Python Guide](https://docs.docker.com/guides/python/)
- [R40: SQLAlchemy Release Status](https://www.sqlalchemy.org/download.html)
- [R41: Django Release Announcements](https://www.djangoproject.com/weblog/2026/aug/05/django-61-released/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


---

# PW01.03 — Routing, validation và serialization

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PW01 — Nền tảng backend · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** M, N, O. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Routing, validation và serialization** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Routing phân phối path/method; request validation chuyển dữ liệu thiếu tin cậy thành schema; serialization quản lý output contract.

**Ngữ cảnh thực tế:** Trong chương **Nền tảng backend**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Validate trước logic nghiệp vụ, kiểm mã lỗi và response schema.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
from fastapi import FastAPI
app=FastAPI()
@app.get('/items/{item_id}')
def get_item(item_id:int):return {'item_id':item_id}
assert get_item(7)['item_id']==7
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PW01.03_demo.py`](MA_MAU/PW01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Type annotations một mình không bảo đảm auth hoặc business rules.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tạo handler POST với Pydantic schema giá dương và test 422.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PW01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PW01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- [R31: FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [R32: Django 6.1 Documentation](https://docs.djangoproject.com/en/6.1/)
- [R33: SQLAlchemy 2.1 Documentation](https://docs.sqlalchemy.org/en/21/)
- [R36: Docker Python Guide](https://docs.docker.com/guides/python/)
- [R40: SQLAlchemy Release Status](https://www.sqlalchemy.org/download.html)
- [R41: Django Release Announcements](https://www.djangoproject.com/weblog/2026/aug/05/django-61-released/)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: PW01.01, PW01.02, PW01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
