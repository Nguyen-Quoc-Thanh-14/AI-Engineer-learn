from http import HTTPStatus
# Simplified HTTP semantics example, not a production web server.
resources={'42':{'title':'hello'}}
def handle(method,path,body=None,authenticated=True):
    if not authenticated:return HTTPStatus.UNAUTHORIZED,None
    if method=='GET':
        if path not in resources:return HTTPStatus.NOT_FOUND,None
        return HTTPStatus.OK,resources[path]
    if method=='POST':
        if not isinstance(body,dict) or not body.get('title'):return HTTPStatus.BAD_REQUEST,None
        return HTTPStatus.CREATED,body
    if method=='PUT':
        if path not in resources:return HTTPStatus.NOT_FOUND,None
        if not isinstance(body,dict):return HTTPStatus.BAD_REQUEST,None
        resources[path]=body;return HTTPStatus.OK,body
    return HTTPStatus.METHOD_NOT_ALLOWED,None
assert handle('GET','42')[0]==200
assert handle('GET','missing')[0]==404
assert handle('POST','',{})[0]==400
assert handle('GET','42',authenticated=False)[0]==401
assert handle('PUT','42',{'title':'updated'})[0]==200
