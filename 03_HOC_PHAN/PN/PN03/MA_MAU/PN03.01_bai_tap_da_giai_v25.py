"""PN03.01 corrected: 30 factual QA records with explicit reference and evidence labels.
Demonstrates a deliberately narrow textual-grounding baseline, NOT semantic entailment.
"""
FACTS = [
 ("Hồ sơ An","mã truy cập","TOKEN-ALPHA"),
 ("Hồ sơ Bình","mã chuyến","TRAIN-024"),
 ("Hồ sơ Cúc","số trang","PAGE-126"),
 ("Hồ sơ Dũng","mã cây","TREE-005"),
 ("Hồ sơ Em","mã nhóm","GROUP-009"),
 ("Hồ sơ Giang","mã bài","LESSON-302"),
 ("Hồ sơ Hạnh","mã ghế","SEAT-A12"),
 ("Hồ sơ Ích","mã áo","SHIRT-X4"),
 ("Hồ sơ Khải","mã kho","STORE-037"),
 ("Hồ sơ Lan","mã phòng","ROOM-308"),
 ("Hồ sơ Minh","mã đợt","BATCH-090"),
 ("Hồ sơ Nga","mã sự kiện","EVENT-072"),
 ("Hồ sơ Oanh","mã đơn","ORDER-063"),
 ("Hồ sơ Phúc","mã toa","CAR-081"),
 ("Hồ sơ Quỳnh","mã hộp","BOX-014"),
]

def build_evaluation_set():
    rows=[]
    for i,(subject,field,value) in enumerate(FACTS,1):
        evidence=f"{subject} có {field} = {value}."
        rows.append({"id":f"QA-{i:02d}-G",
                     "question":f"{subject} có {field} gì?",
                     "evidence":evidence,"reference_answer":value,
                     "candidate_answer":value,"expected":"grounded"})
        rows.append({"id":f"QA-{i:02d}-U",
                     "question":f"{subject} có mật khẩu đăng nhập gì?",
                     "evidence":evidence,
                     "reference_answer":"Không có dữ liệu trong nguồn",
                     "candidate_answer":f"password-{i:02d}",
                     "expected":"unsupported"})
    return rows

def classify_text_support(evidence: str, answer: str) -> str:
    if not isinstance(evidence,str) or not isinstance(answer,str) or not answer:
        raise ValueError("nonempty string evidence and answer required")
    return "grounded" if answer.casefold() in evidence.casefold() else "unsupported"

def check():
    rows=build_evaluation_set()
    assert len(rows)==30 and len(set(r["id"] for r in rows))==30
    assert sum(r["expected"]=="grounded" for r in rows)==15
    assert sum(r["expected"]=="unsupported" for r in rows)==15
    assert all(classify_text_support(r["evidence"],r["candidate_answer"])==r["expected"] for r in rows)
    assert all(r["reference_answer"] for r in rows)
    try:classify_text_support("context","")
    except ValueError:pass
    else:raise AssertionError("empty answer")
if __name__=="__main__":
    check()
    print("PASS PN03.01 30 QA with grounded/unsupported references")
