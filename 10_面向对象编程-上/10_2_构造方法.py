"""
构造方法
    __init__()  构造方法
        初始化对象的属性
        创建类的实例的时候，系统自动调用该方法

    __del__()  释放类所占用的资源
"""

"""
构造1
"""
class Car:
    def __init__(self):
        self.color = "黑色"
    def toot(self):
        print("%s 颜色的车正在鸣笛" %(self.color))

car = Car()
car.toot() #黑色 颜色的车正在鸣笛


"""
创建对象的时候，通过传递参数，动态的设值
"""

print("="*20)
class Dog:
    def __init__(self, type):
        self.type = type

    def run(self):
        print("%s 正在跑" %(self.type))

langDog = Dog("狼狗")
zangDog = Dog("藏獒")

langDog.run()
zangDog.run()




