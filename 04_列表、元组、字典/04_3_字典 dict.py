"""
字典  dict
    key - values
    可以 增删改查

"""

"""
根据键访问值
"""
print("---------")
info = {'name':'班长', 'id':100, 'sex':'男', 'address':'上海'}
print("职位: ", info['name'])
print("职位：", info.get('name'))

# 如果没有对应的key
age = info.get('age')
print(age)
print(type(age))

age = info.get('age', 22)
print(age)

"""
修改dict的值
"""
print("---------")
newId = input('请输入新的id： ')
info['id'] = newId
print("修改后的新的id为： ", info['id'])


"""
添加元素
    使用 dict变量['key'] = value 时，自动加入到dect
"""
print("---------")
info['age'] = 27
print(info)

"""
删除元素
    del    删除字典中某一项
    clear  清空数据，整个字典为空
"""
print("---------")
print("删除前： ", info)
del info['age']
print("删除后： ", info)

print("清空前： ", info)
info.clear()
print("清空后： ", info)

"""
计算键值对的个数
"""
print("---------")
info = {'name':'班长', 'id':100, 'sex':'男', 'address':'上海'}
print(info)
print("键值对的个数： ", len(info))

"""
获取字典的key键 视图
"""
print("---------")
print("keys: ", info.keys())

"""
获取字典的value值 视图
"""
print("---------")
print("values: ", info.values())


"""
获取字典的 key-value 视图
"""
print("---------")
print("key - value: ", info.items())


"""
字典的遍历
"""
print("=========")
dict = {'name':'iLaoda', 'age':18}
# 遍历key
for key in dict.keys():
    print("keys: %s" %key)

# 遍历value
for value in dict.values():
    print("value: %s" %value)

# 遍历元素
# 不能用字符串，因为item是dict类型
for item in dict.items():
    print(item)


# 遍历key-value
for key, value in dict.items():
    print("key: %s, value: %s" %(key, value))


