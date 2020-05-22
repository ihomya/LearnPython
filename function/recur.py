# 递归函数
# fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1) # 引入了乘法表达式
print(fact(5))
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出

# 针对尾递归优化的语言可以通过尾递归防止栈溢出。
# 尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product) # 调用本身

print(fact(5))
# Python 标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题

# 练习
def move(n,a,b,c):
    if n == 1:
        return a+' --> '+c
    else:
        return move(2**n - 1,a,b,c)

print(move(3,'a','b','c'))