"""
变量的数据类型：
    * 数字类型
        * int 整形
            - 十进制
            - 二进制： 0b 或者 0B 开头
            - 八进制： 0 开头
            - 十六进制： 0X 或者 Ox 开头
        * float 浮点型 （每个浮点占8个字节）
        * complex 复数
    * bool 类型 True Flase
    * string 字符串类型
    * list 列表类型 []
    * tuple 元组类型，不能改变 ()
    * dictionary 字典类型 {}
"""

''' 进制的转换 '''
bin(20) # 十进制转换为二进制
oct(20) # 十进制转换为八进制
hex(20) # 十进制转换为十六进制


''' 复数 
实数部分 + 虚数部分  (都是浮点型)
5 + 3j
-3.4 - 6.8j
'''

''' 数字类型之间的转换 '''
# 转换为int
a = 1.2
a1 = int(a)
print(a1)

# 转换为 float
b = 3
b1 = float(3)
print(b1)

# 创建复数
c = complex(3.4)
print(c)  #(3.4+0j)
