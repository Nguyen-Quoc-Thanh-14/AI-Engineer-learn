# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def normalize_order(order):
    qty = order['qty'];price=order['price']
    if any(isinstance(v,bool) or not isinstance(v,int) or v<0 for v in (qty,price)):
        raise ValueError('dữ liệu không hợp lệ')
    return qty,price
def subtotal(qty,price): return qty*price
def format_receipt(order):
    qty,price=normalize_order(order)
    return f'Tổng: {subtotal(qty,price)}'
assert format_receipt({'qty':2,'price':50})=='Tổng: 100'
assert subtotal(0,100)==0
try: format_receipt({'qty':-1,'price':5})
except ValueError: pass
else: raise AssertionError
print('PASS E06.04')
