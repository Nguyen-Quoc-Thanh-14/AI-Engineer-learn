# Quyết định phát hành — kiểm tra trước khi công bố

Cập nhật kiểm kê ngày **07/11/2026**. Tài liệu này ghi nhận bằng chứng bản xem trước, **không phải quyết định xuất bản chính thức**.

| Hạng mục | Điều kiện tối thiểu | Trạng thái đã đối chiếu |
|---|---|---|
| Nội dung | 441 bài + lời giải cùng ID, mục lục đầy đủ | Đã qua kiểm kê tự động tại bản dựng; chưa thay thế phản biện chuyên môn |
| Đóng gói | 5 tập học viên + 5 tập lời giải; Markdown, HTML, EPUB3 | **ĐẠT BẢN XEM TRƯỚC**: 10 Markdown, 10 HTML, 10 EPUB3, 441/441 bài, 137 chương |
| Liên kết | Không mất đích nội bộ trong bản đóng gói | Bộ quét tự động báo 0 đích thiếu; không bảo đảm mọi URL ngoài còn truy cập được |
| Khả năng đọc | Kiểm tra HTML/EPUB thủ công, tiếng Việt, code dài, bảng, công thức, ảnh | **CHƯA KÝ** |
| Quyền sử dụng | Xác minh quyền tác giả, ghi công, nguồn, hình và giấy phép | **CHƯA KÝ** |
| Chứng cứ kỹ thuật | Tuyên bố luôn gắn workflow và SHA được kiểm tra | Đã kiểm tra workflow đóng gói; không suy rộng sang chứng nhận GPU/CPU trên SHA biên tập |
| Phản biện | Danh tính, phạm vi, số phiếu người đánh giá độc lập có bằng chứng | **CHƯA ĐẠT**: Issue #7 |
| GPU CUDA thật | Log runner NVIDIA, bài thử thực tế, artifact nguồn xác minh | **CHƯA ĐẠT**: Issue #8 |
| Content QA | Phân xử cờ heuristic, rà soát nội dung trước khi công bố | **ĐANG THEO DÕI**: Issue #9 |
| Quyết định xuất bản | Chủ sở hữu ký duyệt, ngày phát hành, số phiên bản, kênh, giấy phép | **CHƯA CÓ** |

## Bằng chứng đóng gói đã xác minh

- Pull request biên tập: https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/pull/10
- Source SHA bản dựng: `f2a7430b973465b65714543d6c177e6ab8c85ade`
- Workflow thành công: https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42248515986
- Artifact: `python-course-five-volumes-editorial-PREVIEW-not-certified` (ID `13519272866`).
- Workflow đã ghi nhận 441 bài, 137 chương, 10 Markdown, 10 HTML, 10 EPUB3, không có liên kết thiếu đích trong phép quét.

**Cảnh báo về SHA:** Bằng chứng workflow trên áp dụng cho `f2a7430...` và không tự động chứng minh bất kỳ commit phát sinh sau đó đã được dựng và kiểm thử lại.

## Điều kiện nghiệm thu bản xem trước

- [x] Dựng 5 tập học viên + 5 tập lời giải thành Markdown, HTML, EPUB3.
- [x] Ghi rõ phạm vi bản xem trước và không sử dụng nhãn chứng nhận.
- [ ] Người đọc thử mở đủ 10 ấn bản HTML và 10 EPUB, rà 2 bài mỗi tập, bảng, công thức, code, liên kết và font Unicode.
- [ ] Chốt tác giả, người đóng góp, nguồn hình, quyền tái bản, giấy phép và điều kiện chia sẻ.
- [ ] Phân xử hoặc công bố minh bạch các tồn đọng có ảnh hưởng theo Issue #9.
- [ ] Chủ sở hữu phê duyệt rõ bản cuối, kênh phân phối, ngày phát hành và phiên bản.

**Được phép:** chia sẻ **bản xem trước, chưa phát hành** cho người đọc thử *sau khi kiểm tra quyền chia sẻ*.

**Không được tự động thực hiện:** merge vào `main`, merge Draft PR #4, tạo GitHub Release chính thức, đăng bán, xin ISBN, dùng tên chuyên gia ẩn danh hoặc xác nhận giáo trình đã được chứng nhận toàn diện.

Việc tiếp tục biên tập không phụ thuộc vào việc hoàn tất CUDA hay toàn bộ phản biện; tuy nhiên không được quảng bá các năng lực hoặc chứng nhận chưa có bằng chứng.
