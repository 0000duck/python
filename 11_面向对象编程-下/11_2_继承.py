"""
class 子类名（父类名）：

如果定义类的时候，没有括号，表明默认继承自 object类

例如：
    class Person(object):  等同于 class Person:

父类私有的属性和方法，不会被子类继承，并且子类也不能访问父类私有的。

单继承

多继承： python支持多继承, 即拥有多个父类
    语法  class 子类（父类1， 父类2, ...）


多个父类同名方法
哪个父类在前面，就只执行前面父类中的同名方法
在复杂的继承关系中，python会根据__mro__() 算法找到合适的类
？？？那么能不能指定执行哪个类的同名方法呢？？？

"""

# 父类
class Cat(object):
    def __init__(self, color="白色"):
        self.color = color

    def run(self):
        print("父类的 猫 正在跑")

    # 定义私有的方法让子类访问，肯定会出错
    def __test(self):
        print("我是父类私有的方法")

    # 定义公开的方法
    def test(self):
        print("我是父类私有的方法")



# 子类，波斯猫
class PersianCat(Cat):
    pass

# 测试
persianCat = PersianCat("黑色")
persianCat.run()
print("波斯猫的颜色：%s" %persianCat.color)

# 访问父类私有的方法
# persianCat.__test()
persianCat.test()


"""
多继承
    飞鱼继承了 鸟 和 鱼类
"""
print("========== 多继承 ============")
# 父类 - 鸟类
class Bird:
    # 飞
    def fly(self):
        print("--- 鸟儿在天空飞翔 ---")

    # 测试，同名方法 breathe
    def breathe(self):
        print("鸟儿会呼吸")

# 父类 - 鱼类
class Fish:
    # 游泳
    def swim(self):
        print("--- 鱼儿在水中遨游 ---")

    # 测试，同名方法 breathe
    def breathe(self):
        print("鱼儿也会呼吸")


# 子类 - 飞鱼
class Volador(Bird, Fish):
    pass

# 测试
vola = Volador()
vola.fly()
vola.swim()

# 测试多个父类同名方法
# 哪个父类在前面，就只执行前面父类中的同名方法
vola.breathe()  # 鸟儿会呼吸




