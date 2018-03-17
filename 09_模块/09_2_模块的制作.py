"""
    每个 Python 文件都可以作为一个模块
    模块的名字就是 文件的名字

"""

"""
import test
result = test.add(1, 2)
print("test: ", result)

"""

# 已下两种情况用 test.add() 是错误的
# 用了 from 导入模块后， 不能在实际使用的时候用 模块名.方法

"""
from test import add
result = add(2,3)
print("result: ", result)
"""

from test import *
result = add(9,3)
print("result: ", result)