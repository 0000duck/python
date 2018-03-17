"""
模块的基本使用
    在Python中，一个.py文件就称之为一个模块（Module）
    Python又引入了按目录来组织模块的方法，称为包（Package）。

    import 模块名

    在函数的使用中，如果要调用某个模块的函数：  模块名.函数名

    有时候只需要模块中的某个具体函数，不用全部导入：    from 模块名 import 函数名1, 函数名2...
    例如  from fib import fibonacci
    这种方式的问题：
        1. 使用的时候，只能使用函数名，不能给出模块名
        2. 当两个模块有相同的函数时，后面一次引入会覆盖前面的

    将一个模块的所有内容导入到当前命名空间：(不建议使用)
        from 模块名 import *
        例如: from math import *
"""

# python 模块搜索路，保存在 sys模块的 path 变量中
import sys
import fibo
print("模块的路径： ", sys.path)

fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

# 可以将一个函数赋值给一个本地变量，经常使用

mfib = fibo.fib
mfib(1000)












