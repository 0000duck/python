"""
随机数函数：
    random()
    uniform()
    randint()
    randrang()
    choice()
    shuffle()
    sample()
"""
import random


# random() 生成的值范围  0 <= n < 1.0
print("-----------")
print("随机数 random(): ", random.random())

# uniform()  两个参数之间的浮点数  [x, y] 闭合的
print("-----------")
print("参数之间的随机数 uniform(): ", random.uniform(50, 100))
print("参数之间的随机数 uniform(): ", random.uniform(100, 50))

# randint() 返回两个参数之间的整数， 且第一个参数 < 第二个参数， 两个参数必须取整, 且[]
print("-----------")
print("参数之间的随机整数 randint(): ", random.randint(10, 50))
print("参数之间的随机整数 randint(): ", random.randint(10, 11))
# print("参数之间的随机整数 randint(): ", random.randint(50, 11)) # 第一个参数必须小


# randrang() 返回两个参数区间，每隔固定数字的数的随机数
# 返回的是10，20，30，..., 100 这10个数之中的一个随机数
print("-----------")
print("参数之间的固定数字 randrang(): ", random.randrange(10, 100, 10))

# choice() 返回给定的数据类型中的一个元素。 给定的类型数据可以是： 字符串， list, tuple, dict
print("-----------")
print("任意数据类型中的一个元素 choice()： ", random.choice("我爱你中国"))
print("任意数据类型中的一个元素 choice()： ", random.choice(["shanghai", "beijing"]))
print("任意数据类型中的一个元素 choice()： ", random.choice(("ilaoda", 123, "哈哈")))
#print("任意数据类型中的一个元素： ", random.choice({'name':'xioahua', 'age':22}))

# shuffle() 将列表中的数据打乱  洗牌
print("-----------")
L = ["111", "222", "333", "444"]
random.shuffle(L)
print("打乱列表数字 shuffle()：", L)


# sample() 在指定的序列中，随机获取k个元素作为一个片段返回
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice = random.sample(list, 3)
print("提取的片段 sample()：", slice)
print("原 list 没有改变： ", list)












