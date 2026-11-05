# Chương A02 — Thiết lập môi trường

> **Giai đoạn:** GD0 · **Học phần:** Nhập môn và tư duy lập trình  
> **Trạng thái:** BẢN THẢO CHƯƠNG ĐÃ ĐỒNG BỘ NỘI DUNG BÀI HỌC — cần phản biện sư phạm độc lập và kiểm thử CPython 3.15.2.  
> **Đích:** CPython 3.15.2; một số ví dụ thực thi với Python 3.13.5 theo trạng thái từng bài.

## Mục tiêu chương

- Giải thích đúng các thuật ngữ và cơ chế của chương A02: Thiết lập môi trường, nêu được một giới hạn hoặc phản ví dụ.
- Triển khai và tự kiểm tra tối thiểu một ứng dụng nhỏ sử dụng ít nhất hai nội dung: Cài Python và xác minh phiên bản; Editor, terminal và cấu trúc thư mục thực hành.
- Phân tích ít nhất hai trường hợp biên hoặc lỗi thường gặp; giải thích vì sao cách xử lý được chọn phù hợp.

## Danh mục bài học và file học riêng

- [A02.01 — Cài Python và xác minh phiên bản](BAI_HOC/A02.01.md)
- [A02.02 — REPL, script và cách chạy module](BAI_HOC/A02.02.md)
- [A02.03 — Editor, terminal và cấu trúc thư mục thực hành](BAI_HOC/A02.03.md)

## Tiên quyết

Không có điều kiện tiên quyết bắt buộc ở cấp chương.

## Nguồn đối chiếu

- S01: Python Crash Course
- [R03: Python Language Reference 3.15](https://docs.python.org/3.15/reference/)
- [R05: Python Tutorial 3.15](https://docs.python.org/3.15/tutorial/)
- [R06: Python HOWTOs](https://docs.python.org/3.15/howto/)

---

## A02.01 — Cài Python và xác minh phiên bản

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A02 — Thiết lập môi trường · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Cài Python và xác minh phiên bản** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Cài đặt** tạo môi trường để gọi trình thông dịch Python từ terminal. Cách cài phụ thuộc Windows, macOS hay Linux. Trong giáo trình v2.0, bản tham chiếu là CPython **3.15.2**; nếu một thư viện chưa hỗ trợ 3.15 thì có thể dùng nhánh 3.14 trong môi trường riêng sau khi kiểm tra.

Không nên sửa bừa Python hệ thống trên Linux/macOS, vì có thể ảnh hưởng công cụ của hệ điều hành. Câu lệnh `python`, `python3` hoặc `py` có thể chọn runtime khác nhau. Vì vậy luôn **xác minh đúng runtime được dùng**, không chỉ nhìn bản cài trong giao diện.

### 3. Trình tự tư duy hoặc thực thi

1. Tải bản phát hành từ python.org hoặc trình quản lý tin cậy của hệ điều hành.
2. Thực hiện hướng dẫn cài cho hệ điều hành đó.
3. Mở terminal mới và kiểm tra phiên bản.
4. Chạy một script ngắn để bảo đảm chương trình thực thi được.

### 4. Ví dụ có thể chạy

```python
## Lưu tệp kiem_tra_python.py và chạy bằng Python
import sys
print(sys.version_info[:3])
print(sys.executable)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Bộ ba phiên bản và đường dẫn đến trình thông dịch, phụ thuộc máy cài đặt.
```

**Giải thích:** `sys.executable` giúp phát hiện lỗi cài nhiều Python hoặc môi trường ảo. Không copy nguyên đường dẫn từ máy khác. Trên Windows có thể dùng `py -3.15 --version`; trên macOS/Linux thường dùng `python3 --version` nếu có bản phù hợp.

### 5. Trường hợp biên và lỗi thường gặp

Không dùng `sudo pip install` lên Python hệ thống để giải quyết lỗi quyền một cách tùy tiện. Kiểm tra môi trường và dùng virtual environment trong bài F03.

### 6. So sánh dễ nhầm lẫn

`python --version` hỏi phiên bản của lệnh được chọn; `sys.executable` cho biết đường dẫn runtime đã chạy script.

### 7. Thực hành có lời giải riêng

Chạy `python --version` hoặc `python3 --version`, rồi chạy tệp kiểm tra. Ghi nhận hai thông tin: phiên bản và đường dẫn thực thi.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A02.01_loi_giai.md](LOI_GIAI/A02.01_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Nếu `python` hiển thị 3.13 nhưng `py -3.15` hiển thị 3.15, giải thích nguyên nhân có thể liên quan alias/PATH/launcher.

### 9. Tự kiểm tra khả năng hiểu

1. Vì sao cần kiểm tra `sys.executable`?
2. Khi nào nên dùng môi trường ảo?
3. Có nên xóa Python hệ thống chỉ vì nó không phải phiên bản mới nhất?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://www.python.org/downloads/release/python-3152/
- https://docs.python.org/3.15/using/index.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A02.02 — REPL, script và cách chạy module

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A02 — Thiết lập môi trường · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **REPL, script và cách chạy module** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**REPL** (Read–Eval–Print Loop) là chế độ nhập lệnh tương tác: nhập một biểu thức, Python xử lý và thường hiển thị giá trị biểu thức. **Script** là tệp `.py` được thực thi một lần theo logic chương trình. Với `python -m ten_module`, Python tìm module trong môi trường hiện tại và chạy module đó ở vai trò entry point.

REPL hữu ích để thử ngắn, còn script giúp lưu lại và tái lập. Không nhầm `python -m pip` (chạy module pip trong runtime được chọn) với gọi lệnh `pip` có thể trỏ sang runtime khác.

### 3. Trình tự tư duy hoặc thực thi

1. Mở terminal và chạy `python` hoặc `python3` để vào REPL.
2. Nhập `2 + 3` rồi quan sát kết quả hiển thị.
3. Gõ `exit()` để thoát.
4. Lưu một script và chạy bằng tên tệp; thử `python -m json.tool --help` như ví dụ module thư viện chuẩn.

### 4. Ví dụ có thể chạy

```python
## Tệp chao.py
loi_chao = "Xin chào Python"
print(loi_chao)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Xin chào Python
```

**Giải thích:** Chạy `python chao.py` trên runtime có lệnh `python`. Trong REPL, nếu chỉ nhập `2 + 3`, thường nhìn thấy `5`; trong script, biểu thức `2 + 3` đứng riêng không tự in kết quả, phải gọi `print()`.

### 5. Trường hợp biên và lỗi thường gặp

Nếu terminal đang ở thư mục khác, `python chao.py` có thể báo không tìm thấy tệp. Lỗi này liên quan đường dẫn, không nhất thiết liên quan cú pháp trong script.

### 6. So sánh dễ nhầm lẫn

REPL: thử tương tác; script: chương trình lưu; `-m`: chạy một module/package thích hợp bằng đường phân giải module.

### 7. Thực hành có lời giải riêng

Tạo `tinh_tong.py`, lưu phép cộng 7 và 8 rồi dùng `print()` để in kết quả.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A02.02_loi_giai.md](LOI_GIAI/A02.02_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Thử `python -c "print(2+3)"` và giải thích vì sao kết quả giống nhưng cách cung cấp mã khác với script và REPL.

### 9. Tự kiểm tra khả năng hiểu

1. REPL có tự lưu mã thành `.py` không?
2. Vì sao script cần `print()` để thấy kết quả tính toán?
3. `-m` khác chạy một tệp đường dẫn thế nào?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/tutorial/interpreter.html
- https://docs.python.org/3.15/using/cmdline.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## A02.03 — Editor, terminal và cấu trúc thư mục thực hành

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A02 — Thiết lập môi trường · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

### 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Editor, terminal và cấu trúc thư mục thực hành** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

### 2. Khái niệm và bản chất

**Editor/IDE** để viết và đọc mã; **terminal/shell** để ra lệnh; **working directory** là thư mục hiện tại mà lệnh tương đối được tính từ đó. Khả năng chạy đúng một tệp không phụ thuộc bắt buộc vào IDE cụ thể. Người học nên tách tệp bài học, bài tập và dữ liệu để tránh ghi đè, đồng thời không đặt thông tin bí mật vào thư mục nguồn.

Khi dùng đường dẫn tương đối, vị trí làm việc thực tế rất quan trọng. Dấu phân cách đường dẫn khác nhau theo hệ điều hành; `pathlib` giúp lập trình ít phụ thuộc nền tảng.

### 3. Trình tự tư duy hoặc thực thi

1. Tạo thư mục `hoc_python`.
2. Tạo thư mục con `bai_hoc`, `bai_tap`, `du_lieu`.
3. Mở terminal trong `hoc_python`.
4. Tạo và chạy một script, xác minh thư mục làm việc.

### 4. Ví dụ có thể chạy

```python
from pathlib import Path

print(Path.cwd().name)
print(Path("bai_tap").is_absolute())
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Tên thư mục đang làm việc trên máy
False
```

**Giải thích:** `Path.cwd().name` lấy tên thư mục cuối, khác tùy máy. `Path("bai_tap")` là đường dẫn tương đối nên `is_absolute()` trả False; điều đó không chứng minh thư mục có tồn tại.

### 5. Trường hợp biên và lỗi thường gặp

Không dùng lệnh xóa hàng loạt hay ghi đè dữ liệu thật trong lần thử đầu tiên. Kiểm tra `cwd` trước khi thao tác tệp và dùng thư mục thử nghiệm.

### 6. So sánh dễ nhầm lẫn

Thư mục của **tệp script** khác thư mục **làm việc hiện tại**; hai thư mục có thể trùng nhưng không được giả định luôn trùng.

### 7. Thực hành có lời giải riêng

Tạo ba thư mục nêu trên và một tệp `bai_hoc/hello.py`. Chạy từ thư mục gốc.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A02.03_loi_giai.md](LOI_GIAI/A02.03_loi_giai.md) — chỉ xem sau khi tự làm.

### 8. Bài tự làm mở rộng

Chạy cùng script khi đứng ở thư mục gốc và khi đứng trong `bai_hoc`; mô tả sự thay đổi working directory.

### 9. Tự kiểm tra khả năng hiểu

1. Editor có phải nơi thực sự thực thi mọi chương trình không?
2. Working directory ảnh hưởng đường dẫn tương đối ra sao?
3. Vì sao cần thư mục dữ liệu thử nghiệm?

### 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

### 11. Nguồn

- https://docs.python.org/3.15/library/pathlib.html
- https://docs.python.org/3.15/using/index.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: A02.01, A02.02, A02.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
