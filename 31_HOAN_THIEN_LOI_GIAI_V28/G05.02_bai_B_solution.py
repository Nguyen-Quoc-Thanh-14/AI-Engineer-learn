import unicodedata
flag='🇻🇳'
assert len(flag)==2 # two regional-indicator Unicode code points; one visual flag grapheme
precomposed='café'; decomposed='cafe\u0301'
assert precomposed!=decomposed
assert unicodedata.normalize('NFC',precomposed)==unicodedata.normalize('NFC',decomposed)
# Python str and len() do not automatically segment grapheme clusters.
