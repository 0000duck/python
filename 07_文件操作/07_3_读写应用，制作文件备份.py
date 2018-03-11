oldFileName = input("请输入要备份的文件的名称：")

# 打开旧文件
oldFile = open(oldFileName, "r")

# 如果可以打开
if oldFile:
    # 读取最后一个 . 的索引
    fileFlagNum = oldFileName.rfind('.')
    if fileFlagNum > 0:
        # 获取后缀，将索引处到末尾的内容，赋值给 fileFlag, 即后缀
        fileFlag = oldFileName[fileFlagNum:]

        # 新文件的名字
        newFileName = oldFileName[:fileFlagNum] + '-附件' + fileFlag

    # 创建新的文件
    newFile = open(newFileName, 'w')

    # 把旧文件的内容，一行一行复制到新文件中
    for lineContent in oldFile.readlines():
        newFile.write(lineContent)

# 关闭文件
oldFile.close()
newFile.close()