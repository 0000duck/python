"""
定义 test 模块

"""

def add(a, b):
    return a + b


# 测试代码， 一直执行
#ret = add(12, 22)
#print("测试方法 ----> int test.py file, 12 + 22 = %d" %ret)


# 对测试代码修改，只有自己本模块本身执行的时候，才会执行 add() 方法
if __name__ == '__main__':
    ret = add(12, 22)
    print("测试方法 ----> int test.py file, 12 + 22 = %d" %ret)


