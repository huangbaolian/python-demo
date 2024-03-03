
try:
    x = int(input("请输入一个数字: "))

except ValueError:
    print("您输入的不是数字，请再次尝试输入！")
else:
    print("您输入的是:",x)
finally:
    print("结束")

print("=====================用户自定义异常==========")


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)