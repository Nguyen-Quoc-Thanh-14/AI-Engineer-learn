# Issue #9 — Báo cáo kiểm toán nội dung theo nguồn, 06/11/2026

**Phạm vi:** 441 bài học, 441 demo, 441 lời giải tương ứng và 95 chương trình B độc lập, tổng 26 học phần.

**Phân loại:** INTERNAL_TECHNICAL_CONTENT_AUDIT, **không phải** phản biện học thuật độc lập. Việc đọc/quét toàn bộ file bằng mã không đồng nghĩa toàn bộ 441 bài đã được xác minh thủ công về tính đúng sâu.

**Nhánh sửa:** `audit/issue9-content-qa` (tách từ `d1f740b4faa5c8d1361e5427f0d723afd804a2d2`); giữ `main` và PR #4 nguyên trạng, Draft.

## Bằng chứng CI

- [Run #42212670864](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42212670864) — PASS CPython 3.15.2 cho **11** ca H06 Hypothesis / PE02 Parquet / PS02 sensor, **10** ca N02/F04, **7** ca ORM/migration M05/PW02, **3** ca J07 tính năng Python 3.15, **2** ca D06 runtime typing, **5** ca âm tính cho chương trình quét; **38** ca trong các bộ test Issue #9. Không có phiếu phản biện độc lập.
- [Run #42211870740](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42211870740) — kết quả kiểm tra checker D06.03: **Pyright 1.1.414** pass positive (exit 0), reject negative (exit 1); **mypy 2.4.1** reject cả positive và negative (exit 1/1), nên ghi `CHECKER_PARITY_PENDING`, không khẳng định mypy đã hỗ trợ `TypedDict(extra_items=...)`. File `evidence/issue9_content_qa/D06_03_checker_support.json` nằm trong artifact triage.
- [Run #42212590164](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42212590164) — Structural QA PASS ở SHA nội dung trước bộ test cuối.
- Hồi quy full 536 chương trình trên commit nguồn mới vẫn cần kết quả kết thúc; **không được tự gán PASS** cho lần chạy đang thực thi. Trạng thái CI phải đối chiếu lại theo HEAD trước nghiệm thu.

## Chín bài có bằng chứng hiệu đính/bổ sung

| Mã | Phát hiện và hiệu đính | Bằng chứng |
|---|---|---|
| N02.01 | Đáp án cũ chỉ che token, thiếu checklist rotate API key khi bị lộ; bổ sung quy trình khóa/thu hồi/thay key, giới hạn kỹ thuật redaction | 10 N02/F04 tests trong #42212670864 |
| F04.01 | Kiểm thử cũ tuyên bố không chứa secret nhưng không đưa secret giả vào log (vacuous); bổ sung request ID validation, ContextVar reset và redaction | 10 N02/F04 tests |
| M05.01 | Đề yêu cầu ORM User/Order nhưng mã cũ chỉ dùng sqlite3; thay bằng SQLAlchemy Declarative, UNIQUE và FK với SQLite thật | 7 ORM tests |
| PW02.01 | Đề yêu cầu migration tạo FK; mã cũ chỉ `CREATE TABLE` cuối cùng; thay bằng v1→v2 có giữ dữ liệu và kiểm FK enforcement | 7 ORM tests |
| J07.01 | Đề yêu cầu 3 smoke tests Python 3.15, trước đây chỉ có candidate code chưa chạy; thêm lazy import, frozendict, sentinel | 3 runtime tests |
| D06.03 | Đáp án chứa `NotImplementedError` TypeForm, chưa có kiểm tra checker; có fixture dương/âm và phân loại mypy ≠ pyright | 2 runtime tests + checker report |
| H06.01 | Đề Hypothesis/shrinking, trước chỉ trình bày mã ứng viên chưa chạy; bổ sung property-based runtime và shrink `broken_sort` tới ví dụ 1 phần tử | 2 Hypothesis tests |
| PE02.01 | Đề đọc/ghi Parquet và kiểm schema nullable/dtypes; trước chỉ có hướng dẫn, chưa có chạy; thêm Arrow schema 10.000 dòng, snappy vs uncompressed roundtrip | 2 Arrow tests |
| PS02.03 | Đề sensor timezone/units và Parquet; trước chỉ có mô tả; bổ sung validate UTC, DST 2 offsets, mixed-unit/duplicate/null rejection và Parquet roundtrip | 7 sensor tests |

**Lưu ý:** Những bản sửa minh họa này không đại diện cho ứng dụng production; mỗi lời giải mới đều nêu giới hạn. Việc thêm code chưa chứng minh kiểm định chuyên gia hoặc tích hợp toàn ngành.

## Triage toàn bộ 441 bài và 95 B

Chương trình `tests/issue9_content_inventory.py` đọc toàn bộ nguồn bài học, lời giải, demo và B script; ràng buộc SHA-256 từng nguồn, so khớp mã bài, tìm nội dung chưa khớp, kiểm tra AST syntax của B script, lưu CSV tại artifact.

- [Triage mới nhất #42212670864](https://github.com/Nguyen-Quoc-Thanh-14/AI-Engineer-learn/actions/runs/42212670864): **441 lessons, 95 B scripts, 26 học phần, errors=[]**, `INVENTORY_PASS_TRIAGE_PENDING`.
- **93** đáp án dạng thiết kế vẫn cần rà soát, **97** phát biểu phiên bản có thể lỗi thời; tổng **194 bài** có ít nhất một cờ theo bộ quét (các tập chồng lên nhau).
- **Hai** cờ `ANSWER_NO_EMBEDDED_CODE_REVIEW` là M05.01/PW02.01, *không phải lỗi đã xác minh*: lời giải Markdown trỏ tới B code thực thi thay vì chép lại code trong Markdown. Cần giữ link hoạt động; kiểm thử B độc lập đã PASS.
- **Hai** cờ `ANSWER_SNIPPET_DIFFERS_FROM_B_SCRIPT_REVIEW` là N02.01/F04.01, *không phải lỗi đã xác minh*: Markdown có snippet minh họa cách gọi API, còn file B chứa triển khai và kiểm thử; chênh lệch AST là có chủ đích.
- `DESIGN_ANSWER_REVIEW` không tự động là lỗi. Nhiều bài B yêu cầu checklist/kiến trúc/tài liệu, không nhất thiết phải sinh file executable.

## Những phần chưa được chấp nhận

1. **93** đáp án thiết kế: phân nhóm theo bản chất bài (checklist vs code cần chạy), đối chiếu thủ công, kiểm tra nguồn và thêm ca đối chứng khi phát hiện lỗi thật.
2. **97** tuyên bố phiên bản: đánh giá theo ngữ cảnh lịch sử/hiện tại và chính xác phạm vi code nào chạy CPython 3.15.2; KHÔNG thay tự động câu `chưa kiểm định` bằng `PASS` nếu test chỉ chạy demo, không kiểm lời giải/khả năng thư viện.
3. 95 B có kiểm tra cấu trúc/syntax và hồi quy chạy toàn bộ, nhưng `exit 0` không chứng minh từng mã B bám đúng yêu cầu. Tiếp tục lấy mẫu theo lĩnh vực/hợp đồng và test âm tính nguồn-bound.
4. D06.03: hoàn thiện tương thích mypy/pyright khi phiên bản checker thật sự hỗ trợ, hoặc ghi rõ ngoại lệ được phê duyệt.
5. Kiểm định lại full-course/semantic/structural/native trên **commit chốt** trước khi xem xét đưa thay đổi vào nhánh của Draft PR #4. Bằng chứng GPU Kaggle thuộc SHA cũ; không tự chuyển sang SHA mới.
6. 441 phiếu reviewer độc lập/520 lượt thuộc Issue #7, GPU hardware attestation thuộc Issue #8 — vẫn **BLOCKED**.

**Quyết định:** Issue #9 giữ OPEN vì chưa kết thúc triage/nghiệm thu từng bài. Không merge vào `main`, không chuyển Draft PR #4 thành Ready, không tuyên bố giáo trình FULLY_CERTIFIED.

## Bổ sung M05.03 — bắt buộc đo query thật thay vì diễn giải (06/11/2026)

- **Xác minh lỗi phạm vi đáp án:** Bài B yêu cầu *test assert <=2 queries* khi tải orders cho 100 users. Lời giải trước đây chỉ có mô tả chiến lược, không có SQL ORM thực hoặc test tự chạy; demo Python map giả lập không cho phép đếm N+1. Mức phân loại: `CONFIRMED_UNIMPLEMENTED_TEST_CONTRACT`.
- **Sửa:** thêm `M05.03_bai_B_orm_query_budget.py` dùng SQLAlchemy/SQLite in-memory, 100 users/200 orders; `selectinload` <=2 SELECT, lazy 101 SELECT; counter tách setup/teardown; thêm `tests/test_issue9_m0503_query_budget.py` với 5 ca độc lập, invalid inputs và counter cleanup.
- **Đối chứng cục bộ:** 5/5 unittest PASS trên Python container (không phải CPython 3.15.2). Kết quả CPython 3.15.2 phải xem từ workflow Issue #9 đúng SHA.
- **Giới hạn:** counter này chỉ đo SELECT SQLAlchemy trong fixture; không tuyên bố mọi DB đều đạt 2 queries hay đã có review độc lập. Issue #9 còn OPEN.
