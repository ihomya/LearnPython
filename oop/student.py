# 类是创建实例的模板
class Student(object):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # 方法就是与实例绑定的函数,方法可以直接访问实例的数据
    def get_gender(self):
        print('%s的性别：%s' % (self.name, self.gender))

    # 常见的封装形式
    def get_age(self):
        print('%s的年龄：%s' % (self.name, self.age))


stu1 = Student('leeyanhom', 'man', 23)  # 实例则是一个一个具体的对象
stu1.get_gender()
stu1.get_age()
stu1.score = 90  # 和静态语言不同，Python允许对实例变量绑定任何数据
print(stu1.score)
