"""
多态
    调用同一个方法，出现了两种表现形式
    多态指在不考了对象类型的情况下使用对象，而关注的是对象具有的行为？？？ 如何理解
"""

# 父类
class Animal(object):
    def shout(self):
        print("父类——动物在叫")


# 子类——狗
class Dog(Animal):
    def shout(self):
        print("子类——狗 在叫")

# 子类——猫
class Cat(Animal):
    def shout(self):
        print("子类——猫 在叫")

# 测试
# 定义一个函数
def func(temp):
    temp.shout()  # 多态指在不考了对象类型的情况下使用对象

dog = Dog()
func(dog)

cat = Cat()
func(cat)