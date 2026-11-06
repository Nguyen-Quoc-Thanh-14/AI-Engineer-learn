import csv,json,io

def convert(csv_text):
    rows=[]
    for row in csv.DictReader(io.StringIO(csv_text)):
        try:q=int(row['qty'])
        except (ValueError,KeyError,TypeError):raise ValueError('qty must be integer')
        if q<0:raise ValueError('qty negative')
        rows.append({'name':row['name'],'qty':q})
    return json.dumps(rows,ensure_ascii=False)
assert json.loads(convert('name,qty\nCà phê,2\n'))==[{'name':'Cà phê','qty':2}]
for text in ('name,qty\nA,-1\n','name,qty\nA,xx\n'):
    try: convert(text)
    except ValueError:pass
    else:raise AssertionError('bad quantity accepted')
