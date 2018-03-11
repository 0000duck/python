"""
列表： []
    可存储不同类型的数据
    索引从 0 开始
"""

# 基本的list
L = [1, 'ZhangSan', True, [2, 'Lisi']]
print(L[3][1])
"""
=====================
List 循环
=====================
"""

# List 的 for 循环遍历
print('---------------------')
nameList = ['zhangsan', 'lisi', 'wangwu']
for name in nameList:
    print(name)

# List 的 while 循环遍历
print('---------------------')
listLength = len(nameList)
i = 0
while i<listLength:
    print(nameList[i])
    i += 1


"""
=====================
List 增加元素
    append()
    extend()
    insert()
=====================
"""
# append() 添加
L1 = ['zhangsan', 'lisi']
print('====================================')
print('-------添加之前 L 的数据---------')
for tempName in L1:
    print(tempName)

temp = input("请输入要添加的姓名:")
L1.append(temp)
print('-------添加之后 L 的数据---------')
for tempName in L1:
    print(tempName)

# extend() 添加
# 将一个列表添加到另外一个列表中
print('====================================')
a = [1, 2]
b = [8, 9]
print("添加之前：", a)
# 将 b 添加到 a 中
a.extend(b)
print("添加之后：", a)


# insert() 添加
# 在一个列表指定位置添加元素
print('====================================')
a = [0, 1, 2]
a.insert(1, 'binghua')
print("指定位置插入以后：", a)



"""
=====================
List 查找元素
    in
    not in
=====================
"""
print('====================================')
nameList = ['zhangsan', 'lisi', 'wangwu']
strName = 'zhangsan'
if strName in nameList:
    print("ilaoda 在 nameList 中")
else:
    print("ilaoda 不在 nameList 中")


"""
=====================
List 修改元素
    in
    not in
=====================
"""
print('====================================')
nameList = ['zhangsan', 'lisi', 'wangwu']
print("---------修改之前---------")
for name in nameList:
    print(name)
print("---------修改之后---------")
nameList[0] = "ilaoda"
for name in nameList:
    print(name)


"""
=====================
List 删除元素
    del 根据下标删除
    pop() 删除的是最后一个元素
    remove 删除给定的列表元素
=====================
"""
# del 删除
print('====================================')
cityList = ['beijing', 'shanghai', 'guangzhou', "shenzhen"]
print("---------删除前---------")
for city in cityList:
    print(city)
print("---------删除后---------")
del cityList[0]
for city in cityList:
    print(city)

# pop() 删除
print('====================================')
cityList1 = ['beijing', 'shanghai', 'guangzhou', "shenzhen"]
print("---------删除前---------")
for city in cityList1:
    print(city)
print("---------删除后---------")
cityList1.pop()
for city in cityList1:
    print(city)


# remove() 删除
print('====================================')
cityList2 = ['beijing', 'shanghai', 'guangzhou', "shenzhen"]
print("---------删除前---------")
for city in cityList2:
    print(city)
print("---------删除后---------")
cityList2.remove('shanghai')
for city in cityList2:
    print(city)




"""
=====================
List 排序
    sort()
    reverse()
=====================
"""
print('====================================')
a = [8, 2, 4, 6]
print("正序：", a)

a.reverse()
print("倒序：", a)

a.sort()
print("默认由小到大：", a)

a.sort(reverse=True)
print("由大到小：", a)



"""
=====================
List 的嵌套
    list 中包含 list
=====================
"""
print('====================================')
import random

# 定义老师
teacherName = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 定义三个办公室
offices = [[], [], []]

# 将老师随机分配到3个办公室中
for name in teacherName:
    offIndex = random.randint(0, 2)
    offices[offIndex].append(name)

# 读取出每个办公室的老师人数和姓名
i = 1
for office in offices:
    print("第 %d 办公室的人数为: %d" %(i,len(office)))
    i += 1

    for teacher in office:
        print("老师姓名：%s"%teacher)
    print("-"*20)




