from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'leeyanhom'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):
    self.age = age


# 给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(23)
age = s.age
print(age)


# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)

s2 = Student()
s2.set_score(99)
print(s2.score)


# 使用__slots__限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99  # 绑定属性'score' 报错AttributeError


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
