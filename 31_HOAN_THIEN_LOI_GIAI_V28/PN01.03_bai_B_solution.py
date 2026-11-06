from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs=['python unit testing', 'computer vision image classification', 'python pandas data cleaning']
queries=['unit test in python', 'image recognition', 'pandas dataframe cleaning']
expected=[0,1,2]
vec=TfidfVectorizer().fit(docs)
scores=cosine_similarity(vec.transform(queries),vec.transform(docs))
pred=scores.argmax(axis=1).tolist()
assert pred==expected, (pred,expected)
# Expand to 10 annotated queries and record accuracy@k before claiming system quality.
