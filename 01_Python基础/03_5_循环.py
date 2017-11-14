"""
for...in... 循环
"""

names = ['zhangsan', 'lisi', 'wangwu']
for name in names:
    print('for...in..循环：', name)

# range(): 生成从0开始的几个蓄力整数
list = list(range(10))
print('list集合为： ', list)


# 循环相加
sum = 0
for x in list:
    sum = sum + x
print('sum的和为：', sum)


""" 
while 循环
"""
sum = 0
n = 1
while n < 100:
    sum = sum + n
    n = n + 2
print(sum, '\n')


""" 
break 终止循环，退出方法
"""
n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('程序终止，n为：', n) # 11


""" 
continue 终止本次循环，继续下次循环
"""
# 打印1-10
# 只打印奇数
n = 0
while n<10:
    n = n + 1
    if n%2 == 0:
        continue
    print(n)


