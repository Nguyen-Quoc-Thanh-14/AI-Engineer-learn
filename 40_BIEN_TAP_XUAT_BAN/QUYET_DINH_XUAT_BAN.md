# Quyết định phát hành — kiểm tra trước khi công bố

| Hạng mục | Điều kiện tối thiểu | Trạng thái trong bản thảo |
|---|---|---|
| Nội dung | 441 bài + 441 lời giải cùng ID; mục lục đúng, không có tệp mất | Máy có thể kiểm tra |
| Đóng gói | 5 tập sách và 5 tập lời giải; Markdown/HTML/EPUB | Chờ artifact build |
| Khả năng đọc | Kiểm tra HTML và EPUB thủ công, Unicode, code blocks, bảng, liên kết | Chưa ký |
| Quyền sử dụng | Giấy phép, tên tác giả, đóng góp, trích dẫn/hình minh họa | Chưa ký |
| Chứng cứ kiểm thử | Gắn SHA chuẩn, không dùng kết quả của SHA cũ cho bản mới | Bắt buộc đối chiếu |
| Phản biện | Ghi đúng tính chất phản hồi miệng; không tự nhận chứng nhận | Chưa có phiếu được xác minh |
| CUDA / native | Nếu quảng cáo khả năng phần cứng phải có log GPU/native theo đúng cấu hình | Không đưa ra tuyên bố |
| Quyết định xuất bản | Chủ sở hữu duyệt bản cuối, ngày phát hành, giấy phép, kênh phân phối | CHƯA CÓ |

**Được phép:** chia sẻ bản xem trước cho người đọc thử với nhãn "Bản xem trước, chưa phát hành", khi quyền chia sẻ nội dung đã được chủ sở hữu kiểm tra.

**Chưa được tự động thực hiện:** push lên main, merge Draft PR #4, gắn GitHub Release, xuất bản thương mại, xin ISBN, dùng tên chuyên gia ẩn danh, xác nhận "đã chứng nhận toàn bộ giáo trình".

Quyết định này không buộc phải giải quyết mọi heuristic còn lại trước khi **biên tập**; nhưng các tuyên bố cụ thể về độ đúng, tương thích và an toàn phải dựa trên bằng chứng tương ứng khi **công bố**.
