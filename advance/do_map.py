# map()函数接收2个参数：1.函数 2.Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x*x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 练习
def normalize(name):
    return str.capitalize(name)


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
