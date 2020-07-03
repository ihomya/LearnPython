# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 但也可以直接在实例本身上调用
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()  # self参数不要传入

# 能被调用的对象就是一个Callable对象
# 可通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Student()))
print(callable([1, 2, 3]))
print(callable(None))
