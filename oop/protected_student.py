class Student(object):
    def __init__(self, name, score, gender):
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
        self.__name = name
        self.__score = score
        self.__gender = gender

    # 让外部代码可以获取内部属性
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    # 允许外部代码修改内部属性
    def set_score(self, score):
        # 在方法中，可以对参数做检查，避免传入无效的参数
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')


# 类似_name的实例变量名，虽然可以被访问，但是应视为私有变量，不可随意访问
# 双下划线开头的实例变量不能直接访问__name
# 是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：
# name = object._Student__name
# 不同版本的Python解释器可能会把__name改成不同的变量名,所以一般不使用
print(name)
# 测试:
bart = Student('Bart', 80, 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
