
# 变量
nameList = [] # 名片

# 显示主菜单
def displayMenu():
    print("-"*30)
    print("======名片管理系统======")
    print("1. 添加名片")
    print("2. 删除名片")
    print("3. 修改名片")
    print("4. 查询名片")
    print("5. 查询所有名片")
    print("6. 退出系统")
    print("======名片管理系统======")

# 获取用户选择的菜单
def getChoice():
    selectedKey = input("请输入你要选择的菜单项： ")
    return int(selectedKey)

# 添加名片
def addInfo():
    name = input("请输入你的姓名：")
    nameList.append(name)

# 查询所有名片
def showAllInfo():
    print("=========所有名片信息===========")
    for info in nameList:
        print(info)
    print("==============================")


# 主入口
i = 0

while  i<1:
    # 打印菜单
    displayMenu()

    # 选择菜单项
    key = getChoice()

    # 菜单项匹配
    # 添加名片
    if key == 1:
        addInfo()
    elif key == 2:
        pass
    elif key == 3:
        pass
    elif key == 4:
        pass
    # 查询所有名片
    elif key == 5:
        showAllInfo()
    elif key == 6:
        pass
