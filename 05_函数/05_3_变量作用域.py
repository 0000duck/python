"""
变量的作用域 - LEDB 原则：
    取决于：这个变量是在哪里赋值的

    L：函数内部的区域， 局部变量 和 形参
    E: 外面嵌套函数区域，常见的是闭包函数外的函数 *******
    G: 全局作用域
    B: 内建作用域 *****88

    查找规则也是 从上到下 查找

"""

"""
局部变量
    定义在函数内部的变量
    只能在def函数声明的内部访问和使用
"""

"""
全局变量
    定义在函数外的变量
    在整个全局内都可以访问
"""


"""
global 关键字
    作用：用来在函数内部 或者 其他局部作用域中，使用全局变量    
"""
a = 100
def test():
    # 这里明确的是对全局变量a的值做了修改，python会把a当作
    # 局部变量，可是如果是局部变量，我们并没有声明局部变量a
    # 因此，报错。
    # 因此，我们在局部中，声明下该a为全局变量。 global a
    global a
    a += 80
    print(a)
test()


"""
nonlocal 关键字
    作用：在嵌套的函数内部（类似内部类）使用，用来修改变量。
         表示这个变量是嵌套作用域中（类似外部类）的变量
"""

# 没有 nonlocal 修饰， 没有改变嵌套作用域中的值
def func1():
    count = 1
    def func1_in():
        count = 12
        print("fun1 - 内部 count的值为： ", count)
    func1_in()
    print("fun1 - 外部 count的值为： ", count)
func1()

# nonlocal 修饰， 改变嵌套作用域中的值
def func2():
    count = 3
    def func1_in():
        # 这样在内部修改的值就是外部的值了
        nonlocal count
        count = 88
        print("fun2 - 内部 count的值为： ", count)
    func1_in()
    print("fun2 - 外部 count的值为： ", count)
func2()