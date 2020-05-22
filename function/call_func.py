# 函数abs：求绝对值，只有一个参数
print(abs(-20)) # 调用函数abs
print(abs(12.34))
# abs(1,2) 报错：TypeError: abs() takes exactly one argument (2 given)
# abs('a') 报错：TypeError: bad operand type for abs(): 'str'

# 函数max：可以接收任意多个参数，并返回最大值
print(max(1,2,3,5))
print(max(1,10,-10))

# 数据类型转换
print(int('1234'))
print(int(3.14))
print(float('3.14'))
print(str(1.23))
print(bool(1))
print(bool(0))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数

# 函数hex：把一个整数转换成十六进制表示的字符串
# 练习
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))