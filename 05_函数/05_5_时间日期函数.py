"""
时间函数
    时间戳
        time()
        clock()
    格式化时间字符串
    时间元组
"""

import time
import calendar

# 时间戳
ticks = time.time()
print("当前的时间戳为: ", ticks)


# 格式化时间字符串
# 格式化为 2018-08-08 11：11：11
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化为 Sat Mar 28 11:11:11 2018
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 格式化时间字符串为 时间戳
a = "Sun Mar 11 13:13:57 2018"
a1 = "2018-03-11 13:16:27"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
print(time.mktime(time.strptime(a1, "%Y-%m-%d %H:%M:%S")))



# 日历函数
cal = calendar.month(2018, 8)
print("2018年1月份的日历如下：")
print(cal)