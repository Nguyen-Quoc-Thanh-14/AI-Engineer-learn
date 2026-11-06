# Hướng dẫn nhận việc phản biện chuyên gia độc lập

Workflow GitHub Actions: .github/workflows/expert-review-packets.yml.
Chương trình: tests/generate_expert_review_packets.py.

Artifact unsigned-expert-review-assignments-not-certification có 520 lượt phân công cho 441 bài, trong đó 79 bài thuộc nhóm rủi ro cao phải có hai người phản biện độc lập. Mỗi dòng mang SHA-256 của bài học, demo, lời giải và mã B riêng khi tồn tại. Bộ sinh KHÔNG tạo người phản biện, hồ sơ đánh giá hay chữ ký.

Người điều phối phải mời người có chuyên môn thật; reviewer đọc mã, chạy test, phản biện đề/đáp án, ghi phản ví dụ, issue, commit sửa và retest rồi ký phiếu vào docs/review/INDEPENDENT_REVIEW_SIGNOFFS.csv đúng checksum. Các bài đã đổi checksum phải phản biện lại phần thay đổi. Cổng phần mềm không được tự xác minh danh tính hoặc cấp chứng nhận.

Sử dụng docs/review/PEER_REVIEW_RUBRIC.md và docs/review/INDEPENDENT_REVIEW_PROCESS.md để nghiệm thu. Không biến artifact phân công thành bằng chứng đã có 520 lượt review.
