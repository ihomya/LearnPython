import math

# def语句定义函数
def my_abs(x):
    # 用内置函数isinstance()实现数据类型检查
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-100))
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return

# 空函数
def nop():
    pass
# 实际上pass可以用来作为占位符
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 已知当前坐标获取新坐标
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny 

x,y = move(100,100,60,math.pi/6)
print(x,y)
r = x,y
print(r) # 返回一个tuple,语法上tuple是可以省略括号的

# 练习
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('参数错误')
    if not isinstance(b,(int,float)):
        raise TypeError('参数错误')
    if not isinstance(c,(int,float)):
        raise TypeError('参数错误')
    delta = b**2 - 4*a*c
    if delta < 0:
        return '无解'
    elif delta == 0:
        return x == -b/2*a
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/ a*2
        x2 = (-b - math.sqrt(b**2 + 4*a*c))/ a*2
        return x1,x2


a = int(input('输入a'))
b = int(input('输入b'))
c = int(input('输入c'))
print(quadratic(a,b,c))