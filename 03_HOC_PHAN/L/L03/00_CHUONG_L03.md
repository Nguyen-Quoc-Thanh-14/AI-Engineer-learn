# L03 — Thư viện đồng thời (bản cập nhật v2.7)

Bản trước đã nhầm nội dung asyncio sang các mã bài về thread/process. Đã chỉnh lại cả ba bài như dưới đây.


---

# L03.01 — threading và concurrent.futures

> **Bản sửa lỗi chuyên môn v2.7:** nội dung của bản trước dùng ví dụ asyncio không khớp tiêu đề. Bản này viết lại đúng chủ đề; **đã chạy kiểm tra riêng trên CPython 3.13.5**, chưa được xác minh trên CPython 3.15.2.

## 1. Tiên quyết và mục tiêu

Cần nắm hàm, module, exception, biến chia sẻ, process/thread và khả năng đọc traceback. Người học phải giải thích được cơ chế, viết ví dụ có kiểm thử và nhận biết rủi ro khi chạy thật.

## 2. Khái niệm và cơ chế

Threading dùng nhiều thread cùng không gian bộ nhớ; với I/O-bound, chờ I/O cho phép thread khác tiến hành. ThreadPoolExecutor quản lý worker pool và Future, nhưng không tự chứng minh chương trình thread-safe. CPython có GIL ở build mặc định; điều này không biến mọi phép cập nhật chia sẻ thành atomic contract.

## 3. Ví dụ làm việc độc lập

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def fetch_record(record_id):
    sleep(0.001)
    return {'id': record_id, 'value': record_id * 2}

def run_jobs(items):
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(fetch_record, item) for item in items]
        return [future.result(timeout=2) for future in futures]

if __name__ == '__main__':
    assert run_jobs([1, 2, 3]) == [
        {'id': 1, 'value': 2}, {'id': 2, 'value': 4}, {'id': 3, 'value': 6}]
    assert run_jobs([]) == []
    assert run_jobs([5])[0]['value'] == 10
    print('PASS L03.01')
```

Chạy `python -I ../MA_MAU/L03.01_demo.py` từ thư mục `BAI_HOC`, hoặc mở mã tại [demo](MA_MAU/L03.01_demo.py).

## 4. Trường hợp biên và sai lầm thường gặp

Đừng dùng CPU-bound thuần Python làm minh chứng tốc độ thread; tránh phụ thuộc thứ tự hoàn tất và dùng Future.result(timeout=...) khi cần hạn chờ.

## 5. Bài tập vận dụng

**Bài B — Ứng dụng:** Viết hàm xử lý 3 công việc I/O giả lập bằng ThreadPoolExecutor; kiểm ba kết quả, timeout và dọn pool bằng context manager.

- Chạy với đầu vào thường và đầu vào rỗng.
- Kiểm tra lỗi/timeout hay schema bất hợp lệ tùy bài.
- Dùng các test tách biệt trong dự án thực, không chỉ dựa trên assertions của ví dụ.

## 6. Lời giải và tiêu chí đạt

[Lời giải vận dụng](LOI_GIAI/L03.01_loi_giai.md) và [mã kiểm thử](MA_MAU/L03.01_bai_tap_da_giai_v27.py). Người học phải tự giải thích vì sao chọn thread/process/IPC, nêu hạn chế và chạy lại ở môi trường đích.

## 7. Tài liệu đối chiếu

- [Python 3.15 — Tài liệu chính thức](https://docs.python.org/3.15/library/concurrent.futures.html)
- [Python 3.15 — Free-threaded builds](https://docs.python.org/3.15/howto/free-threading-python.html)

Không suy diễn rằng `assert` đã xác minh hết tính đúng, hiệu năng hay khả năng an toàn của chương trình.


---

# L03.02 — ProcessPoolExecutor và multiprocessing

> **Bản sửa lỗi chuyên môn v2.7:** nội dung của bản trước dùng ví dụ asyncio không khớp tiêu đề. Bản này viết lại đúng chủ đề; **đã chạy kiểm tra riêng trên CPython 3.13.5**, chưa được xác minh trên CPython 3.15.2.

## 1. Tiên quyết và mục tiêu

Cần nắm hàm, module, exception, biến chia sẻ, process/thread và khả năng đọc traceback. Người học phải giải thích được cơ chế, viết ví dụ có kiểm thử và nhận biết rủi ro khi chạy thật.

## 2. Khái niệm và cơ chế

ProcessPoolExecutor phân phối công việc tới các process riêng, thường phù hợp với CPU-bound thuần Python vì mỗi process có interpreter và bộ nhớ riêng. Đối tượng đối số và kết quả cần serialize; worker callable nên khai báo ở module top-level; mọi mã tạo pool phải bảo vệ bằng if __name__ == "__main__" để hỗ trợ cơ chế spawn.

## 3. Ví dụ làm việc độc lập

```python
from concurrent.futures import ProcessPoolExecutor

def square(n: int) -> int:
    return n*n

def batch_square(numbers):
    with ProcessPoolExecutor(max_workers=2) as pool:
        return list(pool.map(square, numbers))

if __name__ == '__main__':
    assert batch_square([2, 3, -4]) == [4, 9, 16]
    assert batch_square([0]) == [0]
    assert batch_square([]) == []
    print('PASS L03.02')
```

Chạy `python -I ../MA_MAU/L03.02_demo.py` từ thư mục `BAI_HOC`, hoặc mở mã tại [demo](MA_MAU/L03.02_demo.py).

## 4. Trường hợp biên và sai lầm thường gặp

Không giả định thứ tự hoàn thành giống thứ tự nộp khi dùng as_completed. Dùng pool.map khi cần thứ tự đầu vào; ghi nhận chi phí serialize và process startup.

## 5. Bài tập vận dụng

**Bài B — Ứng dụng:** Viết một worker thuần tính toán và xử lý 3 số bằng ProcessPoolExecutor, có kiểm thử số 0 và số âm; không tạo pool tại thời điểm import.

- Chạy với đầu vào thường và đầu vào rỗng.
- Kiểm tra lỗi/timeout hay schema bất hợp lệ tùy bài.
- Dùng các test tách biệt trong dự án thực, không chỉ dựa trên assertions của ví dụ.

## 6. Lời giải và tiêu chí đạt

[Lời giải vận dụng](LOI_GIAI/L03.02_loi_giai.md) và [mã kiểm thử](MA_MAU/L03.02_bai_tap_da_giai_v27.py). Người học phải tự giải thích vì sao chọn thread/process/IPC, nêu hạn chế và chạy lại ở môi trường đích.

## 7. Tài liệu đối chiếu

- [Python 3.15 — Tài liệu chính thức](https://docs.python.org/3.15/library/concurrent.futures.html#processpoolexecutor)
- [Python 3.15 — Free-threaded builds](https://docs.python.org/3.15/howto/free-threading-python.html)

Không suy diễn rằng `assert` đã xác minh hết tính đúng, hiệu năng hay khả năng an toàn của chương trình.


---

# L03.03 — Inter-process communication và serialization

> **Bản sửa lỗi chuyên môn v2.7:** nội dung của bản trước dùng ví dụ asyncio không khớp tiêu đề. Bản này viết lại đúng chủ đề; **đã chạy kiểm tra riêng trên CPython 3.13.5**, chưa được xác minh trên CPython 3.15.2.

## 1. Tiên quyết và mục tiêu

Cần nắm hàm, module, exception, biến chia sẻ, process/thread và khả năng đọc traceback. Người học phải giải thích được cơ chế, viết ví dụ có kiểm thử và nhận biết rủi ro khi chạy thật.

## 2. Khái niệm và cơ chế

Các process có không gian bộ nhớ tách biệt. IPC có thể qua Pipe hoặc Queue; dữ liệu cần serialize khi trao đổi. Không giải mã pickle đến từ nguồn không tin cậy: pickle có khả năng thực thi mã trong lúc unpickle. Dùng thông điệp JSON có schema rõ cho ranh giới ít tin cậy, với giới hạn kích thước và kiểm tra kiểu.

## 3. Ví dụ làm việc độc lập

```python
from multiprocessing import Pipe, Process
import json

def worker(conn):
    try:
        for value in (2, 3):
            conn.send_bytes(json.dumps({'kind': 'square', 'value': value**2}).encode('utf-8'))
    finally:
        conn.close()

def receive_messages():
    parent, child = Pipe(duplex=False)
    proc = Process(target=worker, args=(child,))
    proc.start(); child.close()
    out = []
    try:
        for _ in range(2):
            if not parent.poll(3): raise TimeoutError('worker did not send')
            message = json.loads(parent.recv_bytes(maxlength=1024))
            if set(message) != {'kind', 'value'} or message['kind'] != 'square' or type(message['value']) is not int:
                raise ValueError('unexpected payload')
            out.append(message['value'])
    finally:
        parent.close()
        proc.join(timeout=3)
        if proc.is_alive(): proc.terminate(); proc.join()
    if proc.exitcode != 0: raise RuntimeError('worker failed')
    return out

if __name__ == '__main__':
    assert receive_messages() == [4, 9]
    assert json.loads(json.dumps({'kind': 'square', 'value': 4}))['value'] == 4
    try:
        unexpected = {'kind': 'delete', 'value': 4}
        if unexpected['kind'] != 'square': raise ValueError('schema')
    except ValueError: pass
    else: raise AssertionError
    print('PASS L03.03')
```

Chạy `python -I ../MA_MAU/L03.03_demo.py` từ thư mục `BAI_HOC`, hoặc mở mã tại [demo](MA_MAU/L03.03_demo.py).

## 4. Trường hợp biên và sai lầm thường gặp

Một Pipe chứa dữ liệu không tin cậy không được tự động chuyển thành pickle.loads; parent phải kiểm child exitcode và áp dụng timeout trước khi recv để tránh treo.

## 5. Bài tập vận dụng

**Bài B — Ứng dụng:** Tạo hai process truyền JSON qua multiprocessing.Pipe với schema {kind,value}, kiểm cả 2 thông điệp và từ chối schema lạ; đóng các đầu Pipe sau khi sử dụng.

- Chạy với đầu vào thường và đầu vào rỗng.
- Kiểm tra lỗi/timeout hay schema bất hợp lệ tùy bài.
- Dùng các test tách biệt trong dự án thực, không chỉ dựa trên assertions của ví dụ.

## 6. Lời giải và tiêu chí đạt

[Lời giải vận dụng](LOI_GIAI/L03.03_loi_giai.md) và [mã kiểm thử](MA_MAU/L03.03_bai_tap_da_giai_v27.py). Người học phải tự giải thích vì sao chọn thread/process/IPC, nêu hạn chế và chạy lại ở môi trường đích.

## 7. Tài liệu đối chiếu

- [Python 3.15 — Tài liệu chính thức](https://docs.python.org/3.15/library/multiprocessing.html)
- [Python 3.15 — Free-threaded builds](https://docs.python.org/3.15/howto/free-threading-python.html)

Không suy diễn rằng `assert` đã xác minh hết tính đúng, hiệu năng hay khả năng an toàn của chương trình.
