"""PW02.01 B: SQLAlchemy ORM models plus SQLite v1->v2 FK migration.

This is a transactional teaching example. Real deployments require Alembic
migration scripts, backups, data validation, rollback/lock planning, and reviews.
"""
from __future__ import annotations
from sqlalchemy import ForeignKey, String, create_engine, event, select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String(254),nullable=False,unique=True)
    orders:Mapped[list["Order"]]=relationship(back_populates="user")

class Order(Base):
    __tablename__="orders"
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    user:Mapped[User]=relationship(back_populates="orders")

def make_engine():
    engine=create_engine("sqlite+pysqlite:///:memory:")
    @event.listens_for(engine,"connect")
    def enable_foreign_keys(dbapi_conn, _):
        dbapi_conn.execute("PRAGMA foreign_keys=ON")
    return engine

def create_v1(engine):
    with engine.begin() as conn:
        conn.exec_driver_sql("CREATE TABLE schema_version(version INTEGER NOT NULL)")
        conn.exec_driver_sql("INSERT INTO schema_version VALUES (1)")
        conn.exec_driver_sql("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)")
        # Legacy schema has no foreign key.
        conn.exec_driver_sql("CREATE TABLE orders(id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL)")
        conn.exec_driver_sql("INSERT INTO users VALUES (1,'sample@example.invalid')")
        conn.exec_driver_sql("INSERT INTO orders VALUES (10,1)")

def migrate_v1_to_v2(engine):
    with engine.begin() as conn:
        current=conn.exec_driver_sql("SELECT version FROM schema_version").scalar_one()
        if current!=1:raise ValueError("Expected schema version 1")
        # SQLite cannot simply ADD CONSTRAINT to an existing table.
        # Rebuild table and preserve the original rows in the transaction.
        conn.exec_driver_sql(
            "CREATE TABLE orders_new("
            "id INTEGER PRIMARY KEY, "
            "user_id INTEGER NOT NULL REFERENCES users(id))"
        )
        conn.exec_driver_sql("INSERT INTO orders_new SELECT id,user_id FROM orders")
        conn.exec_driver_sql("DROP TABLE orders")
        conn.exec_driver_sql("ALTER TABLE orders_new RENAME TO orders")
        conn.exec_driver_sql("UPDATE schema_version SET version=2")

def run_demo():
    engine=make_engine()
    create_v1(engine)
    migrate_v1_to_v2(engine)
    with engine.connect() as conn:
        version=conn.exec_driver_sql("SELECT version FROM schema_version").scalar_one()
        foreign_keys=conn.exec_driver_sql("PRAGMA foreign_key_list(orders)").all()
        assert version==2 and len(foreign_keys)==1
        assert foreign_keys[0][2]=="users"
    with Session(engine) as session:
        old_row=session.scalars(select(Order).where(Order.id==10)).one()
        assert old_row.user_id==1
        session.add(Order(id=11,user_id=999))
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            foreign_key_rejected=True
        else:
            foreign_key_rejected=False
    assert foreign_key_rejected, "Migration failed to enforce FK"
    return {"schema_version":version,"old_order_preserved":True,
            "foreign_key_rejected":foreign_key_rejected}

if __name__=="__main__":
    print("PW02.01_MIGRATION_FK_PASS",run_demo())
