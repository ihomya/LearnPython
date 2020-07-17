# filter()用于过滤序列
# 接收2个参数：函数与序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 返回的是一个Iterator，也就是一个惰性序列
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回lis

# 保留序列中的奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 7, 8, 9])))


# 去除序列中的空字符串
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 求质数
# 生成器：从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 质数生成器
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
# primes()是无限序列，需要设置退出循环条件
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 练习：筛选回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(0, 1000))))
