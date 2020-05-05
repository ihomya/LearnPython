#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在最新的Python 3版本中，字符串是以Unicode编码的

print('包含中文的str')
# 对于单个字符的编码，Python提供了
# # ord()函数获取字符的整数表示
print(ord('A'))
# # chr()函数把编码转换为对应的字符
print(chr(66))
# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')
# 由于Python的字符串类型是str，
# 内存中:以Unicode表示，一个字符对应若干个字节。
# 网络上传输/保存到磁盘上:就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = 'ABC' # str类型
y = b'ABC' # bytes类型
# 后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii')) # 纯英文的str可以用ASCII编码为bytes，
print('中文'.encode('utf-8')) # 内容是一样的，含有中文的str可以用UTF-8编码为bytes
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示
# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# # len()函数返回str包含字符个数
print(len('中文'))
# # 如果换成bytes，len()函数就计算字节数
print(len(b'ABC')) # 1个英文字符只占用1个字节
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8'))) # 1个中文字符经过UTF-8编码后通常会占用3个字节