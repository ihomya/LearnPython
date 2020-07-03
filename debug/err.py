# err.py:
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()
# Traceback (most recent call last): 告诉我们这是错误的跟踪信息
#   File "e:/Administrator/Documents/PythonProjects/LearnPython/debug/err.py", line 14, in <module>
#     main()
#   File "e:/Administrator/Documents/PythonProjects/LearnPython/debug/err.py", line 11, in main
#     bar('0')
# 调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行
#   File "e:/Administrator/Documents/PythonProjects/LearnPython/debug/err.py", line 7, in bar
#     return foo(s) * 2
# 调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行
#   File "e:/Administrator/Documents/PythonProjects/LearnPython/debug/err.py", line 3, in foo
#     return 10 / int(s)
# 原因是return foo(s) * 2这个语句出错了，但这还不是最终原因
# ZeroDivisionError: division by zero
# 原因是return 10 / int(s)这个语句出错了，这是错误产生的源头
