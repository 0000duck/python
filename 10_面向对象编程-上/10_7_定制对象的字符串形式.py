"""
    可以将对象转换为自定义的字符串形式
    即打印的是对象，最终是打印的是字符串

    __str__  只有str 和 print 函数调用才能转换
    __rept__   str、print、srt 函数都可以获得实例对象自定义的字符串形式
"""

# 只重载 __srt__ 方法
class Demo:
    data1 = 100

    def set(self, num):
        self.data2 = num

    def __str__(self):
        # 返回自定义的字符串
        return "data1 = %s, data2 = %s" %(self.data1, self.data2)

demo = Demo()
demo.set(200)

print("print: ", demo)
print("str: ", str(demo))
print("repr: ", repr(demo))  # repr:  <__main__.Demo object at 0x000000000285ACC0>



# 只重载 __repr__ 方法
print("="*40)
class Demo1:

    data1  =  400
    def set(self, num):
        self.data2 = num

    # 重载
    def __repr__(self):
        # 返回自定义的字符串形式
        return "data1 = %s, data2 = %s" % (self.data1, self.data2)

demo1 = Demo1()
demo1.set(800)

print("print: ", demo1)
print("str: ", str(demo1))
print("repr: ", repr(demo1))



# 只重载 __srt__ 和 __repr__ 方法
print("="*40)
class Demo2:
    data1 = 300

    def set(self, num):
        self.data2 = num

    # 重载方法
    def __repr__(self):
        return "repr 转换： data1 = %s, data2 = %s" % (self.data1, self.data2)

    def __str__(self):
        return "srt转换： data1 = %s, data2 = %s" % (self.data1, self.data2)

demo2 = Demo2()
demo2.set("abc")

print("print: ", demo2)
print("str: ", str(demo2))
print("repr: ", repr(demo2))

