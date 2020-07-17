# 字典：使用键-值（key-value）存储，具有极快的查找速度(其他语言中也称之为map)
d = {'Michael': 95,'Bob': 75,'Tracy': 85}
print('Michael的成绩：',d['Michael'])

d['Jack'] = 67 # 通过赋值方式添加键值对或修改值
print('Jack的成绩：',d['Jack'])

# 判断key是否存在
print('Tim' in d) # 返回False
print(d.get('Tim')) # 返回 None

print(d.get('Tim',-1)) # 通过第二个参数指定值（不会添加到字典中）
print(d)

# 删除字典中键值对
d.pop('Jack')
print(d)

# 要牢记的第一条就是dict的key必须是不可变对象

# 拓展
y = {(1,2,3),4}
print(y)
# z = {(1,[2,3]),4}
# print(z) 报错：list非Hash算法

for i in d:
    print('{}的成绩：{}'.format(i,d[i]))