"""
闭包：内部嵌套的函数成为闭包

闭包需要满足的 3 个条件：
    1. 存在于嵌套关系的函数中
    2. 嵌套的内部函数 引用了 外部函数的变量
    3. 嵌套的外部函数 返回值 是内部函数名
"""

# 外部函数
def outer(start=0):
    count = [start]

    # 内部函数
    def inner():
        count[0] += 1 #引用外部函数的变量
        return  count[0]

    # 外部函数返回内部函数名
    return inner()

# 函数使用
out = outer(start=5)
print(out)