# 字符串的下标从 0 开始
# python不支持单个字符，单个字符也是用字符串表示

"""
切片：
    作用：截取操作对象中其中的一部分
    支持对象：字符串、列表、元组
    表示 [起始：结束：步长]， 属于 左闭右开
"""

# 切片实例
name = "abcdef"
print(name[0:3]) # abc
print(name[3:5]) # de
print(name[1:-1]) # bcde
print(name[2:]) # cdef
print(name[::2]) # 不懂， 取步长为2的字符，可以是负的，表示倒序