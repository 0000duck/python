"""
字符串运算符
    +
    *
    []
    [:]
    in
    not in
    r/R
"""

str1 = "bread and "
str2 = "milk"
print("连接：", str1 + str2)
print("-"*15)
print("指定索引的字符：", str1[2])
print("截取一部分：", str1[2:4])
print("and是否在str1中：", 'and' in str1)
print("and是否在str1中：", 'and' not in str1)