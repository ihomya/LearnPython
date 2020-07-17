import os
# 列表生成式
# 通常使用循环获取列表
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

# 通过列表生成式
a = [x*x for x in range(1,11)]
print(a)
# 还可加if判断
b = [x*x for x in range(1,11) if x % 2 == 0]
print(b)
# 双层循环
c = [m+n for m in 'ABC' for n in 'XYZ'] # 三层和三层以上的循环就很少用到了
print(c)

# 列出当前目录下所有文件及目录名
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# 使用两个变量
d = {'X':'A','Y':'B','Z':'C'}
print([k + '=' + v for k,v in d.items()])

# 将list中字符串变成小写
L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

# if ... else的用法
print([x for x in range(1, 11) if x % 2 == 0]) # if是过滤条件
# 不可直接在后面加else语句，但if写在for前则需要使用else
print([x if x % 2 == 0 else -x for x in range(1, 11)])

# 练习：将L中的字符串改为小写
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

