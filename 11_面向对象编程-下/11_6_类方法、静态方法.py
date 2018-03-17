"""
类方法
    使用 @classmethod 来表示类方法
    cls: 代表类方法所在的类，可以访问类属性

    怎样调用类方法：
        1. 类名调用
        2. 对象调用

    注意：类方法是无法访问实例属性的，单思可以访问类属性


静态方法
    使用 @staticmethod 来表示静态方法
    静态方法没有任何参数，所以不能用 self 来访问实例属性，无法用 cls 访问类属性
    静态方法跟定义他的类没有直接关系，只是起到类似类之外的函数的作用（类中的成为方法）
    如何调用：
        1. 类名调用
        2. 对象调用

总结：
    类的实例对象可以访问如下：
        1. 实例方法
        2. 类方法
        3. 静态方法

    类可以访问如下：
        1. 类方法
        2. 静态方法

几种方法的区别：
    实例方法：可以修改实例属性的值
    类方法：可以修改类属性的值
    静态方法：辅助功能，可以打印菜单等。可以不用创建对象使用，用类名直接调用
"""

"""
类方法     @classmethod
"""
class Test(object):
    # 类属性
    num = 0

    # 类方法
    @classmethod
    def setNum(cls, newNum):
        # 访问类属性num
        cls.num = newNum

# 测试
Test.setNum(300)
print("类访问 类方法： ", Test.num)

test = Test()
test.setNum(500)
print("实例对方访问 类方法： ", Test.num)
print("实例对方访问 类方法： ", test.num)




"""
静态方法  @staticmethod
"""
print("="*40)
class Test1(object):

    # 静态方法 无参数
    @staticmethod
    def printTest1():
        print("我是静态方法")

# 测试
Test1.printTest1()

test1 = Test1()
test1.printTest1()