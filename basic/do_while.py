# 计算 100 以内的 奇数
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习
L = ['Bart','Lisa','Adam']
i = 0
while i < len(L):
    print('Hello,%s!' % L[i])
    i = i + 1

# break
# 打印1-10
n = 1
while n <= 100:
    if n > 10:
        break # 提前跳出循环
    print(n)
    n = n + 1
print('End')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue # 跳过本轮循环
    print(n)
# 不滥用break和continue，容易造成代码执行逻辑分叉过多而出错