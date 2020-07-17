class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承
class Dog(Animal):
    # 多态
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

# 可多级继承


class Husky(Dog):
    pass


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 继承最大的好处是子类获得了父类的全部功能
dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 对数据类型的说明
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

# 用isinstance()判断数据类型
print(isinstance(a, list))
print(isinstance(b, Animal))

print(isinstance(c, Dog))
print(isinstance(c, Animal))

h = Husky()
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(c, Dog) and isinstance(c, Animal))

# 判断变量是否为某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


def run_twice(animal):
    animal.run()
    animal.run()


# 传入Animal实例
run_twice(Animal())
# 传入Dog实例
run_twice(Dog())
# 传入Cat实例
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())
# 多态真正的作用：调用方只管调用，不管细节
# 这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


# 对于静态语言（例如Java）来说，传入的对象必须是父类或者它的子类
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
