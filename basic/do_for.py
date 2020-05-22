names = ['Michael','Bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print(list(range(5))) # range()函数生成一个整数序列，list()函数则将其转换为list
# 计算0-100的和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 练习
L = ['Bart','Lisa','Adam']
for i in L:
    print('Hello,%s!' % i)