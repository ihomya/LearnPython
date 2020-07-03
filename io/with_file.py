# 读取文件open('传入文件名','标识符')
# f = open('/Users/Admin/test.txt', 'r')  # 标示符'r'表示读
# 文件不存在，抛出FileNotFoundError错误


try:
    f = open('E:/Administrator/Documents/PythonProjects/LearnPython\io/test.txt', 'r')
    print(f.read())  # 调用read()方法可以一次读取文件的全部内容
finally:
    if f:
        # 调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
        f.close()

# with语句来自动帮我们调用close()方法
# with open('/path/to/file', 'r') as f:
#     print(f.read())

# 反复调用read(size)方法，每次最多读取size个字节的内容。
# 调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list

# 如果是配置文件，调用readlines()最方便：

f = open('E:/Administrator/Documents/PythonProjects/LearnPython\io/test.txt', 'r')

for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉

# 读取二进制文件
with open('E:/Administrator/Pictures/背景.jpg', 'rb') as f1:
    print(f1.read(100))

# 字符编码文件读取
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件（标识符'w'）
f = open('E:/Administrator/Documents/PythonProjects/LearnPython\io/test.txt', 'w')
f.write('abcdefg')
f.close()

# 保证写入数据不丢失
with open('E:/Administrator/Documents/PythonProjects/LearnPython\io/test.txt', 'a') as wf:
    wf.write('abcdefg')

# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
# 如果我们希望追加到文件末尾可以传入'a'以追加（append）模式写入

# 练习
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
