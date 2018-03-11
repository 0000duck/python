"""
文件的读写
    r   w   a     只 读，写，追加
    rb  wb  ab    只 读，写，追加（二进制）

    r+  w+  a+    读，写，追加
    rb+ wb+ ab+   读，写，追加（二进制）

    open()
    close()


"""
# 在当前文件夹下生成 test.txt
f = open("test.txt", "w+")


# 关闭
f = open("itheima.txt", "w")
f.close()
