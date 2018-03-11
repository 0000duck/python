# '' "" 注释

### 字符串 ###
print('字符串========================')
print('I\'m learning\nPython.')
print("Hi, \\ I'm learning Python.")

# 表示里面的不转义 r''
print(r'默认不转义: \ \n \t')

# 多行内容 ''''''
print('''我
爱你
中国''')

print(r'''\\我
爱你
中国\n\n''')


### 布尔类型 ###
print('\n布尔========================')

# True Flse
print(True)
print(False)
print(7<45)

# and or not 运算符
print(True and False)
print(False or True)
print(not 2>1)

# None 运算符, None不能理解为0，因为0是有意义的
print(None)


### 变量 ###
print('\n变量==========================')

# 同一个变量可以反复赋值，而且可以是不同类型
# 这种类型不固定的成为【动态语言】
a = 123
print(a)
a = "python"
print(a)


### 常量 ###
print('\n常量==========================')

# 精确除法, 结果浮点型
print(10/3)
print(9/3)

# 板除，两个整数的除法仍然是整数 //
print(10//3)
print(9//3)

# 余数运算
print(13%3)




















