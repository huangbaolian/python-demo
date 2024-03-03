import math
# print("she said 'hello'")
print('she said:\n "hello"')
print("""ni shuosha
sjiu shid
sssd 
""")
"""
一个多行注释
"""
num: int = 1234
print("我有"+str(num)+"元\n")

result = math.sin(num)
print("最后结果为:"+str(result)+"\n")
result = 2**3
print("2的3次方为:"+str(result)+"\n")

input_result = int(input("输入一个数字呢:"))

print("输入的是:"+str(input_result)+",给这个数加1后为:"+str(input_result+1))

if input_result <= 5:
    print("是小于等于5")
    if input_result == 4:
        print("为4")
    else:
        print("不为4")
else:
    print("大于5了")

def func_add(a,b):
    return a+b

result = func_add(1,2)

print("计算加法结果为:"+str(result))
