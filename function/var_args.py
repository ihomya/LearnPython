# 位置参数
def power(x): # x属于位置参数
    return x*x # 返回x的平方
print(power(5))

# 计算任意n次方(n > 0)
def power1(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(2,10))

# 默认参数
#  需注意：
# 1.必选参数在前，默认参数在后 
# 2.如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power2(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(5))
# 使用默认参数的最大好处在于能降低调用函数的难度
# 比如，用户注册函数
def reg(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
reg('A','M')
# 也可以不按顺序提供部分默认参数
reg('B','F',city='Tainjin')

# 易错点
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象

# 修改后（None为不变对象）
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象

# 可变参数：传入参数个数可变
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc([1,2,3]))
print(calc((1,3,5,7)))
# 简化后
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变
print(calc(1,2,3))
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
print(calc())
# 如果已经有一个list或者tuple
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# 这种写法是可行的，但是太繁琐
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))