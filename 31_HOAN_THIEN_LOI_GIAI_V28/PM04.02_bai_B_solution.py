from hashlib import sha256
import platform,json
import importlib.metadata as metadata
sample=b'feature,label\n1,0\n2,1\n'
manifest={'data_sha256':sha256(sample).hexdigest(),'python':platform.python_version(),
          'numpy':metadata.version('numpy'),'sklearn':metadata.version('scikit-learn'),'seed':42}
assert len(manifest['data_sha256'])==64 and manifest['seed']==42
print(json.dumps(manifest,sort_keys=True))
