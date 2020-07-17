# 偏函数：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
# int()函数可以把字符串转换为整数，当仅传入字符串时，
# int()函数默认按十进制转换：
i = int('12345')
print(i)
i = int('12345', base=8)
print(i)
i = int('12345', 16)
print(i)


# 假设要转换大量的二进制字符串，
# 可以定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x, base)


# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int, base=2)

# 创建偏函数时，
# 实际上可以接收函数对象、*args和**kw这3个参数，

# 当传入int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，
# 也就是：
i = int2('10010')
print(i)
# 相当于：
kw = {'base': 2}
i2 = int('10010', **kw)
print(i2)

# 当传入：
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边
# 也就是：
m = max2(5, 6, 7)
print(m)
# 相当于：
args = (10, 5, 6, 7)
m2 = max(*args)
print(m2)

# test
min2 = functools.partial(min, 0)
print(min2(1, 2, 3, 4))
