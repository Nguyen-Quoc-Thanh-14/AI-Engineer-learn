# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from collections import Counter
train=[0,1,0,0,1]
test=[0,1,0]
majority=Counter(train).most_common(1)[0][0]
preds=[majority]*len(test)
accuracy=sum(a==b for a,b in zip(preds,test))/len(test)
assert accuracy==2/3
print('baseline accuracy:',round(accuracy,3))
