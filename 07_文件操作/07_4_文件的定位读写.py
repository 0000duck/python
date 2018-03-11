"""
文件的定位读写
    需要从文件的某个特定位置来读写

    tell() 获取文件当前的读写位置
    seek() 定位到文件的指定读写位置
"""

# tell()
f = open("itheima.txt", "r")
str = f.read(4)
print("读取的数据是： ", str)
# 查找当前的位置
position = f.tell()
print("文件的当前位置是: ", position)
f.close()



# seek() 重新定位当前位置
print("-----------")
f = open("itheima.txt", "rb+")
str = f.read(4)
print("seek 读取的位置是： ", str)

# 查找当前的位置
position = f.tell()
print("当前的位置是： ", position)

# 重新设置位置
f.seek(10)
# 查找当前的位置
position = f.tell()
print("seek 读取当前的位置是： ", position)
f.close()



# seek() 在当前位置偏移 4 个字节
print("-----------")
f = open("itheima.txt", "rb+")
str = f.read(3)
print("当前的字符串是：", str)
position = f.tell()
print("当前的位置是： ", position)

# 在当前位置开始偏移
f.seek(5,1)
position = f.tell()
print("查找当前的位置： ", position)
f.close()




# seek() 定位在文件末尾的 3 个字节处
print("-----------------")
f = open("itheima.txt", "rb+")
f.seek(-4, 2)
# 当前的位置
position = f.tell()
str = f.read(position)
print("当前的位置是： ", position)
print("读取的内容是：", str)

















