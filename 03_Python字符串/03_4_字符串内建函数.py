"""
find()
查找给定的字符串是否包含在此字符串中

查到返回第一个字符的索引，否则返回 -1
"""
mystr = "hello world itheima and itheimaAPP"
index1 = mystr.find("itheima")
print(index1)


"""
index()
查找给定的字符串是否包含在此字符串中
查到返回第一个字符的索引，否则抛出异常
"""
index2 = mystr.index("itheima", 0, 20)
print(index2)


"""
count()
用于统计字符串中某个字符出现的次数
"""
result = mystr.count("m", 0, 20)
print("出现的次数：%s"%result)


"""
replace()
字符串替换
返回值为替换后的新字符串
"""
newStr = mystr.replace("itheima", "ITHEIMA", 1)
print("替换后的字符串为： %s"%newStr)



"""
split()
用指定的字符串去分割
返回的数据结构中，不包含分割的字符
"""
str = "this is string example ....wow!!!"
print("分割字符", str.split())
print("分割字符", str.split("i", 1))
print("分割字符", str.split("is"))



"""
capitalize() 大写字母
将首字母变为大写，其他字母变为小写。
返回新字符串
"""
newStrCap = mystr.capitalize()
print("首字母大写：%s"%newStrCap)


"""
title()  将所有单词首字母变为大写
"""
newSrtAllCap = mystr.title()
print("所有单词首字母变为大写：%s" %newSrtAllCap)



"""
upper() 将所有的小写字母转换为大写字母
"""
strUpper = mystr.upper()
print("全部转换为大写字母：%s" %strUpper)


"""
startwith() 检查是否以指定字符串开始, 区分大小写
是： 返回True
否： 返回False
"""
strStartWith = mystr.startswith("hello")
print("是否以指定字符串开始: ", strStartWith)


"""
endWith()
"""
strEndWith1 = mystr.endswith("APP")
strEndWith2 = mystr.endswith("App")
print("是否以指定字符串结尾: ", strEndWith1)
print("是否以指定字符串结尾: ", strEndWith2)


"""
ljust()
原字符串左对齐

返回一个字符串，如果给定的长度没有原字符串长，返回原字符串。
如果超过原字符串，用给定的字符串弥补到给定的长度，不给定字符串的话，默认用空格补齐
"""
str2 = "Runoob example....wow!!!"
print("ljust: ", str2.ljust(50))


"""
rjust()
原字符串右对齐
"""
print("fjust: ", str2.rjust(50, '*'))



"""
center()
返回给定数字长度，在原字符串中的长度的字符串，可以补齐
不够原字符串的长度的话，返回原字符串
"""
srtCenter = mystr.center(50, '*')
print("给定长度中间的字符串： %s"%srtCenter )

"""
lstrip()
截取掉字符串左边的空格或者指定字符串
"""
mystr1 = "      hello word   itheima****     1   "
srtLstrip = mystr1.lstrip()
print("lstrip: %s" %srtLstrip)


"""
rstrip()
截取掉字符串左边的空格或者指定字符串
"""
srtRstrip = mystr1.rstrip()
print("rstrip: %s" %srtRstrip)


"""
strip()
以除掉字符串头尾指定的字符
"""
strip = mystr1.strip()
print("strip: %s" %strip)
