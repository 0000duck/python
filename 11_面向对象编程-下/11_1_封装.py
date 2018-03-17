"""
封装
    私有属性：在属性前加__， 否则就是共有属性
    对外提供 get、 set方法
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 给私有属性赋值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age

    # 外界获取私有属性
    def getAge(self):
        return self.__age

# 创建一个 Person 对象
zhangSan = Person("张三", 30)
print(zhangSan.name + "的年龄为：", zhangSan.getAge())