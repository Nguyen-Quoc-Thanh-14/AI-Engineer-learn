"""Independent ORM/FK/migration behavioral oracles for M05.01 and PW02.01."""
import runpy
import unittest
from pathlib import Path
from sqlalchemy import inspect, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

ROOT=Path(__file__).resolve().parents[1]

class OrmAndMigrationContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m05=runpy.run_path(str(ROOT/"31_HOAN_THIEN_LOI_GIAI_V28/M05.01_bai_B_solution.py"))
        cls.pw=runpy.run_path(str(ROOT/"31_HOAN_THIEN_LOI_GIAI_V28/PW02.01_bai_B_solution.py"))

    def test_m05_executes_actual_orm_models(self):
        m=self.m05
        self.assertEqual(m["User"].__tablename__,"users")
        self.assertEqual(m["Order"].__tablename__,"orders")
        self.assertTrue(hasattr(m["User"],"__mapper__"))
        self.assertTrue(hasattr(m["Order"],"__mapper__"))
        self.assertEqual(m["run_demo"](),{"users":1,"orders":1,"duplicate_email_rejected":True})

    def test_m05_unique_is_database_not_only_python_check(self):
        m=self.m05
        eng=m["make_engine"]()
        m["Base"].metadata.create_all(eng)
        constraints=inspect(eng).get_unique_constraints("users")
        self.assertTrue(any("email" in constraint["column_names"] for constraint in constraints))

    def test_m05_foreign_key_declared(self):
        m=self.m05
        eng=m["make_engine"]()
        m["Base"].metadata.create_all(eng)
        fks=inspect(eng).get_foreign_keys("orders")
        self.assertTrue(any(f["referred_table"]=="users" for f in fks))

    def test_pw02_real_schema_migration_v1_to_v2(self):
        p=self.pw
        engine=p["make_engine"]()
        p["create_v1"](engine)
        with engine.connect() as conn:
            self.assertEqual(conn.exec_driver_sql("SELECT version FROM schema_version").scalar_one(),1)
            self.assertEqual(conn.exec_driver_sql("PRAGMA foreign_key_list(orders)").all(),[])
        p["migrate_v1_to_v2"](engine)
        with engine.connect() as conn:
            self.assertEqual(conn.exec_driver_sql("SELECT version FROM schema_version").scalar_one(),2)
            self.assertEqual(len(conn.exec_driver_sql("PRAGMA foreign_key_list(orders)").all()),1)
            self.assertEqual(conn.exec_driver_sql("SELECT user_id FROM orders WHERE id=10").scalar_one(),1)

    def test_pw02_orphan_is_rejected_after_migration(self):
        p=self.pw
        engine=p["make_engine"]()
        p["create_v1"](engine)
        p["migrate_v1_to_v2"](engine)
        with Session(engine) as session:
            session.add(p["Order"](id=11,user_id=999))
            with self.assertRaises(IntegrityError):
                session.commit()
            session.rollback()

    def test_pw02_second_migration_fails_closed(self):
        p=self.pw
        engine=p["make_engine"]()
        p["create_v1"](engine)
        p["migrate_v1_to_v2"](engine)
        with self.assertRaises(ValueError):
            p["migrate_v1_to_v2"](engine)

    def test_pw02_demo_result(self):
        p=self.pw
        self.assertEqual(p["run_demo"](),{
            "schema_version":2,"old_order_preserved":True,
            "foreign_key_rejected":True})

if __name__=="__main__":
    unittest.main()
