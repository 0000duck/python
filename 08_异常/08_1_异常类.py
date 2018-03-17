"""

所有的异常都是 Exception 的子类

常见异常类
    1. NameError
        访问一个未声明的变量


"""
# NameError
# print(foo)
# NameError: name 'foo' is not defined


# ZeroDivisionError
# ZeroDivisionError: division by zero
# print(1/0)


# SyntaxError
# SyntaxError: invalid syntax
'''
list = [1, 2]
for i in list
    print(i)
'''


# IndexError
# IndexError: list index out of range
'''
list = []
print(list[0])
'''

# KeyError
# KeyError: 'sex'
'''
dict = {"name":"zhangsan", "age":80}
print(dict["sex"])
'''

# FileNotFoundError
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# f = open("test.txt")


# AttributeError
# AttributeError: 'Car' object has no attribute 'name'
'''
class Car(object):
    pass

car = Car()
car.color = "blue"
print(car.color)
print(car.name) # 没有声明 name 属性
'''



