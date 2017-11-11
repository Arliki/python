from myfunction import ComRe
#调用测试
# while 1:
#     a=input("input num:\n")
#     b=ComRe.input_type(a)
#     print(b)
import pymysql
#pymysql.install_as_MySQLdb()
def py_mysql_get_version():
    db = pymysql.connect("localhost","root","root","brow")
    cursor = db.cursor()
    sql="select * from admin"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data[0][1])
    # for i in data:
    #     print(i)

    db.close()
py_mysql_get_version()
