"""
while 循环



for 循环
for 变量 in 序列：
    循环语句
"""
# 当i的值为end 9时候，循环结束。 [5, 9)

for i in range(5, 9):
    print("i的值为： ", i)

# 打印杨辉三角
i = 1
while i < 6:
    j = 0
    while j < i:
        # end = '', 就不会导致换行了
        print("* ", end='')
        j += 1

    print("\n")

    i += 1


# 打印乘法口诀表
x = 1
while x < 10:
    y = 1
    while y <= 1:
        print("%d x %d = %-2d"%(x, y, x*y), end='')
        y += 1
    print("\n")
    i += 1
