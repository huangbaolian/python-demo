import pymysql
db = pymysql.connect(
    host='localhost',  # 数据库主机地址
    user='root',  # 数据库用户名
    passwd='12345678',
    database='demo')  # 从环境变量中读取数据库密码
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
