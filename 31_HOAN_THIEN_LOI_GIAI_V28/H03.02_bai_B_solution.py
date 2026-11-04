from dataclasses import dataclass
import sqlite3
@dataclass
class Item: name: str
class FakeRepo:
    def __init__(self): self.data=[]
    def add(self,x): self.data.append(x)
    def all(self): return self.data[:]
class SQLiteRepo:
    def __init__(self,db): self.db=db;db.execute('CREATE TABLE item(name TEXT NOT NULL)')
    def add(self,x): self.db.execute('INSERT INTO item VALUES (?)',(x.name,))
    def all(self): return [Item(x[0]) for x in self.db.execute('SELECT name FROM item')]
for repo in (FakeRepo(),SQLiteRepo(sqlite3.connect(':memory:'))):
    repo.add(Item('coffee'));assert repo.all()==[Item('coffee')]
