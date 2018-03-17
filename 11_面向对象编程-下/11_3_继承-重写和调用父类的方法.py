"""
子类重写父类的方法
    必须满足：子类重写的方法要和父类被重写的方法具有相同的方法名 和 参数列表

同时重写还有以下几个特点：
    父类的构造可以被子类继承重写
    super() 可以在子类构造中去访问父类构造方法，虽然父类的构造是 __init__ 也可以访问


调用父类的方法  super()
"""
# 父类
class Person(object):
    def sayHello(self):
        print("父类---Hello")

# 子类，重写父类的方法
class Chinese(Person):
    def sayHello(self):
        print("子类重写 --- 你好，吃饭了吗？")

# 测试
chinese = Chinese()
chinese.sayHello()



"""
调用父类的方法  super()
"""
# 定义父类
class Animal(object):
    def __init__(self, legNum):
        # 腿的数量
        self.legNum = legNum

# 子类，继承子父类
class Bird(Animal):
    # 重写父类构造
    def __init__(self, legNum):
        # 增加羽毛颜色的属性
        self.plume = "白色"

        # 还想要父类腿的属性，用 super() 调用父类的构造
        super().__init__(legNum)

# 测试
bird = Bird(2)
print("一只白鹤鸟有 %s 条腿，羽毛是 %s 颜色的" %(bird.legNum, bird.plume))


