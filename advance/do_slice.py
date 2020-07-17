# 切片：取一个list或tuple片段
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 通常方法：
print([L[0],L[1],L[2]])
# 取n个
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 简化成切片：
print(L[0:3]) # 从索引0开始取，直到索引3为止，但不包括索引3
print(L[:3]) # 第一个索引是0，还可以省略
print(L[-2:]) # 同样也支持负数索引
print(L[-2:-1])

L = list(range(100)) # 0 - 99
print(L[:10]) # 0 - 9
print(L[-10:]) # 90 - 99
print(L[10:20]) # 10 - 19
print(L[:10:2]) # 0 - 9 每2个取1个
print(L[::5]) # 所有数，每 5 个取一个

T = (0,1,2,3,4,5)
print(T[:3]) # tuple同样也可以用切片操作，结果仍然是tuple

print('abcdefg'[:3]) # 字符串同样可以，结果仍然是str

# 练习：利用切片操作实现去除字符串首尾的空格
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')