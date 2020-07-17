# sorted()排序函数,用sorted()排序的关键在于实现一个映射函数
a = sorted([36, 5, -12, 9, -21])
print(a)
# 还可接收一个key函数来实现自定义排序
b = sorted([36, 5, -12, 9, -21], key=abs)  # 以绝对值大小排序
print(b)
# keys排序结果 => [5, 9,  12,  21, 36]
#                 |  |    |    |   |
# 最终结果     => [5, 9, -12, -21, 36]
c = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(c)
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
# 忽略大小写
d = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(d)
# 进行反向排序
e = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(e)
# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
