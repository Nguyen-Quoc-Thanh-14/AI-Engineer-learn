# Chương A04 — Lỗi và tư duy gỡ lỗi

> **Giai đoạn:** GD0 · **Học phần:** Nhập môn và tư duy lập trình  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương A04: Lỗi và tư duy gỡ lỗi, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: SyntaxError, exception và lỗi logic; Tái hiện lỗi và khoanh vùng nguyên nhân.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [A04.01 — SyntaxError, exception và lỗi logic](BAI_HOC/A04.01.md)
- [A04.02 — Đọc traceback có hệ thống](BAI_HOC/A04.02.md)
- [A04.03 — Tái hiện lỗi và khoanh vùng nguyên nhân](BAI_HOC/A04.03.md)

## Tiên quyết

Không có điều kiện tiên quyết bắt buộc ở cấp chương.

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R05: Python Tutorial 3.15](https://docs.python.org/3.15/tutorial/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## A04.01 — SyntaxError, exception và lỗi logic

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A04 — Lỗi và tư duy gỡ lỗi · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **SyntaxError, exception và lỗi logic** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

Ba nhóm lỗi cần phân biệt: **lỗi cú pháp** (mã không được phân tích hợp lệ), **ngoại lệ lúc chạy** (runtime exception xảy ra khi thực thi) và **lỗi logic** (chương trình vẫn chạy nhưng tạo kết quả sai). Python báo ngoại lệ bằng tên loại và traceback; còn lỗi logic có thể không hiển thị cảnh báo.

`SyntaxError` là một lớp exception, nhưng trong thực tế giáo trình dùng tên “lỗi cú pháp” để nhấn mạnh lỗi xảy ra trước khi phần mã liên quan được chạy. Trong một số tình huống như `eval`/`compile`, `SyntaxError` có thể xuất hiện lúc chương trình đang chạy.

### 3. Trình tự tư duy hoặc thực thi

1. Xác định triệu chứng: không chạy, dừng giữa chừng, hay chạy sai kết quả.
2. Đọc thông báo lỗi cụ thể và dòng gây lỗi.
3. Tạo ví dụ tối thiểu tái hiện.
4. Sửa nguyên nhân và chạy lại cả ca đúng lẫn ca biên.

### 4. Ví dụ có thể chạy

```python
gia = 100_000
phan_tram = 10
gia_sau_giam = gia * (1 - phan_tram / 100)
print(gia_sau_giam)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
90000.0
```

**Giải thích:** Ví dụ đúng cho giảm 10%. Nếu viết `(1 + phan_tram / 100)`, chương trình vẫn chạy nhưng tăng giá: **lỗi logic**. Nếu bỏ dấu đóng ngoặc `)`, sinh `SyntaxError`. Nếu `phan_tram` là chuỗi, phép chia có thể gây `TypeError`.

### 5. Trường hợp biên và lỗi thường gặp

Không xử lý mọi lỗi bằng `except Exception: pass`, vì sẽ che giấu lỗi và làm khó debug. Từng tình huống phải chọn hành vi phù hợp.

### 6. So sánh dễ nhầm lẫn

Cú pháp được parser kiểm tra; exception mô tả thất bại lúc thực thi; lỗi logic được nhận ra nhờ đặc tả và ca thử.

### 7. Thực hành có lời giải riêng

Phân loại: `print("hi"` thiếu dấu ); `1 / 0`; tính diện tích bằng phép cộng thay vì nhân.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A04.01_loi_giai.md](LOI_GIAI/A04.01_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Viết hai phiên bản hàm giảm giá: đúng và sai logic. Lập ca thử phát hiện sai khác.

### 9. Tự kiểm tra khả năng hiểu

1. Chương trình không ném exception có chắc đúng không?
2. Vì sao `except: pass` nguy hiểm?
3. Có tình huống nào SyntaxError xuất hiện trong lúc runtime không?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/errors.html
- https://docs.python.org/3.15/reference/simple_stmts.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A04.02 — Đọc traceback có hệ thống

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A04 — Lỗi và tư duy gỡ lỗi · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Đọc traceback có hệ thống** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Traceback** (truy vết ngăn xếp) trình bày chuỗi vị trí lời gọi dẫn đến exception và vị trí exception được sinh ra. Khi đọc, thường bắt đầu từ **dòng cuối** để biết loại lỗi và thông điệp, sau đó xem những frame liên quan trong mã của mình để tìm ngữ cảnh.

Không nên chỉ nhìn số dòng và sửa tùy tiện. Vị trí báo lỗi có thể là nơi triệu chứng xuất hiện, còn nguyên nhân bắt nguồn từ dữ liệu hoặc lời gọi trước đó.

### 3. Trình tự tư duy hoặc thực thi

1. Đọc tên exception ở cuối.
2. Xác định đường dẫn tệp, hàm và dòng liên quan.
3. Kiểm tra giá trị đầu vào tại lời gọi.
4. Tạo ví dụ tối thiểu và sửa nguyên nhân.

### 4. Ví dụ có thể chạy

```python
def chia(a, b):
    return a / b

def tinh_ty_le():
    return chia(10, 0)

## Dòng sau được chủ ý để người học tự chạy và quan sát lỗi.
tinh_ty_le()
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Sinh ZeroDivisionError: division by zero; số dòng và đường dẫn trong traceback phụ thuộc nơi lưu tệp.
```

**Giải thích:** Thứ tự lời gọi: module → `tinh_ty_le` → `chia` → phép chia có mẫu số 0. Traceback giúp thấy chuỗi lời gọi; exception ở phép chia nhưng dữ liệu 0 được truyền từ hàm gọi.

### 5. Trường hợp biên và lỗi thường gặp

Traceback của thư viện ngoài có thể dài. Không cần hiểu từng frame của thư viện ngay; hãy xác định đoạn mã của bạn, dữ liệu truyền vào và hợp đồng của hàm.

### 6. So sánh dễ nhầm lẫn

Thông báo cuối cho biết **lỗi gì**; các frame giúp xác định **đường đi đến lỗi**. Hai phần cần được đọc cùng nhau.

### 7. Thực hành có lời giải riêng

Giải thích thứ tự gọi hàm trong ví dụ và vì sao sửa `b` bằng 2 giúp tính ra 5.0.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A04.02_loi_giai.md](LOI_GIAI/A04.02_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Thêm kiểm tra `if b == 0: raise ValueError(...)` và giải thích lợi ích khi ứng dụng có đầu vào không tin cậy.

### 9. Tự kiểm tra khả năng hiểu

1. Dòng cuối traceback thường nói điều gì?
2. Vì sao vị trí phát hiện lỗi không luôn là nơi tạo dữ liệu sai?
3. Nên sửa mã nguồn thư viện ngay khi thấy frame của thư viện không?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/errors.html
- https://docs.python.org/3.15/library/traceback.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A04.03 — Tái hiện lỗi và khoanh vùng nguyên nhân

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A04 — Lỗi và tư duy gỡ lỗi · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Tái hiện lỗi và khoanh vùng nguyên nhân** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Tái hiện lỗi** nghĩa là tìm được tập bước và đầu vào làm lỗi xuất hiện lặp lại. **Khoanh vùng** nghĩa là giảm số thành phần nghi ngờ bằng quan sát có kiểm soát. Phương pháp hiệu quả: giữ một yếu tố thay đổi mỗi lần, tạo ví dụ tối thiểu và lưu lại đầu ra trước/sau khi sửa.

**Giả thuyết debug** là phỏng đoán có thể kiểm tra; không nên đồng nhất với kết luận. Nếu không tái hiện được, cần kiểm tra khác biệt môi trường, phiên bản, thư mục làm việc và dữ liệu.

### 3. Trình tự tư duy hoặc thực thi

1. Ghi hiện tượng, phiên bản Python và lệnh chạy.
2. Tạo dữ liệu đầu vào gây lỗi.
3. Giảm chương trình xuống ví dụ nhỏ vẫn sai.
4. Đề xuất một nguyên nhân, kiểm tra bằng log/breakpoint/test.
5. Sửa và thêm regression test.

### 4. Ví dụ có thể chạy

```python
so = [2, 4, 6]
trung_binh = sum(so) / len(so)
print(trung_binh)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
4.0
```

**Giải thích:** Nếu đổi `so = []`, phép chia có mẫu số 0 và chương trình dừng bằng `ZeroDivisionError`. Bước debug đầu tiên là tái hiện với dữ liệu rỗng; sau đó xác định rằng `len(so)` bằng 0. Bài này chưa giải thích chi tiết cú pháp kiểm tra danh sách — phần đó sẽ được học ở B05/C01; điều quan trọng là xác định nguyên nhân.

### 5. Trường hợp biên và lỗi thường gặp

Không dùng `print()` quá nhiều khiến thông tin quan trọng bị chìm. Khi đã có chương trình dài, cần chuyển sang logging/debugger và test tự động; chương H04 sẽ hướng dẫn chi tiết.

### 6. So sánh dễ nhầm lẫn

**Debug** tìm/sửa lỗi hiện tại; **regression test** giảm nguy cơ lỗi cũ tái xuất hiện; **profiling** đo hiệu năng, không thay thế debug.

### 7. Thực hành có lời giải riêng

Lập ba ca thử cho `trung_binh`: `[2,4,6]`, `[0]`, `[]`, ghi kết quả hoặc exception kỳ vọng.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A04.03_loi_giai.md](LOI_GIAI/A04.03_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Tạo thêm ca nhập sai kiểu, đề xuất validation phù hợp và viết test bảo đảm lỗi được báo rõ.

### 9. Tự kiểm tra khả năng hiểu

1. Ví dụ tối thiểu giúp ích gì?
2. Vì sao ghi phiên bản Python là thông tin quan trọng khi báo lỗi?
3. Sau khi sửa lỗi, cần kiểm tra lại những ca nào?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/library/pdb.html
- https://docs.python.org/3.15/library/unittest.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: A04.01, A04.02, A04.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
