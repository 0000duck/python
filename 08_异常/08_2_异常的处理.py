"""
异常的处理
    try:   except 具体异常：

    可以多个except 语句来捕获异常

    可以使用一个 except 语句后来捕获多个异常：
        python2    异常1, 异常2:
        python3   (异常1, 异常2):  元组来表示了

    相对完整的异常处理语句：


    try:
        语句块
    except A:
        异常A处理代码
    except:
        其他异常的处理代码
        如果有多个 except, 空的 except 必须位于所有 except 之后
    else:
        没有异常的代码（就想在 except 和 finally 之间运行）
        有else 必须有 except
    finally:
        必须执行的代码

"""

"""
捕获简单的异常
"""
print("="*20)
try:
    num1 = input("请输入第一个数：")
    num2 = input("请输入第二个数：")
    print("两数相除：", int(num1) / int(num2))
except ZeroDivisionError: # 具体的异常
    print("第二个数不能为 0")


"""
捕获多个异常
"""
print("="*20)
try:
    num1 = input("请输入第一个数：")
    num2 = input("请输入第二个数：")
    print("两数相除：", int(num1) / int(num2))
except ZeroDivisionError: # 具体的异常
    print("第二个数不能为 0")
except ValueError:
    print("输入的是非数字")



"""
捕获异常的描述信息
    except 后跟具体异常
    except 后面什么也不跟，捕获所有异常  （和下面同时存在，必须位于最后）
    except 后面跟 Except, 捕获所有异常
"""
print("="*20)
try:
    num1 = input("请输入第一个数：")
    num2 = input("请输入第二个数：")
    print("两数相除：", int(num1) / int(num2))
except (ZeroDivisionError, ValueError) as result:
    print("捕获到的异常信息为: %s" %result)

"""
捕获所有异常
    except :
    或者
    except Exception:
"""


"""
终止行为：
    finally: 无论发生异常，都会去执行
    通常用来释放资源，例如关闭文件，释放锁等
"""
print("="*20)
import time
try:
    f = open("test.txt", "r+")
    while True:
        content = f.read()
        if len(content) == 0:
            break

        time.sleep(2)
        print(content)
finally:
    f.close()
    print("文件被关闭了")



