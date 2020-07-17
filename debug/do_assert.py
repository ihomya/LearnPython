def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    # assert的意思是，表达式n != 0应该是True，否则后面的代码肯定会出错
    return 10 / n


def main():
    foo('0')


main()  # AssertionError: n is zero!
# Python解释器时可以用-O参数来关闭assert(python -O err.py)
