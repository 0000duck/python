"""
self  类中的构造或者方法的第一个参数

创建的对象是谁，调用类中的所有方法，这个self就是谁。如同 this

即将具体的对象所指的内存地址也赋值给了 self, 让 self 也指向了同一块内存区域
this 和 创建的对象指的是同一块内存区域

self.新的属性名

"""
class Dog:
    def __init__(self, newColor):
       self.color = newColor

    def printColor(self):
        print("颜色为：%s" %(self.color))


dog1 = Dog("白色")
dog1.printColor()

dog2 = Dog("黑色")
dog2.printColor()



