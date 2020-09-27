import pymysql.cursors
from ham import *
# Kết nối vào database.
connection = pymysql.connect(host='localhost',
                     user='root',
                     password='duysydeptrai',
                     db='hethong',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:
    with connection.cursor() as cursor:
        sql = "Insert into thongbao(idgiaovien,thongbao,toi,nguoithongbao,datetime) " + " values (%s, %s ,%s ,%s,%s)"
        cursor.execute(sql, ("đâsdjklja", "dlaskdas", "kajdla", "dkasjdla", getdatetime()))
        connection.commit()
except:
    print("Loi")
finally:
    connection.close()
