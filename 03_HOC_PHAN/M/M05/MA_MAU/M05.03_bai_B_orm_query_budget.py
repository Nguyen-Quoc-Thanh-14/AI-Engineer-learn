"""M05.03 ORM N+1 reproducible query budget, SQLite and SQLAlchemy 2.x."""
from contextlib import contextmanager
from sqlalchemy import ForeignKey, create_engine, event, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "m0503_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user", lazy="select")

class Order(Base):
    __tablename__ = "m0503_orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("m0503_users.id"), nullable=False)
    user: Mapped[User] = relationship(back_populates="orders")

def seed_engine(user_count: int = 100):
    if type(user_count) is not int or not 1 <= user_count <= 200:
        raise ValueError("user_count must be an integer from 1 to 200")
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all([User(id=i, orders=[Order(), Order()]) for i in range(1, user_count + 1)])
        session.commit()
    return engine

@contextmanager
def select_counter(engine):
    observed = []
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        if statement.lstrip().upper().startswith("SELECT"):
            observed.append(statement)
    event.listen(engine, "before_cursor_execute", before_cursor_execute)
    try:
        yield observed
    finally:
        event.remove(engine, "before_cursor_execute", before_cursor_execute)

def load_users_orders(engine, *, eager: bool):
    with select_counter(engine) as statements, Session(engine) as session:
        stmt = select(User).order_by(User.id)
        if eager:
            stmt = stmt.options(selectinload(User.orders))
        users = session.scalars(stmt).all()
        result = [(u.id, tuple(sorted(o.id for o in u.orders))) for u in users]
    return result, len(statements)

def verify():
    engine = seed_engine(100)
    eager_result, eager_queries = load_users_orders(engine, eager=True)
    lazy_result, lazy_queries = load_users_orders(engine, eager=False)
    assert len(eager_result) == 100
    assert all(len(orders) == 2 for _, orders in eager_result)
    assert eager_result == lazy_result
    assert eager_queries <= 2, eager_queries
    assert lazy_queries == 101, lazy_queries
    engine.dispose()
    return {"users": 100, "orders": 200,
            "eager_selects": eager_queries, "lazy_selects": lazy_queries}

if __name__ == "__main__":
    print("M05_03_ORM_QUERY_BUDGET_PASS", verify())
