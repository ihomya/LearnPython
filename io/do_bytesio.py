#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

# 使用BytesIO操作二进制数据,BytesIO实现了在内存中读写bytes
# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())
