"""N01.02 safety-of-instruction regression, not expert security review."""
from pathlib import Path
import re
import sqlite3
import unittest

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "03_HOC_PHAN/N/N01/BAI_HOC/N01.02.md"

class N0102SafetyLanguage(unittest.TestCase):
    def test_attack_names_are_not_recommended_as_methods(self):
        text=LESSON.read_text(encoding="utf8")
        self.assertIn("là các kiểu tấn công hoặc rủi ro",text)
        self.assertNotIn("nêu một trường hợp nên và không nên áp dụng",text)
        self.assertNotIn("**Injection, path traversal và command execution** mang lại lợi ích",text)
        for term in ("SQL injection","Path traversal","Command injection","parameter binding","trust boundary"):
            self.assertIn(term,text)
    def test_sql_parameter_example_still_has_valid_semantics(self):
        with sqlite3.connect(":memory:") as conn:
            conn.execute("CREATE TABLE products (code TEXT PRIMARY KEY)")
            conn.execute("INSERT INTO products(code) VALUES (?)",("ABC-12345",))
            valid=conn.execute("SELECT code FROM products WHERE code = ?",("ABC-12345",)).fetchone()
            untrusted="ABC-12345' OR '1'='1"
            injected=conn.execute("SELECT code FROM products WHERE code = ?",(untrusted,)).fetchone()
            self.assertEqual(valid,("ABC-12345",))
            self.assertIsNone(injected)
    def test_security_lessons_avoid_attack_as_benefit_template(self):
        for lesson in ROOT.glob("03_HOC_PHAN/N/**/BAI_HOC/*.md"):
            text=lesson.read_text(encoding="utf8")
            self.assertNotRegex(text,r"(?is)(?:injection|path traversal|command execution).{0,90}mang lại lợi ích lớn hơn độ phức tạp",lesson.name)

if __name__=="__main__":
    unittest.main()
