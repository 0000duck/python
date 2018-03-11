"""
元组 ：tuple     ()
    中的元素不能修改、删除
    下标从 0 开始
"""

tup1 = ("beijing", "shanghai", "guangzhou", "shenzhen")

"""
=====================
访问 tuple
=====================
"""
print(tup1[1])


"""
=====================
修改 tuple， 只是将两个合并，并不是真正的修改
=====================
"""
tup1 = ("beijing", "shanghai", "guangzhou", "shenzhen")
tup2 = ("hangzhou", "chengdu")

# 不能修改
# tup1[0] = "nanjing"

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)


"""
=====================
遍历 tuple
=====================
"""
for city in tup3:
    print(city, end=" " )

print("---------")
i = 0
while i<len(tup3):
    print(tup3[i], end=" " )
    i += 1



"""
=====================
tuple 内置函数
    len()
    max()
    min()
    tuple(list) List转换为Tuple
=====================
"""
print("---------")
tup4 = (8, 4, 15)
print("tup4 长度: %s"%len(tup4))
print("tup4 最大值: %s"%max(tup4))
print("tup4 最小值: %s"%min(tup4))

list = ["baidu", "ali", "tencent"]
tup5 = tuple(list)
print(tup5)










