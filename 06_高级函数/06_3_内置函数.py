"""
内置函数：
    在Python中被自动加载的函数

"""

# map() 对指定的序列做映射
# 第二个参数的每个元素，都会去调用第一个参数的函数

func = lambda x: x+2
result = map(func, [1, 2, 3, 4, 5])
print(list(result))

# 两个参数的
result = map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
print(list(result))

# filter()
# 返回的是 迭代器中包含调用结果为 True 的元素
# function 函数只能接收一个参数
func = lambda x: x%2
result = filter(func, [1, 2, 3, 4, 5])
print(list(result))


# reduce()
# 对参数迭代器中的元素进行累积
from functools import reduce
func = lambda x, y: x+y
result = reduce(func, [1, 2, 3, 4, 5])
print(result)

# 提供了initializer参数， 如果有这个初始值，那么第一元素先和初始值计算
func = lambda x, y: x+y
result = reduce(func, [1, 2, 3, 4, 5], 10)
print(result)

# 还可以传递字符串, 计算字符串, dd初始值在前
result = reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd')
print(result)











