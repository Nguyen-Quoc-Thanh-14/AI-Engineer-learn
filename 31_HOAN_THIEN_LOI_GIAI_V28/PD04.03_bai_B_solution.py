import csv,io,statistics

def report(csv_data):
    rows=list(csv.DictReader(io.StringIO(csv_data)))
    values=[float(r['value']) for r in rows]
    if not values:raise ValueError('no values')
    return f'# Report\n\nRows: {len(rows)}\nMean: {statistics.mean(values):.2f}\n'
assert report('value\n1\n2\n3\n')=='# Report\n\nRows: 3\nMean: 2.00\n'
