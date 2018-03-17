"""
预定义清理：
    除了finally中可以释放资源意外，也可以用预定义清理with
    作用：无论资源在使用过程是否发生异常，都会执行释放资源的操作，如文件使用后的自动关闭

    格式：
        whih 上下文表达式 [as 资源对象]
            对象的操作

"""

"""
with 语句
"""
with open("foo.txt", "w+") as file:
    data = file.read()





