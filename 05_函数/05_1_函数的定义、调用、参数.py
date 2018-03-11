"""
def 函数名(参数)：
    ''' 函数说明 '''
    函数体
    return 表达式

函数的使用必须在 定义之后

-------------
不定长参数
参数的定义：
    formal: 会优先匹配普通参数的个数，超出后匹配下面两个
    *args: 元组存放。 匹配超出的没有指定名称的参数
    **kwargs: 字典存放。匹配超出指定名称的参数
"""


"""
默认参数
    定义函数的时候，给参数设置默认值
    这个参数已经要位于参数列表的末尾
"""
def printinfo(name, age=35):
    print("name: ", name)
    print("age: ", age)
    print("------------")

printinfo("zhangsan", 15)
printinfo("lisi")
printinfo(name="wangwu", age=80)


"""
不定长参数
参数的定义：
    formal: 会优先匹配普通参数的个数，超出后匹配下面两个
    *args: 元组存放。 匹配超出的没有指定名称的参数
    **kwargs: 字典存放。匹配超出指定名称的参数
"""

# 匹配 *args 元组
print("------------")
def test(a, b, *args):
    print(a)
    print(b)
    print(args)
test(11, 22, 33, 44, 55, 66, 77, 88)


# 匹配 *args 元组 和 **kwargs 字典
print("------------")
def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
test(11, 22, 33, 44, 55, 66, 77, m=88, n=99)