print("=====================列表推导式==========")
"""
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
或者 
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
"""

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

print("=====================字典推导式==========")
"""
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {value: len(value) for value in listdemo}
print(newdict)

print("=====================集合推导式==========")
"""
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
setnew = {i**2 for i in (1,2,3)}
print(setnew)

print("=====================元组推导式（生成器表达式）==========")
"""
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""
a = (x for x in range(1,10))
print(a)
# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a))