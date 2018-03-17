"""
抛出异常
    raise 异常类
    raise 异常类对象
    raise
"""

# 使用类名引发异常
# raise IndexError

# 使用异常类的实例引发异常
'''
index = IndexError()
raise index
'''

# 传递异常
# 不带任何参数的 raise 语句
'''
try:
    raise IndexError
except:
    print("出错了")
    raise # 又发生了和上面一样的异常。在异常快中又出现了异常
'''

# 指定异常的描述信息
# raise IndexError("索引下标越界异常")


# 异常引发异常，即异常中再抛异常
# 会抛出两个异常
try:
    num
except Exception as exceptionName:
    raise IndexError("下标越界") from exceptionName