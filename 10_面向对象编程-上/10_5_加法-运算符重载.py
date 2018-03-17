"""
运算符重载：
    平常的运算符是对数字等的操作。
    而这里的是对 对象 的加、减、乘、除等操作。

"""
class Demo:
    def __init__(self, obj):
        self.data = obj[:]

    # 将两个列表中的对应的元素想加
    def __add__(self, obj):
        x = len(self.data)
        y = len(obj.data)
        max = x if x > y else y

        nl = []

        for n in range(max):
            nl.append(self.data[n] + obj.data[n])

        # 返回包含新列表的实例对象
        return Demo(nl[:])

# 创建实例对象并初始化
x = Demo([1, 2, 3])
y = Demo([10, 12, 13])

# 执行加法运算
z = x + y

print(z.data)


