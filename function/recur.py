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
# # 利用递归函数移动汉诺塔:
### 从 A 借助 B 移动到 C 的方法
### n表示3个柱子A、B、C中第1个柱子A的盘子数量
def move(n,a,b,c):
    if n == 1:
        print(a,' --> ',c)
    else:
        move(n-1, a, c, b)  #例如三块，就先把上面两块借助中间的c移到b

        move(1,a,b,c)    #然后最下面的那个最大的那块，就可以移动到c终点

        move(n-1,b,a,c)    #最后再把剩下的那两块借助a移动到c终点搭好

move(3,'a','b','c')