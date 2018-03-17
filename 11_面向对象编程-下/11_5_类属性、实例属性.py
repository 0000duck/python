"""
类属性
    在类中声明的属性，即在方法外的属性
    访问：
        类名访问
        实例对象访问
    他是所有类的实例对象所共有的，在内存中只存在一个副本

实例属性
    在方法中定义的属性
    访问：
        只能是实例对象访问

注意：
    如果类属性 和 实例属性相同
        通过对象访问的是实例属性
        通过类名访问的是类小户型
"""

# 定义类
class Cat(object):
    # 类属性
    num = 0

    # 实例属性-在方法中
    def __init__(self):
        # self.num = 100
        self.age = 20

# 测试
cat = Cat()
# print(cat.num)
print(Cat.num)
print(cat.num)