# list: 列表， 有序集合 [ ]
# 作用：添加、删除
classmates = ['zhangsan', 'lisi', 'wangwu']
print(classmates)

# len()：获得 list 的元素个数，
print(len(classmates))

# classmates[]: 获得 list 的每一个元素，索引从 0 开始
# 最后的一个元素索引: len(classmates)-1, 或者-1做最后一个元素索引
print(classmates[2])
print(classmates[-1])

# append():  最后追加元素
classmates.append('zhaoliu')
print(classmates)

# insert(): 插入到指定位置的元素
classmates.insert(1, 'ilaoda')
print(classmates)

# pop(): 删除 list 末尾元素
classmates.pop()
print(classmates)

# pop(i): 删除指定位置元素
classmates.pop(1)
print(classmates)

# list[i]: 替换指定位置元素
classmates[1] = 'lisilisi'
print(classmates)

# list 中元素类型可以不同
L = ['China', 123, True]
print(L)

# list 中可以包含 list
s = ['python', 'java', ['asp', 'C++'], 'PHP']
print(s)
print(len(s))

a = ['asp', 'php']
aa = ['python', 'java', a, 'scheme']
# 拿到 php, 可以看作二维数组
print(a[1])
print(aa[2][1])

# list 为空, 长度为0
L = []
print(L)
print(len(L))





