"""
学生管理系统

"""
# 新建一个list, 用来保存学生的信息
stuInfos = []

# 主功能菜单
def printMenu():
    print("="*30)
    print("****** 学生管理系统 V0.1 *******")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 显示所有学生的信息")
    print("0. 退出系统")
    print("="*30)

# 添加学生
def addStuInfo():
    # 学生姓名
    stuName = input("请输入学生姓名：")

    # 学生性别
    stuSex = input("请输入学生性别：")

    # 学生年龄
    stuAge = input("请输入学生年龄: ")

    # 定义 dict, 保存一个学生的信息
    newStuInfo = {}
    newStuInfo['stuName'] = stuName
    newStuInfo['stuSex']  = stuSex
    newStuInfo['stuAge']  = stuAge

    # 将新添加的学生 dict, 保存到 list中
    stuInfos.append(newStuInfo)


# 删除学生
def delteStuInfo(student):
    delteNum = int(input("请输入要删除的序号： ")) - 1
    del stuInfos[delteNum]


# 修改学生
def mofifyStuInfo():
    stuId = int(input("请输入要修改学生的序号: "))
    newName = input("请输入新的学生姓名: ")
    newSex = input("请输入新的学生性别: ")
    newAge = input("请输入新的学生年龄: ")

    stuInfos[stuId - 1]['stuName'] = newName
    stuInfos[stuId - 1]['stuSex'] = newSex
    stuInfos[stuId - 1]['stuAge'] = newAge


# 显示所有学生的信息
def showAllStuInfo():
    print("****** 所有学生信息如下 *******")
    print("序号     姓名        性别     年龄 ")
    i = 1
    for tempInfo in stuInfos:
        print("%d     %s        %s     %s" %(i,tempInfo['stuName'],tempInfo['stuSex'],tempInfo['stuAge']))
        i += 1




# 主函数
def main():
    while True:
        printMenu()
        key = input("请您选择对应的功能数字：")

        if key == "1":
            addStuInfo()
        elif key == "2":
            delteStuInfo(stuInfos)
        elif key == "3":
            mofifyStuInfo()
        elif key == "4":
            showAllStuInfo()
        elif key == "0":
            quitConfirm = input("亲， 你真的要退出系统吗？？？ (Yes or No):")
            if quitConfirm == "Yes":
                break # 退出系统
            else:
                print("输入有误, 请重新输入！")


# 调用 main() 函数
main()