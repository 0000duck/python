"""
文件夹的相关操作
    创建
    获取当前目录
    改变默认目录
    获取目录列表
    删除文件夹
"""
import os

# 创建文件夹
# os.mkdir("zhangsan")

# 获取当前的目录
dir = os.getcwd()
print("当前的目录： ", dir)

# 改变默认目录
# os.chdir("../")


# 获取目录列表
dirList = os.listdir("./")
for dir in dirList:
    print(dir)


# 删除文件夹
os.rmdir("zhangsan")





