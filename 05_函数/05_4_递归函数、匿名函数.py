"""
递归函数
    函数内部调用自己
"""

# 求 n! 的阶乘

def fn(num):
    if num == 1:
        result = num
    else:
        result = fn(num-1) * num

    return result

n = int(input("请输入你要求阶乘的数字："))
print("%d! 的阶乘为： %d" %(n, fn(n)))



"""
匿名函数
    没有函数名称的函数，不再使用 def 声明的函数
    用 lambda 关键字声明
    ----------
    定义   变量 = lambda 参数：表达式
    使用   变量（参数...）
    ----------- 
    能接受任何数量的参数
    只能返回一个表达式的值
"""
sum = lambda arg1, arg2: arg1 + arg2
print("求和的结果为： ", sum(10, 20))


# 将匿名函数 作为参数传递，可以计算不同的运算
def fun(a, b, opt):
    print("a = %d" %a)
    print("b = %d" %b)
    print("result = ", opt(a, b))

fun(11, 22, lambda x, y: x + y) # 将参数 匿名函数 传递到实际函数中
fun(11, 22, lambda x, y: x - y)


# 匿名函数例子
# 定义一个 list
stus = [
    {"name":"zhangsan", "age":10},
    {"name":"lisi", "age":30},
    {"name":"wangwu", "age":70}
]

# 下面的有些不理解
# 按照名字排序
stus.sort(key = lambda x: x['name'])
print("按 name 排序后的结果为： ", stus)

# 按照age排序
stus.sort(key = lambda x: x['age'])
print("按 name 排序后的结果为： ", stus)





















