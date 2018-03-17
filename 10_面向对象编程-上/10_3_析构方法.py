"""
析构方法
    __del__()  析构方法

    当删除一个对象来释放所占用的资源时候，默认自动执行析构方法
        程序结束的时候，自动释放
        手动释放 del 对象名, 删除对象，释放他所占用的资源
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("析构方法， 释放资源: ", self)

zhangSan = Person("张三", 30)

# 手动释放
del zhangSan
print("手动释放 zhangSan 对象")

