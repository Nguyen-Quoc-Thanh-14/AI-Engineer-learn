# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import socket
if hasattr(socket,'socketpair'):
    a,b=socket.socketpair()
    with a,b:
        a.sendall(b'abc')
        assert b.recv(3)==b'abc'
print('socket lab ok')
