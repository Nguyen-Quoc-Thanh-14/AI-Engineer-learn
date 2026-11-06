"""M05.01 B: real SQLAlchemy ORM User/Order plus DB-enforced unique constraint."""
from __future__ import annotations
from sqlalchemy import ForeignKey, String, create_engine, event, inspect, select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String(254),unique=True,nullable=False)
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

def run_demo():
    engine=make_engine()
    Base.metadata.create_all(engine)  # Lab only: NOT a production migration.
    constraints=inspect(engine).get_unique_constraints("users")
    assert any("email" in c["column_names"] for c in constraints)
    with Session(engine) as session:
        user=User(email="demo@example.invalid")
        session.add(user)
        session.flush()
        session.add(Order(user=user))
        session.commit()
    with Session(engine) as session:
        session.add(User(email="demo@example.invalid"))
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            duplicate_blocked=True
        else:
            duplicate_blocked=False
    assert duplicate_blocked, "DB accepted duplicate email"
    with Session(engine) as session:
        user_count=session.scalar(select(func.count()).select_from(User))
        order_count=session.scalar(select(func.count()).select_from(Order))
        assert session.scalar(select(Order.user_id))==1
    assert user_count==1 and order_count==1
    return {"users":user_count,"orders":order_count,
            "duplicate_email_rejected":duplicate_blocked}

if __name__=="__main__":
    print("M05.01_ORM_UNIQUE_PASS",run_demo())
