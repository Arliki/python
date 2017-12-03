from myfunction import ComRe
#调用测试
#while 1:
    # a=input("input num:\n")
    # b=ComRe.input_type(a)
a=(1,2,3,4,5,6,7)
b=[3,4,5]
c=ComRe.to_dict(a,b,7)
print(c)
#参数顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *ds, d,**kw):
    print('a =', a, 'b =', b, 'c =', c,'ds=',ds, 'd =', d, 'kw =', kw)

argsa = (1, 2, 3, 4,5,6)
kws = {'d': 99, 'x': '#'}
f2(*argsa, **kws)
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
#py_mysql_get_version()
