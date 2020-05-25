from collections import Iterable
from collections.abc import Iterator

# 迭代：循环遍历list或tuple，还可以用于其他可迭代对象上。
# 通过for...in完成
d = {'a':1,'b':2,'c':3}
# 字典的迭代：
# dict 的存储不是按照 list 的方式顺序排列，所以结果顺序很可能不一样
for key in d:
    print(key)
# 对字典的值进行迭代
for value in d.values():
    print(value)
# 同时迭代字典的键值
for key,value in d.items():
    print(key,'->',value)

# 字符串也是可迭代对象
for char in 'ABCD':
    print(char)

# 判断对象是否为可迭代对象
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

# list的下标循环
# enumerate函数可以把一个 list 变成索引 - 元素对
for i,value in enumerate(['A','B','C']):
    print(i,value)

# 引入两个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

# 练习：使用迭代查找list中最小值与最大值，并返回tuple
def findMinAndMax(L):
    if L == []:
        return (None,None)
    min,max = L[0],L[0]
    for value in L:
        if value < min:
            min = value
        elif value > max:
            max = value
    return min,max
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 判断是否为可迭代对象：Iterable（list、tuple、dict、set、str、generator）
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterato
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    pass
#实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break