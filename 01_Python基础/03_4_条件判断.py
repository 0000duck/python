# True: 非零整数， 非空字符串， 非空list等
a = 4

if a >= 18:
    print('成人')
elif a >= 12:
    print('青年')
else:
    print('小孩')

# input(): 输入函数
# int(): 将字符串转换为 整型
'''
s = input('请输入出生日期：')
birth = int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
'''

# 练习
height = 1.75
weight = 80.5
BMI = weight / (height*height)

if BMI >= 32:
    print('严重肥胖')
elif (28 <= BMI < 32):
    print('肥胖')
elif (25 <= BMI < 28):
    print('过重')
elif (18.5 <= BMI < 25):
    print('正常')
else:
    print('过轻')






