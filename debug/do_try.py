def some_function():
    pass


def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r


def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)  # 当错误发生时，后续语句print('result:', r)不会被执行
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:  # 如果执行出错，则直接跳转至错误处理代码
    print('except:', e)
else:
    print('no error!')
finally:  # 执行完except后，如果有finally语句块，则执行finally语句块
    print('finally...')
print('END')

try:
    foo()
# except不但捕获该类型的错误，还把其子类也“一网打尽”
except ValueError as e:
    print('ValueError')
except UnicodeError as e:  # UnicodeError 是 ValueError的子类，因此永远无法捕获到
    print('UnicodeError')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    # 可以跨越多层调用
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
