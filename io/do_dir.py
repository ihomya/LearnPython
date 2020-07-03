import os

print(os.name)  # 查看操作系统类型（linux,unix,mac os x是posix，windows是nt）
# os.uname() 获取详细的系统信息 windows不提供
print(os.environ)  # 返回环境变量
print(os.environ.get('PATH'))  # 返回某个环境变量的值
# os.environ.get('x', 'default') 返回default
print(os.path.abspath('.'))  # 返回当前目录的绝对路径

# 合并路径
testdir = os.path.join(
    'E:\Administrator\Documents\PythonProjects\LearnPython', 'testdir')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir(testdir)  # 然后创建一个目录:
os.rmdir(testdir)  # 删除目录

# 拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))
# 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# 返回 ('/Users/michael/testdir', 'file.txt')
print(os.path.splitext('/path/to/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名

# 重命名
os.rename(
    'e:/Administrator/Documents/PythonProjects/LearnPython/io/test.txt', 'io/test.md')

os.rename(
    'e:/Administrator/Documents/PythonProjects/LearnPython/io/test.md', 'io/test.txt')

# 删除文件
# os.remove('io/test.txt')

# import shutil 模块提供了copyfile()的函数

# 过滤文件
print([x for x in os.listdir('.') if os.path.isdir(x)])  # 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py'])
# 列出所有的.py文件
