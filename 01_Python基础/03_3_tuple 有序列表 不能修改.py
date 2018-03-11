# tuple 元组 ( )
# 初始化后不能修改，这样代码更安全
classmates = ('zhangsan', 'lisi', 'wangwu')
print(classmates)

# 定义的时候，tuple 元素就被定下来
t = (1, 2, 'zhangsan')
print(t)
print(len(t))

# 定义空tuple
t = ()
print(t)  # ()

# 数字 tuple
# 此处的() 表示运算优先级的括号，并不是 tuple
s = (5)
print(s) # result: 5, 并不是(5)

# 因此只有 1 个元素的 tuple, 要加逗号 ,
r = ('zhangsan',)
print(r) # result: ('zhangsan',)

# "可变的tuple"
# 为何最后的x值变了
# 表面上变是tuple, 但实际上变的是 list中的内容
# tuple所谓的“不变”是说，tuple的每个元素指向永远不变。
x = ('a', 'b', ['A', 'B'])
print(x) # ('a', 'b', ['A', 'B'])
x[2][0] = 'X'
x[2][1] = 'Y'
print(x) # ('a', 'b', ['X', 'Y'])


print('h'*19)







