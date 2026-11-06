"""Independent M05.03 SQLAlchemy 2.x SQL query-budget contracts."""
import runpy
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "03_HOC_PHAN/M/M05/MA_MAU/M05.03_bai_B_orm_query_budget.py"

class ORMQueryBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = runpy.run_path(str(SOURCE))

    def test_100_users_two_orders_eager_max_two_selects(self):
        engine = self.mod["seed_engine"](100)
        rows, queries = self.mod["load_users_orders"](engine, eager=True)
        self.assertEqual(len(rows), 100)
        self.assertTrue(all(len(orders)==2 for _,orders in rows))
        self.assertLessEqual(queries, 2)
        engine.dispose()

    def test_lazy_is_real_n_plus_one_not_in_memory_emulation(self):
        engine = self.mod["seed_engine"](100)
        eager, eq = self.mod["load_users_orders"](engine, eager=True)
        lazy, lq = self.mod["load_users_orders"](engine, eager=False)
        self.assertEqual(eager, lazy)
        self.assertEqual(lq, 101)
        self.assertLessEqual(eq, 2)
        engine.dispose()

    def test_small_edge_cases(self):
        for n in (1,2,10):
            with self.subTest(n=n):
                engine = self.mod["seed_engine"](n)
                eager,eq = self.mod["load_users_orders"](engine,eager=True)
                lazy,lq = self.mod["load_users_orders"](engine,eager=False)
                self.assertEqual(eager,lazy)
                self.assertLessEqual(eq,2)
                self.assertEqual(lq,n+1)
                engine.dispose()

    def test_invalid_user_count_rejected(self):
        for n in (0,201,-1,True,1.0,"100",None):
            with self.subTest(n=n),self.assertRaises(ValueError):
                self.mod["seed_engine"](n)

    def test_sql_count_hook_removed_after_read(self):
        engine=self.mod["seed_engine"](3)
        _,q1=self.mod["load_users_orders"](engine,eager=True)
        _,q2=self.mod["load_users_orders"](engine,eager=True)
        self.assertEqual(q1,2)
        self.assertEqual(q1,q2)
        engine.dispose()

if __name__ == "__main__":
    unittest.main()
