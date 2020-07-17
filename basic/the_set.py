# set也是一组key的集合，但不存储value，并且key不能重复
s = set([1,2,3]) # 创建set需要提供一个list作为输入集合
print('一个set：',s)
# 传入的参数是list，而显示的{1，2，3}则只能表示set内部有 1，2，3这三个元素
# 而且显示的顺序也不表示set是有序的
s1 = set([1,1,2,2,2,3,3,3])
print('自动过滤重复元素',s1)

s.add(4) # 添加元素
s.add(3) # 可重复添加，但无效果
print(s)

s.remove(4) # 删除元素
print(s)
s1.remove(3)
print(s1)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2) # 交集
print(s1 | s2) # 并集

# 可变对象：list
# 不可变对象：str
a = 'abc'
print(a.replace('a','A')) # 对 不可变对象 进行操作,但对对象本身无影响
print(a)
# 通常说的对象a的内容是‘abc’,其实是指它指向对象的内容是‘abc’,而 a 本身是个变量
b = a.replace('a','A')  # 变量b的str对象指向的是'对象a'的replace返回的str对象
print(b) # 打印‘Abc’

# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的

# 拓展
x = set((1,2,3))
print(x)
# y = set((1,[2,3]))
# print(y) 报错：list非Hash算法
for i in x:
    print(i)