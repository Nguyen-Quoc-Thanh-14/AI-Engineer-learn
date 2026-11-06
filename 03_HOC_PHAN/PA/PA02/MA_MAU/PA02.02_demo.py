# coding: utf-8
# Bài PA02.02 — Tài liệu có thể thực thi độc lập
from html.parser import HTMLParser
class Tags(HTMLParser):
    def __init__(self):super().__init__();self.tags=[]
    def handle_starttag(self,tag,attrs):self.tags.append(tag)
p=Tags();p.feed('<div><p>A</p></div>')
assert p.tags==['div','p']
