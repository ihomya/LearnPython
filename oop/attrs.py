# 使用dir()获得一个对象的所有属性和方法,返回一个包含字符串的list
print(dir('abc'))

print(len('ABC'))
# len()函数内部自动去调用该对象的__len__()方法
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100


d = MyDog()
print(len(d))

# 配合getattr()、setattr()以及hasattr()
# 我们可以直接操作一个对象的状态


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(getattr(obj, 'y'))  # 获取属性'y'

# 试图获取不存在的属性，会抛出AttributeError的错误
# getattr(obj, 'z')
# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))

# 获取对象的方法
print(hasattr(obj, 'power'))  # 有属性'power'吗？
print(getattr(obj, 'power'))  # 获取属性'power'
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)  # fn指向obj.power
print(fn())  # 调用fn()与调用obj.power()是一样的
