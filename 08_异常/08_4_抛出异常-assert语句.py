"""
assert语句

    当用户定义的约束条件不满足的时候，就会出发 AssertionError 异常
    assert 是用来手机用户定义的约束条件，而不是捕获内在的程序错误

    格式： assert 逻辑表达式, data(可选)

    以上格式等同于：
    if not 逻辑表达式：
        raise AssertionError(data)

"""

#
a = 0
assert a != 0, "a的值不能为0"