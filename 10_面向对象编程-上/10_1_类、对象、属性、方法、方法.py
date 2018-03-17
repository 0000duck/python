"""
类
    类的定义
    对象的创建
    属性
    方法

类中的方法必须显示的声明一个 self 参数， 而且该参数要位于参数列表的开始
self 代表类的实例（对象）本身，可以用来引用对象的属性和方法
"""

# 定义类
class Car:
    # 移动方法
    def move(self):
        print("车在奔跑")
    # 鸣笛
    def toot(self):
        print("车在鸣笛。。。嘟嘟嘟。。。")


# 创建一个 Car的对象
BWM = Car()

# 给对象添加一个颜色属性
BWM.color = "黑色"

# 调用方法 和 属性
BWM.move()
BWM.toot()
print(BWM.color)