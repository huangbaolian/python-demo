import re
"""Python 中的 with 语句用于异常处理，封装了 try…except…finally 编码范式，提高了易用性。

with 语句使代码更清晰、更具可读性， 它简化了文件流等公共资源的管理。"""

def open_file():
    with open("../../../source/poem.txt", "w", encoding="UTF-8") as f:
        f.write("只是一行测试\n")
        f.write("只是一行测试\n")
        f.write("只是一行测试\n")
        f.write("只是一行测试\n")

    with open("../../../source/poem.txt", "a", encoding="UTF-8") as f:
        f.write("只是一行测试aa\n")
        f.write("只是一行测试aa\n")

    try:
        with open("../../../source/poem.txt", "r", encoding="UTF-8") as source, open("../../../source/tarpoem.txt", "w",
                                                                                     encoding="UTF-8") as target:
            for line in source:
                if "aa" in line:
                    print(line)
                    a = 0 / 0
                    line = line.replace("aa", "bb")
                target.write(line)
    except IOError as e:
        print("出IO错了:" + str(e))
    except ArithmeticError as e:
        print("出数学错了:" + str(e))
    finally:
        source.close()
        target.close()
