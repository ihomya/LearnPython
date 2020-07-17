# list是一种有序的集合，可以随时增删改查其中的元素
l = ['A', 'B', 'C']
print(l)
print('列表:l 包含'+str(len(l))+'个元素')
print('分别为'+l[0]+','+l[1]+','+l[2])
# 当索引越界时，Python会报一个IndexError错误
print(l[-1]) # 输出最后一个元素
print(l[-2]) # 输出倒数第二个元素，以此类推，可以获取倒数第3个、倒数第4个

l.append('D') # 使用 append()方法向列表中追加元素到末尾
print(l)
l.insert(1 ,"a") # 使用insert()方法向索引号为1的位置插入元素‘a’
print(l)
l.pop() # 使用pop()方法删除列表末尾的元素
l.pop(1) # 如果带有参数则将删除指定位置的元素
print(l)
l[0] = 'a' # 重新赋值将替换原有值
print(l) 
l[0] = 'A'
print(l)

# list中的数据类型也可以不同
i = ['A',1,True]
# 也可以包含另一个list
s = ['A',2,i]
print(len(s)) # 其中列表i也是一个元素
print(s[2][2]) # 列表s也可视为（php中的）二维数组

x = []
print(len(x)) # 一个空的list的长度为0