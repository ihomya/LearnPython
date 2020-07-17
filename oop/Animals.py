class Animal(object):
    pass

# 大类:


class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 其他类


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
# 多重继承
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Flyable):
    pass
