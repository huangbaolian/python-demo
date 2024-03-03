class CuteCat:
    def __init__(self, cat_name, age):
        self.name = cat_name
        self.age = age
        self.tool = {"猫猫棒","玩具鱼","猫抓板"}
    def miao(self):
        if self.age < 4:
            print("喵喵小于4岁")
        else:
            print("喵喵大于等于4岁")
        return
    def favoriate(self,tool):
        if tool in self.tool:
            return "猫猫最喜欢的玩具在里面"
        else:
            return "猫猫最喜欢的玩具不在里面"

cat1 = CuteCat("aa", 12)

print("cat1 name: %s, age: %d" %(cat1.name, cat1.age))

cat1.miao()

print("猫猫有这些玩具:{}".format(cat1.tool))
favorite_tool = "猫抓板"
print("猫猫最喜欢的玩具是:"+favorite_tool, cat1.favoriate(favorite_tool))

print("=====================继承==========")

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()

print("=====================多继承==========")
#另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))


# 多继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法
print("=====================方法重写==========")
"""
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。"""
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    __a: int=1
    def myMethod(self):
        print('调用子类方法')
        print(self.__a)

    def __method(self):
        print(self.__a)


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法