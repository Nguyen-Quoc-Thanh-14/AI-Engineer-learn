# Chương A03 — Phân tích bài toán

> **Giai đoạn:** GD0 · **Học phần:** Nhập môn và tư duy lập trình  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương A03: Phân tích bài toán, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Đầu vào, đầu ra và ràng buộc; Lưu đồ, dry-run và thiết kế ca kiểm thử.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [A03.01 — Đầu vào, đầu ra và ràng buộc](BAI_HOC/A03.01.md)
- [A03.02 — Chia nhỏ bài toán và giả mã](BAI_HOC/A03.02.md)
- [A03.03 — Lưu đồ, dry-run và thiết kế ca kiểm thử](BAI_HOC/A03.03.md)

## Tiên quyết

Không có điều kiện tiên quyết bắt buộc ở cấp chương.

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R05: Python Tutorial 3.15](https://docs.python.org/3.15/tutorial/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## A03.01 — Đầu vào, đầu ra và ràng buộc

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A03 — Phân tích bài toán · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Đầu vào, đầu ra và ràng buộc** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

Trước khi viết mã, mô tả **bài toán** bằng ba phần: đầu vào (input), đầu ra (output) và ràng buộc (constraints). Ràng buộc bao gồm miền giá trị hợp lệ, định dạng, hành vi khi thiếu dữ liệu và điều kiện kết quả đúng. Không có ràng buộc, những trường hợp như số lượng âm hoặc chia cho 0 có thể được xử lý tùy tiện và tạo lỗi logic.

**Đặc tả** nên phân biệt dữ liệu thực tế với giả định của người viết. Nếu yêu cầu chưa rõ, ghi giả định và cách kiểm tra thay vì ngầm coi là sự thật.

### 3. Trình tự tư duy hoặc thực thi

1. Viết yêu cầu bằng một câu chính xác.
2. Liệt kê tên và kiểu dữ liệu đầu vào.
3. Định nghĩa kết quả và ràng buộc hợp lệ.
4. Đặt ít nhất ba ca: thông thường, biên, sai đầu vào.

### 4. Ví dụ có thể chạy

```python
chieu_dai = 4
chieu_rong = 3
dien_tich = chieu_dai * chieu_rong
print(dien_tich)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
12
```

**Giải thích:** Chương trình tối giản nhận hai giá trị được gán sẵn và tính tích. Mã hiện **chưa xác thực đầu vào**; trước khi dùng thực tế phải bổ sung điều kiện không âm, kiểm tra kiểu dữ liệu và đơn vị đo. Phần này tập trung vào đặc tả, không yêu cầu người học biết `def` hoặc `raise` trước khi tới bài tương ứng.

### 5. Trường hợp biên và lỗi thường gặp

Cần hỏi rõ có tính kích thước âm (không), số không (có), số thực (có) và đơn vị đo hay không. Việc chọn giả định hợp lý phải được ghi vào đặc tả.

### 6. So sánh dễ nhầm lẫn

**Kiểm tra hợp lệ** xét đầu vào có thuộc miền cho phép hay không; **kiểm tra tính đúng** xét thuật toán có tạo đúng kết quả cho đầu vào hợp lệ hay không.

### 7. Thực hành có lời giải riêng

Viết đặc tả hàm tính tiền vé: tuổi 0–5 miễn phí, 6–17 giá 30.000, từ 18 trở lên giá 50.000. Nêu hành vi với tuổi âm.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A03.01_loi_giai.md](LOI_GIAI/A03.01_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Thêm yêu cầu giảm giá cho người cao tuổi và xem ràng buộc nào phải thay đổi.

### 9. Tự kiểm tra khả năng hiểu

1. Tại sao phải ghi rõ đơn vị đo?
2. Một ví dụ đủ chứng minh chương trình đúng trong mọi trường hợp không?
3. Đầu vào sai kiểu là lỗi của thuật toán hay vi phạm hợp đồng đầu vào?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/controlflow.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A03.02 — Chia nhỏ bài toán và giả mã

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A03 — Phân tích bài toán · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Chia nhỏ bài toán và giả mã** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Phân rã** (decomposition) chia vấn đề lớn thành nhiệm vụ nhỏ có thể kiểm tra riêng. **Giả mã** (pseudocode) mô tả logic bằng ngôn ngữ gần tự nhiên, không bị phụ thuộc quá sớm vào cú pháp Python. Một giả mã hữu ích nêu rõ bước xử lý, điều kiện và dữ liệu trung gian.

Chia bài toán theo chức năng sẽ giúp phát hiện bước nào còn thiếu và xác định điểm có thể tái sử dụng thành hàm.

### 3. Trình tự tư duy hoặc thực thi

1. Nêu mục tiêu và đầu ra.
2. Chia thành thu thập đầu vào, kiểm tra, tính toán, trình bày.
3. Viết giả mã từng bước; lần vết ít nhất một ví dụ.
4. Chuyển giả mã sang Python và kiểm tra từng bước.

### 4. Ví dụ có thể chạy

```python
## Giả mã: nhận 3 điểm, tính trung bình, rồi xét ngưỡng đạt 5.
diem_1 = 6
diem_2 = 5
diem_3 = 4
trung_binh = (diem_1 + diem_2 + diem_3) / 3
print(trung_binh)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
5.0
```

**Giải thích:** Mỗi dòng có một nhiệm vụ đơn giản. Ba điểm có tổng 15, nên trung bình là 5.0. Bước xếp loại “đạt nếu trung bình từ 5” được giữ ở dạng giả mã, vì câu lệnh điều kiện sẽ được học kỹ ở B05. Nếu đổi yêu cầu sang số điểm bất kỳ, công thức và ràng buộc số lượng điểm phải được viết lại.

### 5. Trường hợp biên và lỗi thường gặp

Tránh viết giả mã mơ hồ như “xử lý dữ liệu”; nên ghi rõ công thức và điều kiện. Bước validation không được bỏ qua chỉ vì chưa biết cú pháp.

### 6. So sánh dễ nhầm lẫn

**Giả mã** diễn đạt thuật toán; **flowchart** diễn đạt luồng bằng hình; **code** chịu ràng buộc cú pháp của ngôn ngữ.

### 7. Thực hành có lời giải riêng

Viết giả mã cho việc tính tiền sau giảm giá 10% khi hóa đơn >= 200.000 đồng.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A03.02_loi_giai.md](LOI_GIAI/A03.02_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Đề xuất tách bài toán xử lý bảng điểm thành ba hàm nhỏ và định nghĩa đầu vào/đầu ra của từng hàm.

### 9. Tự kiểm tra khả năng hiểu

1. Giả mã có cần tuân thủ toàn bộ cú pháp Python không?
2. Tách chức năng giúp kiểm thử như thế nào?
3. Khi nào việc chia nhỏ quá nhiều lại gây khó hiểu?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/controlflow.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A03.03 — Lưu đồ, dry-run và thiết kế ca kiểm thử

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A03 — Phân tích bài toán · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Lưu đồ, dry-run và thiết kế ca kiểm thử** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Lưu đồ** biểu diễn các bước thực thi: hình bắt đầu/kết thúc, thao tác, nhập/xuất và nhánh quyết định. **Dry-run** là lần vết thủ công giá trị biến qua từng dòng mà chưa chạy mã. **Test case** là một tập đầu vào có kết quả kỳ vọng.

Một bảng lần vết giúp phát hiện nhánh thiếu hoặc vòng lặp không dừng. Các ca kiểm thử nên bao gồm giá trị sát biên (ví dụ 17 và 18 khi điều kiện là từ 18 tuổi).

### 3. Trình tự tư duy hoặc thực thi

1. Vẽ chuỗi thao tác và nhánh quyết định.
2. Chọn đầu vào cụ thể và ghi giá trị biến theo từng bước.
3. Lập bảng ca thử có kết quả kỳ vọng.
4. Chạy thật và so sánh; ghi rõ sai khác.

### 4. Ví dụ có thể chạy

```python
tuoi = 17
if tuoi >= 18:
    nhom = "Người lớn"
else:
    nhom = "Chưa đủ 18"
print(nhom)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Chưa đủ 18
```

**Giải thích:** Dry-run: lúc đầu `tuoi=17`; so sánh `17 >= 18` là False; đi vào `else`; `nhom` được gán chuỗi và in ra. Ca biên đáng thử: 18, giá trị ngay dưới 18 và giá trị không hợp lệ.

### 5. Trường hợp biên và lỗi thường gặp

Không thể dùng một ca thử để kết luận chương trình không còn lỗi. Với dữ liệu thực, có thể cần đo độ phủ nhánh và kiểm tra các trạng thái ngoại lệ.

### 6. So sánh dễ nhầm lẫn

**Dry-run** là kiểm tra bằng lý luận; **test tự động** chạy code; hai cách bổ sung lẫn nhau.

### 7. Thực hành có lời giải riêng

Lập bảng kiểm thử cho điều kiện `tuoi >= 18` với tuổi 0, 17, 18 và 100.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A03.03_loi_giai.md](LOI_GIAI/A03.03_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Viết chương trình đọc tuổi từ `input()` rồi kiểm tra. Giải thích tại sao cần xử lý trường hợp nhập chữ.

### 9. Tự kiểm tra khả năng hiểu

1. Dry-run khác debug thực thi ở đâu?
2. Vì sao giá trị 18 đặc biệt quan trọng khi kiểm tra biên?
3. Có nên tính mọi chuỗi nhập vào là tuổi hợp lệ không?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/controlflow.html
- https://docs.python.org/3.15/library/unittest.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: A03.01, A03.02, A03.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
