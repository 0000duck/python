"""
索引、 分片   的重载

    __getitem__  索引、分片
    __setitem__  索引赋值
    __delitem__  索引、分片删除

"""
# __getitem__  索引、分片
class Demo:
    def __init__(self, obj):
        self.data = obj[:]

    # 索引、分片运算符重载
    def __getitem__(self, index):
        return self.data[index]


x = Demo([1, 2, 3, 4])
print(x[1])
print(x[:])
print(x[:2])

for num in x:
    print(num)


# __setitem__  索引赋值
print("="*20)
class Demo1:
    def __init__(self, obj):
        self.data = obj[:]

    # 重载索引、分片的赋值方法
    def __setitem__(self, index, value):
        self.data[index] = value

x1 = Demo1([1, 2, 3, 4, 5])
print("显示所有元素：%s" %(x1.data))

x1[0] = "abc"
print("修改第一个元素：%s" %(x1.data))

x1[1:3] = ['a', 'b', 'c']
print("修改部分元素：%s" %(x1.data))


# __delitem__  索引、分片删除
print("="*20)
class Demo2:
    def __init__(self, obj):
        self.data = obj[:]

    # 重载索引、分片删除运算符
    def __delitem__(self, index):
        del self.data[index]

x2 = Demo2([1, 2, 3, 4, 5])
print("显示所有元素：%s" %(x2.data))

# 删除以一个元素
del x2[0]
print("删除第一个元素后：%s" %(x2.data))

# 删除部分元素，即删除分片
del x2[1:3]
print("删除部分元素后：%s" %(x2.data))


