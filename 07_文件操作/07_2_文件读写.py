"""
文件的读写
    write()  每调一次，写入的数据就会追加到文件末尾
"""

# write() 先打开，再写入
# 注意，如果这个文件存在，会先覆盖 *****************
print("-"*20)
f = open('itheima.txt', 'w')

f.write("hello itheima, i am here!\n")
f.write("welcome to beijing\n")
f.write("this is shanghai\n")
f.close()


# 文件的读 read(size)
# size 为读取的数据长度为字节，没有指定则读取全部数据
# ??? 为何最后的全部内容不全？？？
print("-"*20)
f = open("itheima.txt", "r")
content = f.read(12)
print("读取12字节的大小： ", content)
content = f.read()
print("读取全部内容： ", content)
f.close()


# 文件的读 readlines()
# 读全部，但是返回的是一个列表。列表中每个元素为一行
print("-"*20)
f = open("itheima.txt", "r")
content = f.readlines()
i = 1
for temp in content:
    print("第 %d 行的内容为：%s" %(i, temp))
    i += 1
f.close


# 文件的读 readlines()
# 一行一行的读
print("-"*20)
f = open("itheima.txt", "r")
content = f.readline()
print("111: ", content)
content = f.readline()
print("222: ", content)
content = f.readline()
print("333: ", content)
