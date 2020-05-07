# tuple（元组）是一种不可变的、有序的列表
x = ('a','b','c')
print(x)
# 调用元素
print(x[1])
print(x[-1])
# 不可变的tuple意义：代码更加安全（尽可能的使用tuple代替list）
# 定义一个空的tuple
y = ()
print(y)
# 定义只有1个元素的tuple
y = (1,) # 如果不加‘,’则将被视为数学公式中的小括号
print(y[0])
# 可变的tuple,即tuple中包含list元素
z = ('a','b',['A','B'])
print(z[2][0])
print(z[2][1])
z[2].append('C')
print(z[2])
# tuple的不可变是指‘指向不变’

# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])