class Student(object):

    # 内置的@property装饰器就是负责把一个方法变成属性调用的
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    # birth是可读写属性

    # 定义只读属性
    # 只定义getter方法，不定义setter方法就是一个只读属性

    # age就是一个只读属性
    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.score = 60
# 该属性不是直接暴露的，而是通过getter和setter方法来实现的
print(s.score)
# s.score = 999
# print(s.score)

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
