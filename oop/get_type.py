# 使用type()函数判断对象类型
import types
i = type(123)
print(i)
s = type('str')
print(s)
n = type(None)
print(n)
f = type(abs)  # 指向函数
print(f)


class a(object):
    pass


c = type(a)  # 指向类
print(c)  # <class '__main__.Animal'>

print(type(type))  # 返回对应的Class类型

# 比较类型是否相同
print(i == int)
print(i == s)


# 判断对象是否为函数，需import types
def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
