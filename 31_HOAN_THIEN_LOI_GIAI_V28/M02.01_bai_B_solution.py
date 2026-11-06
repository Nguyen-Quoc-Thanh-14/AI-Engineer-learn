from unittest.mock import Mock
# Dependency-injected transport; no real network connection.
def get_resource(client,url):
    result=client.get(url,timeout=2.0)
    if result.status_code!=200:raise RuntimeError('upstream unavailable')
    return result.json()
client=Mock();client.get.return_value.status_code=200
client.get.return_value.json.return_value={'value':12}
assert get_resource(client,'https://example.invalid/api')=={'value':12}
client.get.assert_called_once_with('https://example.invalid/api',timeout=2.0)
client.get.return_value.status_code=503
try:get_resource(client,'https://example.invalid/api')
except RuntimeError:pass
else:raise AssertionError('503 accepted')
