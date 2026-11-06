from fastapi import FastAPI,HTTPException
from fastapi.testclient import TestClient
app=FastAPI()
@app.get('/public')
def public():return {'ok':True}
@app.get('/private/{id}')
def private(id:int,role:str='guest'):
    if role=='guest':raise HTTPException(401)
    if id!=1:raise HTTPException(403)
    return {'id':id}
client=TestClient(app)
assert client.get('/public').status_code==200
assert client.get('/private/1').status_code==401
assert client.get('/private/2?role=reader').status_code==403
assert client.get('/private/notint?role=reader').status_code==422
# Synthetic auth role query parameter is ONLY for test illustration; not production auth.
