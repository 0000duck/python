"""
新建的一个 斐波那也数列 模块
让外面去调用
"""

# 定义到 n 的斐波那契数列
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


# 返回到 n 的斐波那契数列
def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result