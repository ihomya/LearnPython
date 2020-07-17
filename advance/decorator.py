import time
import functools
# 修饰器


def now():
    print('2015-3-25')


# 函数也是一个对象，而且函数对象可以被赋值给变量
f = now
# 通过变量也能调用该函数
f()
# 函数对象有一个__name__属性
print(now.__name__)  # 返回函数名
# 假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数


# 定义如下
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log  # 相当于执行了 now = log(now)
def now():
    print('2015-3-25')


now()
# 如果decorator本身需要传入参数，
# 那就需要编写一个返回decorator的高阶函数，写出来会更复杂
# 比如，要自定义log的文本


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')  # 相当于 now = log('execute')(now)
def now():
    print('2015-3-25')


now()
print(now.__name__)  # 此时__name__的值为‘wrapper’


# 所以一个完整的decorator的写法如下：
# import functools
def log(func):
    @functools.wraps(func)  # 相当于执行 wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 或者针对带参数的decorator：
#import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')  # 相当于 now = log('execute')(now)
def now():
    print('2015-3-25')


print(now.__name__)

# 练习
# import time, functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        result = fn(*args, **kw)  # 执行
        end_time = time.time()
        run_time = end_time - start_time
        print('%s executed in %s ms' % (fn.__name__, run_time))
        return result
    return wrapper

# 测试


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
