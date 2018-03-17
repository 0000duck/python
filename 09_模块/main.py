"""
不用在调用 test.py 的 add() 方法的时候，打印处 test.py 的测试语句

__name__   属性, 每个模块都有一个这个属性
    当其值为 '__main__' 时， 表明该模块自身在运行，也就是这个时候可以打印测试语句。否则就是被其他模块引用。




"""

import test

result = test.add(10, 20)
print("main.py 文件中, 调用 test.py add()方法的值为：%d" %result)