# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()
print(type(Hello))  # 类<class 'type'>

print(type(h))  # 实例 <class '__main__.Hello'>

# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 通过type()定义类


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hellox = type('Hellox', (object,), dict(hello=fn))  # 创建Hellox class
# 创建一个class对象，type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
hx = Hellox()
print(type(hx))
print(type(Hellox))
