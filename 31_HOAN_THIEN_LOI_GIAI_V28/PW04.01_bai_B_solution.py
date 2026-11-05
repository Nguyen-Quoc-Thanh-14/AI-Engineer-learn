from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.testclient import TestClient
state={'opened':0,'closed':0}
@asynccontextmanager
async def lifespan(app):
    state['opened']+=1
    try:yield
    finally:state['closed']+=1
app=FastAPI(lifespan=lifespan)
@app.get('/')
def home():return {'ok':True}
with TestClient(app) as client:
    assert client.get('/').status_code==200
    assert state=={'opened':1,'closed':0}
assert state=={'opened':1,'closed':1}
