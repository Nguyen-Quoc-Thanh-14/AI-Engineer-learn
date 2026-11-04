# Chương E02 — Thiết kế đối tượng

> **Giai đoạn:** GD3 · **Học phần:** Lập trình hướng đối tượng  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương E02: Thiết kế đối tượng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Encapsulation và invariants; Polymorphism và interface.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [E02.01 — Encapsulation và invariants](BAI_HOC/E02.01.md)
- [E02.02 — Composition so với inheritance](BAI_HOC/E02.02.md)
- [E02.03 — Polymorphism và interface](BAI_HOC/E02.03.md)

## Tiên quyết

B, C

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## E02.01 — Encapsulation và invariants

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E02 — Thiết kế đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Encapsulation và invariants**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Encapsulation tập trung bảo vệ invariant: quan hệ luôn đúng giữa các thuộc tính. Python không cấm tuyệt đối truy cập tên có dấu gạch dưới; kiểm soát thuộc tính cần dùng API và validation phù hợp.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class Vi:
    def __init__(self,so_du):
        if so_du<0: raise ValueError('âm')
        self._so_du=so_du
    def nap(self,so_tien):
        if so_tien<=0: raise ValueError('phải dương')
        self._so_du+=so_tien
    @property
    def so_du(self): return self._so_du
x=Vi(10);x.nap(5)
assert x.so_du==15
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/E02.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Đặt tên `_so_du` không ngăn caller chủ động sửa thuộc tính.
- **Trường hợp biên:** Validation phải chạy ở mọi đường cập nhật trạng thái.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo lớp nhận số lượng không âm; method bán hàng không cho tồn kho âm.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E02.01_loi_giai.md](LOI_GIAI/E02.01_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Encapsulation và invariants** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## E02.02 — Composition so với inheritance

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E02 — Thiết kế đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Composition so với inheritance**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Composition mô hình hóa quan hệ *có một* (has-a): lớp giữ đối tượng cộng tác. Inheritance mô hình hóa quan hệ *là một* (is-a) khi có hợp đồng thay thế được; lạm dụng inheritance tạo coupling.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class NhanTin:
    def send(self,x):return 'send:'+x
class DonHang:
    def __init__(self,notifier):self.notifier=notifier
    def xac_nhan(self):return self.notifier.send('ok')
assert DonHang(NhanTin()).xac_nhan()=='send:ok'
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/E02.02_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Không kế thừa chỉ để dùng lại 1 method tiện lợi.
- **Trường hợp biên:** Trong hệ thống nhỏ, một hàm nhận dependency có thể đủ, không cần class.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Tạo class Report sử dụng đối tượng Formatter qua constructor, viết test fake formatter.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E02.02_loi_giai.md](LOI_GIAI/E02.02_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Composition so với inheritance** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.

---

## E02.03 — Polymorphism và interface

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD3 · **Chương:** E02 — Thiết kế đối tượng · **Đích:** CPython 3.15.2.

### 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Polymorphism và interface**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** B, C.

### 2. Khái niệm — Bản chất

Polymorphism cho phép nhiều kiểu đối tượng đáp ứng cùng một giao diện hành vi. Với Python, duck typing có thể dùng mà không bắt buộc chung lớp cha.

### 3. Nguyên lý và cơ chế từng bước

Xác định đầu vào và hợp đồng → thực hiện bước biến đổi → kiểm tra kết quả bằng `assert` → thử thêm ca biên; giải thích từng dòng thay vì chỉ nhìn đầu ra.

### 4. Ví dụ tối thiểu có thể chạy

```python
class Sms:
    def gui(self,x):return 'sms:'+x
class Email:
    def gui(self,x):return 'email:'+x
def thong_bao(k,noi_dung):return k.gui(noi_dung)
assert thong_bao(Sms(),'A')=='sms:A'
assert thong_bao(Email(),'A')=='email:A'
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
(Không có đầu ra; các assert đều đạt)
```

**Thực hành:** chạy file `07_MA_VI_DU/E02.03_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

### 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Trùng tên method không chứng minh hợp đồng về ý nghĩa hay đơn vị là giống nhau.
- **Trường hợp biên:** Nếu kiểu không có method mong đợi, AttributeError tại runtime.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

### 6. So sánh lựa chọn kỹ thuật và đánh đổi

So sánh với cách xử lý không có cấu trúc trước khi thêm abstraction.

### 7. Bài tập có yêu cầu kiểm chứng

Viết hai class thanh toán với `tinh_phi(amount)` và một hàm gọi chung.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [E02.03_loi_giai.md](LOI_GIAI/E02.03_loi_giai.md).

### 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Polymorphism và interface** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

### 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

### 10. Nguồn và giới hạn

- [S01] Python Crash Course — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R03] [Python Language Reference 3.15](https://docs.python.org/3.15/reference/) — Chuẩn ngôn ngữ.
- [R06] [Python HOWTOs](https://docs.python.org/3.15/howto/) — Gốc.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: E02.01, E02.02, E02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
