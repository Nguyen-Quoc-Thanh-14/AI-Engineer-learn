# Chương PM01

> Bản đọc gộp v2.5, sinh trực tiếp từ file bài học.

## Nội dung các bài học — đồng bộ v2.5


---

# PM01.01 — Định nghĩa bài toán và baseline

> **Trạng thái:** ĐÃ BIÊN SOẠN BẢN THẢO CHUYÊN BIỆT; VÍ DỤ VÀ LỜI GIẢI CHẠY ĐẠT PYTHON 3.13.5.
> **Giai đoạn:** GD6 · **Chương:** PM01 — Quy trình ML · **Đích:** CPython 3.15.2.

## 1. Chuẩn đầu ra có thể kiểm chứng

1. Tự giải thích khái niệm **Định nghĩa bài toán và baseline**, nêu một trường hợp nên và không nên áp dụng.
2. Dự đoán trạng thái/kết quả ví dụ trước khi chạy và giải thích từng bước.
3. Viết một lời giải độc lập, xử lý ít nhất ba trường hợp (bình thường, biên, sai đầu vào).
4. Chỉ ra giả định, giới hạn và đối chiếu kết quả bằng kiểm thử.

**Tiên quyết:** PD, PT, H.

## 2. Khái niệm — Bản chất

Quy trình ML bắt đầu bằng định nghĩa bài toán, metric, baseline và cơ chế phân tách train/validation/test. Baseline đơn giản là chuẩn so sánh cần phải vượt qua; nếu không, mô hình phức tạp không có bằng chứng cải thiện. Không được chọn mô hình bằng cách nhìn kết quả test nhiều lần.

## 3. Nguyên lý và cơ chế từng bước

Ví dụ baseline dự đoán lớp đa số. Dataset nhỏ và không dùng sklearn để tránh ràng buộc môi trường; quan trọng là thống kê tỉ lệ lỗi, không phải đạt độ chính xác cao trên mẫu minh họa.

## 4. Ví dụ tối thiểu có thể chạy

```python
from collections import Counter
train=[0,1,0,0,1]
test=[0,1,0]
majority=Counter(train).most_common(1)[0][0]
preds=[majority]*len(test)
accuracy=sum(a==b for a,b in zip(preds,test))/len(test)
assert accuracy==2/3
print('baseline accuracy:',round(accuracy,3))
```

**Kết quả kiểm thử cục bộ:** pass trên Python 3.13.5.

```text
baseline accuracy: 0.667
```

**Thực hành:** chạy file `07_MA_VI_DU/PM01.01_vi_du.py` từ thư mục gốc giáo trình rồi sửa một tham số để dự đoán sự khác biệt.

## 5. Trường hợp biên, lỗi thường gặp và hướng debug

- **Ngộ nhận:** Accuracy cao trên tập mất cân bằng có thể vô nghĩa; cân nhắc precision/recall theo chi phí lỗi.
- **Trường hợp biên:** Nếu test có phân phối khác train, baseline cũng cần đánh giá theo kịch bản triển khai.
- **Debug có phương pháp:** xác định hợp đồng → tái hiện lỗi bằng đầu vào tối thiểu → đọc traceback/kiểm tra trạng thái → sửa → thêm regression test.

## 6. So sánh lựa chọn kỹ thuật và đánh đổi

Tránh đầu tư mô hình nếu chưa biết metric và cách so sánh thành công.

## 7. Bài tập có yêu cầu kiểm chứng

Thiết kế baseline cho dự đoán số: giá trị trung bình train; đánh giá MAE trên test.

**Bài tập độc lập:** bổ sung ca thử bình thường, biên, sai dữ liệu; giải thích đầu ra và một cách triển khai khác. Không xem lời giải mẫu trước khi tự viết.

**Lời giải:** [PM01.01_loi_giai.md](LOI_GIAI/PM01.01_loi_giai.md).

## 8. Câu hỏi kiểu mentor để tự đánh giá

1. Nếu chỉ được giải thích nguyên lý bằng ba câu, bạn sẽ giữ lại những điều kiện nào và vì sao?
2. Nếu thay đổi dữ liệu đầu vào thành rỗng, trùng, âm hoặc sai kiểu, quy tắc nào có thể thất bại?
3. Bạn sẽ dùng thử nghiệm nào để phản chứng lời giải hiện tại?
4. Trong trường hợp thực tế nào **Định nghĩa bài toán và baseline** mang lại lợi ích lớn hơn độ phức tạp bổ sung?

## 9. Tiêu chí đạt và tự chấm

- [ ] Nói được khái niệm và cơ chế mà không nhìn đáp án.
- [ ] Chạy thành công ví dụ và ghi phiên bản runtime.
- [ ] Viết lời giải riêng, có ít nhất ba ca kiểm thử.
- [ ] Nhận diện và giải thích một cách làm sai hoặc giả định không hợp lệ.
- [ ] Nêu được tình huống lựa chọn phương pháp thay thế.

## 10. Nguồn và giới hạn

- [S03] Hands-On Machine Learning 2e — tài liệu PDF trong bộ nguồn gốc; cần đối chiếu phiên bản API mới.
- [R25] [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — Chính thức thư viện.
- [R26] [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — Chính thức thư viện.

Giải thích và bài tập được biên soạn mới để học tập; dùng các nguồn nêu trên để đối chiếu, không sao chép nguyên văn sách.
**Chưa kiểm chứng:** tính tương thích trực tiếp với CPython 3.15.2; kiểm định sư phạm độc lập; độ tương thích các bộ thư viện trên máy người học.


---

# PM01.02 — Train/validation/test split

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PM01 — Quy trình ML · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PT, H. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Train/validation/test split** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Train dùng để fit, validation để chọn model/hyperparameters, test để đánh giá cuối; các tập phải độc lập theo thực thể/thời gian khi cần.

**Ngữ cảnh thực tế:** Trong chương **Quy trình ML**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Tạo split trước mọi preprocessing học từ dữ liệu; tránh chia ngẫu nhiên khi có leakage nhóm.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
from sklearn.model_selection import train_test_split
x=list(range(100))
a,b=train_test_split(x,test_size=.2,random_state=42)
assert len(a)==80 and len(b)==20 and set(a).isdisjoint(b)
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PM01.02_demo.py`](MA_MAU/PM01.02_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Nếu dùng test set để tune nhiều lần, test không còn đánh giá độc lập.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Chia dataset theo user ID thay vì mỗi record và giải thích leakage.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PM01_02.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PM01.02_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S03: Hands-On Machine Learning 2e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R25: scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [R26: scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.

---

## 11. Bài chuyên sâu bổ sung v2.5 — kiểm định bằng chương trình thực thi

> **Kết quả:** Đã chạy thành công lời giải độc lập trên Python 3.13.5 tại thời điểm xuất bản v2.5. **Chưa kiểm định trực tiếp trên CPython 3.15.2; chưa qua phản biện sư phạm độc lập.**

### Nguyên lý cần nắm

Chia dữ liệu phải dựa vào đơn vị độc lập phù hợp: nếu các bản ghi của cùng một người rơi vào train và test, mô hình có thể học thông tin về người đó thay vì tổng quát hóa.

### Cách suy luận và thiết kế lời giải

Dùng user ID làm đơn vị phân chia; sắp xếp groups và shuffle bằng Random(seed) để tái lập. Chia ba tập train/validation/test theo nhóm, không theo record; kiểm tra giao nhau của tập user IDs sau khi chia. Với dữ liệu thời gian, chiến lược split sẽ khác.

### Phản ví dụ và ngộ nhận cần tránh

Không chia ngẫu nhiên từng record trước rồi chỉ kiểm tra tỷ lệ 80/20; điều đó không chứng minh độc lập theo nhóm. Không fit preprocessing trên toàn bộ dữ liệu trước khi chia.

### Lộ trình tự kiểm tra

1. Đọc yêu cầu bài tập ở trên, tự viết lời giải **trước khi mở đáp án**.
2. Dự đoán đầu ra các trường hợp bình thường, biên và không hợp lệ; nói rõ từng precondition, hậu điều kiện.
3. Chạy mã độc lập [`PM01.02_bai_tap_da_giai_v25.py`](MA_MAU/PM01.02_bai_tap_da_giai_v25.py) để đối chiếu.
4. Kiểm tra lời giải chi tiết: [`PM01.02_loi_giai.md`](LOI_GIAI/PM01.02_loi_giai.md).
5. **Bài mở rộng:** Dùng scikit-learn GroupShuffleSplit/GroupKFold khi có thư viện; thảo luận vì sao time series cần TimeSeriesSplit hoặc split theo thời gian.

**Nguồn kỹ thuật chính thức:** https://scikit-learn.org/stable/common_pitfalls.html#data-leakage. Tài liệu được dùng để đối chiếu API/cơ chế, không phải nguồn sao chép nguyên văn bài này.


---

# PM01.03 — Leakage, metrics và cross-validation

> **Trạng thái biên soạn:** BẢN THẢO CHUYÊN BIỆT CÓ NỘI DUNG; ĐÃ CHẠY ĐẠT — Python 3.13.5. **Chưa phản biện sư phạm độc lập.**  
> **Giai đoạn:** GD6 · **Chương:** PM01 — Quy trình ML · **Python đích:** CPython 3.15.2.

## 1. Điều kiện tiên quyết và chuẩn đầu ra

**Tiên quyết:** PD, PT, H. Trước bài này, cần nắm khái niệm đã dùng trong chương.

Sau bài học, bạn phải làm được: (i) giải thích **Leakage, metrics và cross-validation** không cần nhìn mã; (ii) dự đoán đầu ra và diễn giải từng bước; (iii) sửa/áp dụng ví dụ; (iv) nêu được một giới hạn, một lỗi biên và phương pháp kiểm chứng.

## 2. Khái niệm và vì sao cần học

Data leakage xảy ra khi thông tin ngoài thời điểm dự đoán lọt vào training; CV đánh giá khả năng khái quát nếu split phù hợp.

**Ngữ cảnh thực tế:** Trong chương **Quy trình ML**, nội dung này giúp quyết định cách thiết kế/kiểm tra giải pháp khi dự án có đầu vào hoặc yêu cầu thay đổi. Không chọn kỹ thuật chỉ vì cú pháp ngắn; cần xem tính đúng, độ rõ ràng và hành vi lỗi.

## 3. Cơ chế — mô hình thực thi

Đặt transformations fit trong Pipeline của fold training; chọn metric theo cost của false positives/negatives.

**Quy trình phân tích:** Xác định dữ liệu đầu vào và điều kiện hợp lệ → theo dõi thứ tự đánh giá và thay đổi trạng thái → kiểm tra kết quả đầu ra và exception → đối chiếu với contract, không chỉ với một lần chạy.

## 4. Ví dụ độc lập, có assertion

```python
from sklearn.model_selection import KFold
cv=KFold(n_splits=3,shuffle=True,random_state=1)
splits=list(cv.split(range(9)))
assert len(splits)==3 and all(set(a).isdisjoint(b) for a,b in splits)
```

**Trạng thái thực thi:** ĐÃ CHẠY ĐẠT — Python 3.13.5. Mã nguồn độc lập tại [`PM01.03_demo.py`](MA_MAU/PM01.03_demo.py). `assert` trong ví dụ dùng làm phép thử minh họa, không thay thế test suite đầy đủ.

**Cách tự học với ví dụ:** Che phần assertion cuối, dự đoán kết quả theo cơ chế phần 3; sau đó chạy và so sánh. Thử thay một input hợp lệ và một input vi phạm contract.

## 5. Trường hợp biên và lỗi thường gặp

Fit scaler trên toàn bộ dataset trước CV làm rò thống kê từ validation fold.

**Bảng kiểm tự thực hiện:**

| Tình huống | Cần kiểm tra |
|---|---|
| Đầu vào thường | Hành vi đúng hợp đồng; không phát sinh side effect không dự kiến |
| Đầu vào rỗng/giá trị biên | Cách trả kết quả, lỗi và fallback có được mô tả? |
| Đầu vào sai/ngoài miền | Có từ chối rõ ràng, không gây mất dữ liệu hay lộ thông tin? |

## 6. Bài tập tự làm

**Bài A — Phân tích:** Tự giải thích kết quả của đoạn mã ở phần 4, nêu rõ ít nhất hai bước thực thi và kiểm tra trường hợp biên.

**Bài B — Ứng dụng:** Tạo Pipeline(StandardScaler, LogisticRegression) và so CV sai/đúng.

**Bài C — Phản biện:** Thử một giải pháp thay thế, so sánh về tính đúng, chi phí bảo trì/hiệu năng và độ an toàn trong tình huống có input không tin cậy.

**Bài D — Kiểm thử:** Viết tối thiểu ba ca thử, trong đó có một ca sai đầu vào; lưu thành `test_PM01_03.py`. Không viết `except: pass` để che lỗi.

## 7. Hướng dẫn giải và tiêu chí đạt

[Mở hướng dẫn / lời giải mẫu](LOI_GIAI/PM01.03_loi_giai.md). **Tình trạng:** mẫu tham khảo; lời giải bài vận dụng chưa được kiểm định.

Chỉ tự công nhận đạt khi: (1) giải thích đúng khái niệm và giới hạn; (2) dự đoán đúng ví dụ trước khi chạy; (3) bài B chạy với ít nhất ba ca thử có assertions cụ thể; (4) có thể giải thích vì sao chọn cách làm này thay cho giải pháp khác.

## 8. Tài liệu kiểm chứng

- S03: Hands-On Machine Learning 2e (nguồn người dùng cung cấp; tra trong thư mục tài liệu gốc)
- [R25: scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [R26: scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)

**Ghi chú:** Nguồn dùng để đối chiếu khái niệm và các mốc phiên bản, không hàm ý toàn bộ ví dụ trong bài có trong tài liệu gốc. Nếu có tính năng phụ thuộc phiên bản hoặc thư viện ngoài, phải chạy lại trên môi trường thực tế trước khi nâng trạng thái xuất bản.


## Cập nhật chất lượng v2.7

Đã cập nhật file bài lẻ: PM01.01, PM01.03. Ưu tiên đọc file bài lẻ để xem lời giải và demo mới, báo cáo kiểm thử tại thư mục `30_KIEM_DINH_V27`. Các bài chưa được kiểm thử trên Python 3.15.2 vẫn giữ trạng thái cần xác minh.
