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

# 如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
# 这种设计通常称之为MixIn


# 为了更好地看出继承关系，
# 我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
# MixIn的目的就是给一个类增加多个功能
# 优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
