# reduce的用法：是将一个函数作用于一个序列[x1,x2,x3,...]上，
# 其函数必须接收2个参数，reduce把结果继续和序列的下一个元素做累积计算
# 效果如：reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))  # 返回1+3+5+7+9


def fn(x, y):
    return x*10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))  # 返回13579

# str转换为int的函数


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))  # 返回13579


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 整理成一个str2int的函数
def str2int(s):
    def fn(x, y):
        return x*10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('13579'))


# 用lambda函数进一步简化成
def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 练习
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)


# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习
def str2float(s):
    def char2num(s):
        return DIGITS[s]

    def fn(x, y):
        return x*10 + y

    i = str.split(s, '.')
    c = len(i[1])  # 小数点后位数
    s = str.replace(s, '.', '')  # 去除小数点
    return reduce(fn, map(char2num, s)) / (10 ** c)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
