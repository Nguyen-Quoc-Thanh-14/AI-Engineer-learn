# Chương A05 — Tư duy chương trình và bằng chứng về tính đúng

> **Giai đoạn:** GD0 · **Học phần:** Nhập môn và tư duy lập trình  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương A05: Tư duy chương trình và bằng chứng về tính đúng, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Mô phỏng trạng thái chương trình; Giải thích độ đúng bằng lập luận từng bước.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [A05.01 — Mô phỏng trạng thái chương trình](BAI_HOC/A05.01.md)
- [A05.02 — Invariants, tiền điều kiện và hậu điều kiện](BAI_HOC/A05.02.md)
- [A05.03 — Xây dựng bộ dữ liệu thử và phản ví dụ](BAI_HOC/A05.03.md)
- [A05.04 — Giải thích độ đúng bằng lập luận từng bước](BAI_HOC/A05.04.md)

## Tiên quyết

Không có điều kiện tiên quyết bắt buộc ở cấp chương.

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R05: Python Tutorial 3.15](https://docs.python.org/3.15/tutorial/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## A05.01 — Mô phỏng trạng thái chương trình

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A05 — Tư duy chương trình và bằng chứng về tính đúng · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Mô phỏng trạng thái chương trình** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Trạng thái chương trình** tại một thời điểm là tập thông tin cần để tiếp tục xử lý, bao gồm giá trị mà những tên đang tham chiếu và các dữ liệu liên quan. **Bảng lần vết** (trace table) ghi trạng thái sau từng câu lệnh. Việc một tên được gán lại không nhất thiết có nghĩa là đối tượng cũ đã bị sửa; mô hình đối tượng–tham chiếu chính xác sẽ học ở B01/C03.

Ở bước nhập môn, hãy quan sát các giá trị trước và sau phép gán. Không cần học khái niệm stack, heap hoặc garbage collector để tự lần vết chương trình đơn giản.

### 3. Trình tự tư duy hoặc thực thi

1. Ghi trạng thái đầu vào.
2. Thực hiện lần lượt từng phép gán hoặc phép tính.
3. Sau mỗi bước, cập nhật bảng tên và giá trị tương ứng.
4. Đối chiếu dòng in cuối với trạng thái đã dự đoán.

### 4. Ví dụ có thể chạy

```python
so_du = 100_000
so_du = so_du - 25_000
so_du = so_du + 10_000
print(so_du)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
85000
```

**Giải thích:** Bảng trạng thái lần lượt là 100000 → 75000 → 85000. Dấu `=` ở đây biểu diễn phép gán tên trong Python, không phải phép khẳng định hai biểu thức bằng nhau trong toán học. Biểu thức phía phải được tính trước, sau đó tên phía trái được gán giá trị mới.

### 5. Trường hợp biên và lỗi thường gặp

Dùng cùng một tên cho dữ liệu trước/sau có thể gây khó đối chiếu. Khi debug, hãy ghi bảng hoặc dùng tên phụ nếu cần để tránh mất thông tin trung gian.

### 6. So sánh dễ nhầm lẫn

Biểu thức `x = x + 1` hợp lệ trong Python vì `=` là phép gán, nhưng không phải một đẳng thức toán học thường.

### 7. Thực hành có lời giải riêng

Lần vết `diem=5; diem=diem+2; diem=diem*3; print(diem)`. Ghi giá trị sau từng bước.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A05.01_loi_giai.md](LOI_GIAI/A05.01_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Thử đổi thứ tự phép cộng và phép nhân trong ví dụ. Chỉ ra vì sao kết quả thay đổi và khi nào chúng không thay đổi.

### 9. Tự kiểm tra khả năng hiểu

1. Trạng thái chương trình khác câu lệnh như thế nào?
2. Tại sao bên phải của phép gán được đánh giá trước?
3. Khi nào bảng lần vết giúp phát hiện lỗi logic?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/reference/simple_stmts.html
- https://docs.python.org/3.15/reference/executionmodel.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A05.02 — Invariants, tiền điều kiện và hậu điều kiện

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A05 — Tư duy chương trình và bằng chứng về tính đúng · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Invariants, tiền điều kiện và hậu điều kiện** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Tiền điều kiện** (precondition) là điều cần đúng trước khi thực hiện thao tác. **Hậu điều kiện** (postcondition) là điều mong đợi sau khi thao tác kết thúc đúng. **Invariant** là thuộc tính được duy trì qua các trạng thái thích hợp của một tiến trình hay vòng lặp.

Ở bài này, chỉ làm quen qua một giao dịch đơn giản: số tiền rút phải không âm và không vượt quá số dư. Nếu yêu cầu hợp lệ, **số dư còn lại = số dư ban đầu − số tiền rút**, hay `số dư ban đầu = số dư còn lại + số tiền rút`. Chương trình minh họa chưa có lệnh kiểm tra tiền điều kiện; việc đó sẽ được dạy khi học `if`.

### 3. Trình tự tư duy hoặc thực thi

1. Nêu tiền điều kiện: số dư ≥ 0, tiền rút từ 0 đến số dư.
2. Nêu phép biến đổi dự kiến.
3. Nêu hậu điều kiện: số dư mới không âm.
4. Kiểm tra quan hệ bảo toàn tổng tiền trong trường hợp hợp lệ.

### 4. Ví dụ có thể chạy

```python
so_du_ban_dau = 100_000
so_tien_rut = 20_000
so_du_moi = so_du_ban_dau - so_tien_rut
print(so_du_moi)
print(so_du_moi + so_tien_rut == so_du_ban_dau)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
80000
True
```

**Giải thích:** Với đầu vào hợp lệ, phép trừ cho số dư mới 80.000 và điều kiện bảo toàn tiền cho `True`. Đây là một điều kiện cần theo mô hình nhưng tự nó không chứng minh tính đúng trong mọi tình huống, chẳng hạn rút vượt số dư sẽ cần chính sách xử lý riêng.

### 5. Trường hợp biên và lỗi thường gặp

Lấy tiền rút lớn hơn số dư có thể cho số dư âm mà Python không báo lỗi; đây là vi phạm tiền điều kiện nghiệp vụ. Dùng `float` cho tiền cũng có nguy cơ sai số; khi làm dự án tài chính sẽ cân nhắc số nguyên đơn vị nhỏ hoặc `decimal.Decimal`.

### 6. So sánh dễ nhầm lẫn

Tiền điều kiện là giả định đầu vào; hậu điều kiện kiểm kết quả; invariant duy trì quan hệ qua nhiều bước (không phải bất kỳ đẳng thức nào cũng là invariant vòng lặp).

### 7. Thực hành có lời giải riêng

Với số dư 70.000 và rút 15.000, nêu tiền điều kiện, số dư mới và một hậu điều kiện kiểm tra được.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A05.02_loi_giai.md](LOI_GIAI/A05.02_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Với rút 90.000 từ số dư 70.000, giải thích vì sao công thức vẫn cho ra số nhưng thao tác phải bị từ chối theo đặc tả.

### 9. Tự kiểm tra khả năng hiểu

1. Precondition phải được kiểm trước hay sau giao dịch?
2. Quan hệ bảo toàn tiền có đủ để loại trừ mọi đầu vào không hợp lệ không?
3. Invariant khác hậu điều kiện ở điểm nào?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/reference/expressions.html
- https://docs.python.org/3.15/library/decimal.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A05.03 — Xây dựng bộ dữ liệu thử và phản ví dụ

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A05 — Tư duy chương trình và bằng chứng về tính đúng · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Xây dựng bộ dữ liệu thử và phản ví dụ** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Bộ kiểm thử** phải đại diện cho nhiều loại đầu vào: thông thường, sát biên, dữ liệu bất thường, sai định dạng và những trường hợp có khả năng làm giả định của người viết không đúng. **Phản ví dụ** là một tình huống cụ thể bác bỏ khẳng định quá rộng, chẳng hạn “công thức luôn cho tổng tiền đúng”.

Khi chưa biết hàm và thư viện kiểm thử, ta vẫn có thể tạo bảng giá trị đầu vào / đầu ra kỳ vọng rồi thay thủ công vào script. Bài H02 sẽ chuyển cách này thành kiểm thử tự động có thể lặp lại.

### 3. Trình tự tư duy hoặc thực thi

1. Phát biểu rõ khẳng định cần kiểm tra.
2. Chọn dữ liệu điển hình và biên.
3. Chọn một đầu vào có thể bác bỏ giả định (counterexample).
4. Đối chiếu kết quả và sửa đặc tả hoặc thuật toán.

### 4. Ví dụ có thể chạy

```python
don_gia = 9_000
so_luong = 0
phi_van_chuyen = 15_000
print(don_gia * so_luong + phi_van_chuyen)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
15000
```

**Giải thích:** Nếu yêu cầu nói rằng “đơn không có hàng không tính tiền”, kết quả 15.000 là **phản ví dụ** cho thiết kế thu phí vận chuyển cố định. Nếu cửa hàng vẫn thu phí kể cả đơn số lượng 0, kết quả có thể đúng. Điều quan trọng là kiểm tra **đặc tả**, không tự áp đặt chính sách.

### 5. Trường hợp biên và lỗi thường gặp

Một test thành công không chứng minh chương trình đúng với tất cả đầu vào. Dữ liệu ngẫu nhiên hữu ích nhưng phải kết hợp giá trị biên có chủ đích.

### 6. So sánh dễ nhầm lẫn

Test thường cho biết một trường hợp hoạt động; phản ví dụ cho thấy một khẳng định phổ quát không đúng. Bộ test mạnh tìm cả hai.

### 7. Thực hành có lời giải riêng

Tạo bảng 4 test cho tổng tiền: số lượng 0, 1, 5 và -1. Ghi điều kiện hợp lệ và kết quả kỳ vọng khi số lượng âm bị cấm.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A05.03_loi_giai.md](LOI_GIAI/A05.03_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Thêm trường hợp phí vận chuyển miễn nếu tổng hàng từ 100.000 và nêu hai test sát ngưỡng.

### 9. Tự kiểm tra khả năng hiểu

1. Phản ví dụ là gì?
2. Vì sao cần test tại biên?
3. Nếu đặc tả không rõ trường hợp số lượng 0, có thể kết luận chương trình sai không?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/library/unittest.html
- https://docs.python.org/3.15/tutorial/controlflow.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A05.04 — Giải thích độ đúng bằng lập luận từng bước

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A05 — Tư duy chương trình và bằng chứng về tính đúng · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Giải thích độ đúng bằng lập luận từng bước** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Lập luận về tính đúng** đi từ các điều kiện ban đầu, phân tích từng bước biến đổi và so sánh kết quả với hậu điều kiện. Với một chương trình nhỏ, ta có thể diễn giải từng phép gán và các tính toán bằng những phép toán đã biết. Tuy nhiên, ví dụ chạy đúng và lập luận trên một đầu vào **chưa tạo thành chứng minh tổng quát** cho mọi dữ liệu.

Một mô hình đáng tin cậy cần nêu giả định (kiểu dữ liệu, miền đầu vào), tính đúng của bước tính và rủi ro còn tồn tại. Trong Python, điều kiện ban đầu và sự làm tròn số phải được xem xét nếu dùng `float`.

### 3. Trình tự tư duy hoặc thực thi

1. Viết công thức và điều kiện đầu vào.
2. Giải thích phép tính của từng câu lệnh bằng giá trị cụ thể.
3. Kiểm tra quan hệ đầu ra với yêu cầu.
4. Tìm ca biên có thể làm lý luận thất bại.

### 4. Ví dụ có thể chạy

```python
gia_goc = 80_000
phan_tram_giam = 10
tien_giam = gia_goc * phan_tram_giam / 100
thanh_toan = gia_goc - tien_giam
print(thanh_toan)
print(thanh_toan + tien_giam == gia_goc)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
72000.0
True
```

**Giải thích:** Giá gốc 80.000; mức giảm 10% tương ứng 8.000; tiền thanh toán 72.000. Quan hệ “tiền thanh toán + tiền giảm = giá gốc” đúng trong dữ liệu minh họa. Với số thực tổng quát, quan hệ dùng `==` có thể chịu ảnh hưởng làm tròn; phép kiểm tra toán học và phép so sánh số thực của máy tính không luôn đồng nhất.

### 5. Trường hợp biên và lỗi thường gặp

Không khẳng định luôn đúng vì chỉ thử một đầu vào. Phần trăm âm, trên 100%, giá gốc âm hoặc số thực vô cùng có thể vi phạm đặc tả. Cần xác minh miền hợp lệ trước.

### 6. So sánh dễ nhầm lẫn

**Dry-run** dự đoán hành vi trên đầu vào cụ thể; **kiểm thử** thực thi trên ca có kiểm tra; **chứng minh tính đúng** cần lập luận bao quát mọi đầu vào hợp lệ dưới các giả định đã nêu.

### 7. Thực hành có lời giải riêng

Giải thích từng bước số tiền thanh toán khi giá gốc 50.000 và giảm 20%, kèm một ca biên cần kiểm tra.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A05.04_loi_giai.md](LOI_GIAI/A05.04_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Tìm một trường hợp sử dụng số thực mà phép tính `a+b==c` gây ngạc nhiên; giải thích vì sao không thể suy từ đó rằng Python sai.

### 9. Tự kiểm tra khả năng hiểu

1. Khi nào lập luận trên một ví dụ là chưa đủ?
2. Lập luận khác với test tự động ở điểm nào?
3. Vì sao số thực cần chú ý khi kiểm tra đẳng thức?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/floatingpoint.html
- https://docs.python.org/3.15/reference/expressions.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: A05.01, A05.02, A05.03, A05.04. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
