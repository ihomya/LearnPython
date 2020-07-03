#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
# 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Michael Liao'  # 使用__author__变量把作者写进去

import sys


def test():
    args = sys.argv  # sys模块有一个argv变量，用list存储了命令行的所有参数
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码
if __name__ == '__main__':
    test()


# 正常的函数和变量名是公开的（public），可以被直接引用
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private）,不应该被直接引用，比如_abc，__abc等
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了
# 调用greeting()函数不用关心内部的private函数细节，
# 这也是一种非常有用的代码封装和抽象的方法
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 外部不需要引用的函数全部定义成private，
# 只有外部需要引用的函数才定义为public
