print("=====================函数调用==========")


def hello():
    print("Hello World!")


hello()

print("=====================参数传递==========")
a = [1, 2, 3]

a = "Runoob"
print(a)
"""
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
"""

print("=====================python 传不可变对象实例==========")


def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)

print("=====================传可变对象实例==========")


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

print("=====================必需参数==========")


def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
printme(str="3")

print("=====================默认参数==========")
# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

print("=====================不定长参数==========")


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

#字典的方式
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)

print("=====================匿名函数==========")
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))