# 格式化字符串
# 占位符 %s 替换内容 字符串
print('Hello,%s'% 'world')
# 占位符 %d 替换内容 整数
print('your age is %d'% 18)
# 占位符 %f 替换内容 浮点数
print('PI is %f'% 3.1415)
# 占位符 %x 替换内容 十六进制整数
print('16的十六进制是 %x'% 16)
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))
# 用%%来表示一个%
print('growth rate: %d %%' % 7)

# format()函数用于格式化字符串,用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))