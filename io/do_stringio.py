#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
f = StringIO()  # StringIO顾名思义就是在内存中读写str
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())  # getvalue()方法用于获得写入后的str

# read from StringIO:
# 初始化
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
