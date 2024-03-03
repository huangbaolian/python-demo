###基础语法
print("=====================注释==========")
# 一行注释
# 注释一行
"""
这是多行注释哦
"""
'''
这也是多行注释呢,哈哈
'''
print("hello word!")

print("=====================缩进==========")
value: bool = False
if value:
    print("这是为true")
else:
    print("这不为true")
print("这和上面多判断流程没关系")

print("=====================多行语句==========")
num1: int = 1
num2: int = 2
num3: int = 3
total: int = num1 + \
             num2 + \
             num3
print("总量为:", total)

print("=====================数字(Number)类型==========")
inta: int = 2
boolb: bool = True
floatc: float = 0.2
complexd: complex = 1 + 2j
print("int (整数):", inta)
print("bool (布尔):", boolb)
print("float (浮点数):", floatc)
print("complex (复数):", complexd)

print("=====================字符串(String)==========")
word = '字符串'
sentence = "--这是一个句子。"
paragraph = """---这是一个段落，
---可以由多行组成,啦啦"""
print(word)
print(sentence)
print(paragraph)
str = '123456789'
print("输出字符串:", str)
print("输出第一个到倒数第二个的所有字符:", str[0:-1])
print("输出字符串第一个字符:", str[0])
print("输出从第三个开始到第六个的字符（不包含）:", str[2:5])
print("输出从第三个开始后的所有字符:", str[2:])
print("输出从第二个开始到第五个且每隔一个的字符（步长为2):", str[1:5:2])
print("输出字符串两次:", str * 2)
print("连接字符串:", str + '你好')
print('hello\nrunoob')
print(r'hello\nrunoob')  # 加了r后不进行转义

print("=====================等待用户输入==========")
inputStr = input("\n\n按下 enter 键后退出。")
print("输入的内容是:", inputStr)

print("=====================import 与 from...import==========")
#在 python 用 import 或者 from...import 来导入相应的模块。
import sys
print ('python 路径为',sys.path)