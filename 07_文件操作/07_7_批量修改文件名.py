"""
批量修改文件名

********还存在点问题
"""
import os

# 创建一些文件
'''
f = open("学员信息-1.txt", "w",)
f.close()
f = open("学员信息-2.txt", "w")
f.close()
f = open("学员信息-3.txt", "w")
f.close()
f = open("学员信息-4.txt", "w")
'''

# 批量修改文件
# 标识  1：添加   2：删除
funFlag = 2
folderName = "./学员信息"

# 获取指定路径的所有文件
dirList = os.listdir(folderName)

# 遍历所有文件名
for name in dirList:
    print(name)

    if funFlag == 1:
        newName = "[黑马程序员]-" + name

    elif funFlag == 2:
        num = len("[黑马程序员]-")
        newName = name[num:]

    print("新名称 ----> ", newName)

    os.rename(name, newName)




