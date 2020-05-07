# 练习
height = input('输入你的身高：')
weight = input('输入你的体重：')
h = float(height)
w = float(weight)
BMI = h / w
if BMI < 18.5:
    print('过轻')
elif BMI < 25 & BMI >= 18.5:
    print('正常')
elif BMI < 28 & BMI >= 25:
    print('过重')
elif BMI <= 32 & BMI >= 28:
    print('肥胖')
elif BMI > 32:
    print('过度肥胖')