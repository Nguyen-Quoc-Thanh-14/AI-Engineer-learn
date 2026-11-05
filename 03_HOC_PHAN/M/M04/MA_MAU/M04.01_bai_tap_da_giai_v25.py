"""M04.01 corrected: SQL placeholder query product NAME by integer ID."""
import sqlite3

def create_products_db():
    conn=sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    conn.executemany("INSERT INTO products(id,name) VALUES (?,?)",
                     [(1,"Pen"),(2,"Paper"),(3,"Coffee")])
    conn.commit()
    return conn

def product_name(conn:sqlite3.Connection, product_id:int)->str|None:
    if type(product_id) is not int:
        raise TypeError("product_id must be int, not str or bool")
    row=conn.execute("SELECT name FROM products WHERE id = ?",(product_id,)).fetchone()
    return row[0] if row else None

def check():
    with create_products_db() as db:
        assert product_name(db,1)=="Pen"
        assert product_name(db,3)=="Coffee"
        assert product_name(db,999) is None
        for bad in ("1 OR 1=1",True,"1; DROP TABLE products"):
            try:product_name(db,bad)
            except TypeError:pass
            else:raise AssertionError("unsafe ID accepted")
        assert db.execute("SELECT COUNT(*) FROM products").fetchone()[0]==3
if __name__=="__main__":
    check()
    print("PASS M04.01 SQL parameter binding")
