###基础数据类型
import math

print("=====================单个变量赋值==========")
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "test"  # 字符串
print(counter)
print(miles)
print(name)

print("=====================多个变量赋值==========")
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, "aa"
print(a, b, c)

print("=====================Number（数字)==========")
a, b, c, d = 20, 5.5, True, 4 + 3j
"""
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
# Python3 中，bool 是 int 的子类,True 和 False 可以和数字相加， True==1、False==0 会返回 True
print(isinstance(c, int))
print(issubclass(bool, int))
a, b = 1, 0
if a is True:
    print("a is true")
if b is False:
    print("b is False")
if True == 1:
    print("1==true")
if False == 0:
    print("0==False")
print("除法，得到一个浮点数:", 2 / 4)
print("除法，得到一个整数:", 2 // 4)
print("取余:", 17 % 3)
print("乘方:", 2 ** 5)

number=2.334
print("绝对值:",abs(number))
print("浮点绝对值:",math.fabs(number))
print("向下取整:",math.floor(number))
print("向上取整",math.ceil(number))
print("取最大值:",max(a,b))
print("取最小值:",min(a,b))


print("=====================String（字符串）==========")
word = 'Python'
print(word[0], word[5])
print(word[-2], word[-6])
str = "hello"
print("首字母大写:",str.capitalize())
"""
在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，
只有 0、空字符串、空列表、空元组等被视为 False
"""

print("=====================List（列表）==========")
testList = ['abcd', 786, 2.23, 'runoob', 70.2]
tinyList = [123, 'runoob']
print(testList)  # 输出完整列表
print(testList[0])  # 输出列表第一个元素
print(testList[-1])  # 输出列表最后一个元素
print(testList[1:3])  # 从第二个开始输出到第三个元素
print(testList[2:])  # 输出从第三个元素开始的所有元素
print(tinyList * 2)  # 输出两次列表
print(testList + tinyList)  # 连接列表
print("从下标为1的开始到下标为4截取步长为2:", testList[1:4:2])
print("反转顺序:", testList[-1::-1])

print("=====================Tuple（元组）==========")
# 修改元组元素的操作是非法的
testTuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinyTuple = (123, 'runoob')
print(testTuple)  # 输出完整元组
print(testTuple[0])  # 输出元组的第一个元素
print(testTuple[1:3])  # 输出从第二个元素开始到第三个元素
print(testTuple[2:])  # 输出从第三个元素开始的所有元素
print(tinyTuple * 2)  # 输出两次元组
print(testTuple + tinyTuple)  # 连接元组

print("=====================Set（集合）==========")
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
print("=====================Dictionary（字典）==========")
dicts = {}
dicts['one'] = "1 - 菜鸟教程"
dicts[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dicts['one'])  # 输出键为 'one' 的值
print(dicts[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print("=====================bytes 类型==========")
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")