# Chương A01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# A01.01 — Máy tính thực thi lệnh

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A01 — Chương trình và Python · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

## 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Máy tính thực thi lệnh** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

## 2. Khái niệm và bản chất

Một **chương trình** là một tập chỉ dẫn được biểu diễn theo quy tắc mà máy tính có thể xử lý. Với Python, ta viết mã nguồn dạng văn bản. Chương trình nhận **đầu vào**, thực hiện thao tác và tạo **đầu ra** hoặc tác động khác (ghi tệp, gửi yêu cầu mạng). Không phải chương trình nào cũng có đầu vào từ bàn phím hoặc in ra màn hình.

Cần phân biệt: **thuật toán** (phương pháp giải bài toán) và **chương trình** (cách hiện thực thuật toán bằng ngôn ngữ và môi trường cụ thể). Một thuật toán có thể được viết bằng nhiều ngôn ngữ; cùng một chương trình có thể có lỗi nếu không đáp ứng đặc tả.

## 3. Trình tự tư duy hoặc thực thi

1. Xác định dữ liệu ban đầu: giá và số lượng.
2. Tính thành tiền bằng phép nhân.
3. Biểu diễn kết quả qua `print()`.
4. Thay đổi đầu vào và kiểm tra kết quả.

## 4. Ví dụ có thể chạy

```python
gia = 12_000
so_luong = 3
thanh_tien = gia * so_luong
print("Thành tiền:", thanh_tien)
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Thành tiền: 36000
```

**Giải thích:** `12_000` là số nguyên 12000; dấu gạch dưới chỉ giúp đọc số. Python gán giá trị cho `gia`, sau đó lấy hai giá trị nhân với nhau và chuyển kết quả đến `print()`. Thứ tự thực hiện phụ thuộc câu lệnh và biểu thức, không phải toàn bộ các câu lệnh luôn chạy song song.

## 5. Trường hợp biên và lỗi thường gặp

Nếu `so_luong = 0`, kết quả là 0; nếu số lượng âm, phép nhân vẫn chạy, nhưng **quy tắc nghiệp vụ** có thể không cho phép. Đây là khác biệt giữa chạy đúng cú pháp và xử lý đúng yêu cầu.

## 6. So sánh dễ nhầm lẫn

Không đồng nhất “chương trình chạy không lỗi” với “chương trình đúng”; độ đúng phải so sánh với yêu cầu và ca kiểm thử.

## 7. Thực hành có lời giải riêng

Viết chương trình tính tổng tiền của bốn quyển vở giá 8.500 đồng/quyển. Đổi sang số lượng 0, giải thích kết quả.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A01.01_loi_giai.md](LOI_GIAI/A01.01_loi_giai.md) — chỉ xem sau khi tự làm.

## 8. Bài tự làm mở rộng

Tính tổng tiền gồm giá sản phẩm và phí vận chuyển cố định 15.000 đồng. Hãy giải thích trường hợp số lượng bằng 0 có còn thu phí vận chuyển không: đây là quyết định về yêu cầu, không phải vấn đề cú pháp.

## 9. Tự kiểm tra khả năng hiểu

1. Chương trình khác thuật toán như thế nào?
2. Vì sao mã chạy được chưa chắc giải quyết đúng bài toán?
3. Khi giá không đổi nhưng số lượng đổi, những câu lệnh nào cần thay đổi?

## 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

## 11. Nguồn

- https://docs.python.org/3.15/tutorial/introduction.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Chương trình là chuỗi thao tác có thứ tự; phép tính chạy được chưa có nghĩa đầu vào hợp lệ về mặt nghiệp vụ.

### Cách suy luận và thiết kế lời giải

Đầu tiên xác lập hợp đồng: giá và số lượng là số nguyên không âm; loại trừ bool vì bool cũng là int trong Python. Sau đó tính thành tiền từ hai biến đã qua xác thực. Thử thêm trường hợp 0 và dữ liệu âm để phân biệt logic với lỗi cú pháp.

### Phản ví dụ và ngộ nhận cần tránh

Không nhầm thao tác print với giá trị return. Nếu ghi kết quả ra màn hình mà không return, hàm không trả về giá trị để kiểm thử hoặc tái sử dụng.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`A01.01_bai_tap_da_giai_v25.py`](MA_MAU/A01.01_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`A01.01_loi_giai.md`](LOI_GIAI/A01.01_loi_giai.md).
5. **Bài mở rộng:** Hãy đổi hợp đồng để cho phép đơn giá thập phân: giải thích vì sao xử lý tiền nên dùng Decimal thay vì float.

**Nguồn kỹ thuật chính thức:** https://docs.python.org/3.15/tutorial/introduction.html. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# A01.02 — Python trong hệ sinh thái lập trình

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A01 — Chương trình và Python · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

## 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Python trong hệ sinh thái lập trình** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

## 2. Khái niệm và bản chất

**Python** là ngôn ngữ lập trình đa mục đích, nổi bật ở cú pháp dễ đọc và hệ sinh thái phong phú. Bản thân ngôn ngữ Python khác với **trình triển khai** (implementation) chạy nó: CPython, PyPy và các triển khai khác không nhất thiết có cùng cấu trúc nội bộ.

**Thư viện chuẩn** đi kèm Python cung cấp nhiều chức năng như xử lý đường dẫn, JSON, ngày giờ và kiểm thử. **Thư viện bên thứ ba** được cài riêng, chẳng hạn NumPy hoặc pandas. **Framework** định hình cách tổ chức ứng dụng (ví dụ một ứng dụng web), khác với thư viện chỉ được gọi khi cần.

## 3. Trình tự tư duy hoặc thực thi

1. Chọn vấn đề phù hợp: tự động hóa tác vụ lặp lại.
2. Kiểm tra chức năng có trong thư viện chuẩn trước.
3. Chỉ thêm thư viện ngoài khi có lợi ích rõ và chấp nhận được chi phí bảo trì.
4. Ghi rõ phụ thuộc và phiên bản cho dự án.

## 4. Ví dụ có thể chạy

```python
from pathlib import Path

thu_muc_hien_tai = Path.cwd()
print("Đã xác định thư mục:", isinstance(thu_muc_hien_tai, Path))
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Đã xác định thư mục: True
```

**Giải thích:** `pathlib` là thư viện chuẩn, không cần cài bằng pip. Lệnh `from ... import ...` lấy một tên từ module. `Path.cwd()` cho biết thư mục làm việc hiện hành; đường dẫn thực tế thay đổi tùy máy.

## 5. Trường hợp biên và lỗi thường gặp

Không mặc định Python phù hợp với mọi hệ thống: nhiệm vụ điều khiển thời gian thực nghiêm ngặt, nền tảng đặc thù hoặc yêu cầu tài nguyên rất hạn chế có thể đòi hỏi công nghệ khác. Thư viện ngoài không đồng nghĩa với chất lượng đã được kiểm chứng.

## 6. So sánh dễ nhầm lẫn

**Ngôn ngữ** là quy tắc cú pháp/ngữ nghĩa; **implementation** thực hiện quy tắc; **module/thư viện** cung cấp chức năng; **framework** cung cấp bộ khung ứng dụng.

## 7. Thực hành có lời giải riêng

Phân loại các thành phần `Python`, `CPython`, `json`, `pandas`, `Django` vào ngôn ngữ, triển khai, thư viện chuẩn, thư viện bên thứ ba hoặc framework.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A01.02_loi_giai.md](LOI_GIAI/A01.02_loi_giai.md) — chỉ xem sau khi tự làm.

## 8. Bài tự làm mở rộng

So sánh khi nào nên viết script Python thuần với khi nào cần thêm thư viện ngoài. Nêu tiêu chí: độ tin cậy, bảo mật, giấy phép, công sức bảo trì.

## 9. Tự kiểm tra khả năng hiểu

1. CPython có phải là toàn bộ định nghĩa của Python không?
2. Thư viện chuẩn khác thư viện ngoài ở điểm nào?
3. Vì sao dùng ít dependency có thể làm ứng dụng dễ bảo trì hơn?

## 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

## 11. Nguồn

- https://docs.python.org/3.15/library/index.html
- https://docs.python.org/3.15/reference/introduction.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


---

# A01.03 — Mã nguồn, trình thông dịch, bytecode và CPython

> **Trạng thái:** ĐÃ BIÊN SOẠN NỘI DUNG · Ví dụ được kiểm thử bằng Python 3.13.5 (kết quả trong `09_NHAT_KY_KIEM_THU.md`) · **CHƯA** kiểm thử CPython 3.15.2.  
> **Chương:** A01 — Chương trình và Python · **Giai đoạn:** GD0 · **Phiên bản mục tiêu:** CPython 3.15.2.

## 1. Mục tiêu có thể kiểm tra

Sau bài này, người học phải (1) giải thích được **Mã nguồn, trình thông dịch, bytecode và CPython** bằng từ ngữ của mình; (2) chạy và giải thích ví dụ; (3) nhận diện ít nhất một trường hợp biên; (4) giải ít nhất một bài tập mà không sao chép lời giải.

**Tiên quyết:** Không yêu cầu kiến thức lập trình trước đó.

## 2. Khái niệm và bản chất

**Mã nguồn** là văn bản trong tệp `.py`. **CPython** thường phân tích/cấu trúc mã nguồn, biên dịch sang một dạng **bytecode** rồi thực thi qua máy ảo Python; đó là mô tả của CPython, không phải bảo đảm rằng mọi triển khai đều chạy y hệt.

**Bytecode không phải mã máy CPU**, và `.pyc` là dạng lưu cache của bytecode trong một số trường hợp để tái sử dụng. Không nên yêu cầu người nhập môn phải hiểu từng opcode. `dis` giúp quan sát bytecode, nhưng opcode và các tối ưu có thể khác theo phiên bản. Một số lệnh `python -c`, REPL hoặc mã trong module có thể không tạo `.pyc` trong thư mục hiện hành.

## 3. Trình tự tư duy hoặc thực thi

1. Viết mã nguồn trong tệp `.py`.
2. Gọi Python để chạy tệp.
3. CPython thực hiện các giai đoạn xử lý nội bộ phù hợp.
4. Các câu lệnh tạo tác động quan sát được; nếu có lỗi, ngoại lệ có thể dừng thực thi.

## 4. Ví dụ có thể chạy

```python
import platform
import sys

print("Python:", sys.version_info.major, sys.version_info.minor)
print("Implementation:", platform.python_implementation())
```

**Đầu ra quan sát được hoặc dự kiến:**

```text
Ví dụ trên CPython 3.15: Python: 3 15
Implementation: CPython
```

**Giải thích:** `sys.version_info` cho biết phiên bản runtime thực tế; `platform.python_implementation()` chỉ tên implementation. Nếu máy đang dùng Python 3.13 hoặc PyPy thì kết quả khác; đây là đầu ra **phụ thuộc môi trường**, không được đóng đinh như kết quả phổ quát.

## 5. Trường hợp biên và lỗi thường gặp

Không suy từ sự tồn tại của `.pyc` rằng mã đã được phân phối an toàn hay được bảo mật. Bytecode có thể bị phân tích. Việc thay đổi phiên bản Python có thể thay đổi opcode dù cú pháp nguồn vẫn hợp lệ.

## 6. So sánh dễ nhầm lẫn

`.py`: mã nguồn. `.pyc`: cache bytecode (khi có). **CPython**: implementation phổ biến. **Python Language Reference**: tài liệu mô tả ngữ nghĩa ngôn ngữ.

## 7. Thực hành có lời giải riêng

Chạy một lệnh in ra phiên bản và implementation trên máy cá nhân. Ghi kết quả thực tế thay vì sao chép kết quả minh họa.

**Gợi ý:** Viết dữ liệu thử, dự đoán kết quả, chạy trên máy, đối chiếu.  
**Lời giải mẫu:** [A01.03_loi_giai.md](LOI_GIAI/A01.03_loi_giai.md) — chỉ xem sau khi tự làm.

## 8. Bài tự làm mở rộng

Đọc `dis.dis(lambda x: x + 1)`, mô tả bạn quan sát được, nhưng không mặc định cùng opcode xuất hiện trên mọi phiên bản.

## 9. Tự kiểm tra khả năng hiểu

1. Bytecode có phải ngôn ngữ máy của CPU không?
2. Mọi triển khai Python có buộc tạo `.pyc` không?
3. Vì sao ví dụ liên quan `dis` cần ghi rõ phiên bản?

## 10. Tóm tắt và tiêu chí hoàn thành

Bạn hoàn thành bài khi giải thích được khái niệm, tự chạy ví dụ, phát hiện sai lầm thường gặp, nộp tệp bài tập và đối chiếu ít nhất ba đầu vào (thường/biên/không hợp lệ nếu có).

## 11. Nguồn

- https://docs.python.org/3.15/reference/executionmodel.html
- https://docs.python.org/3.15/library/dis.html

**Phân biệt nguồn:** Các đoạn giải thích và bài tập là phần tổng hợp, biên soạn mới dựa vào tài liệu chuẩn; không phải bản dịch nguyên văn sách PDF.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: A01.01, A01.02, A01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
