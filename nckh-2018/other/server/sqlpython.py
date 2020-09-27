import pymysql
from ham import *
class sqlpython():
    def connect(self):
        cconnect = pymysql.connect(host='localhost',
                     user='root',
                     password='duysydeptrai',
                     db='hethong',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
        print("connect successful!!")
        return cconnect

    def RFID(self,rfid,phong):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                sql = "Insert into diemdanh(idrfid,time,thu,ngay,gio,phong) " + " values (%s,%s,%s,%s,%s,%s)"
                print(rfid+"  "+getdatetime()+" "+getthu()+" "+getngay()+" "+getgio()+" "+phong)
                cursor.execute(sql,(rfid, getdatetime(),getthu(),getngay(),getgio(),phong))
                connection.commit()
        except:
            print("Loi")
        finally:
            connection.close()
    def cautruyvan(self,cautruyvan):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                cursor.execute(cautruyvan)
                for i in cursor:
                    return i
        except:
            print("Loi")
        finally:
            connect.close()

    def truyvandanhsach(self, cautruyvan):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                cursor.execute(cautruyvan)
                return cursor
        except:
            print("Loi")
        finally:
            connect.close()

    def lichHoc(self,ID,phong):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                sql = "select * from diemdanh where ID='"+ID+"'"
                cursor.execute(sql)

                print(ID + "  " + getdatetime())
                connect.commit()
        except:
            print("Loi")
        finally:
            connect.close()
    def themThongBao(self, idgiaovien, toi,thongbao, nguoithongbao,):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                sql = "Insert into thongbao(idgiaovien,thongbao,toi,nguoithongbao,datetime,date) " + " values (%s, %s ,%s ,%s,%s,%s)"
                cursor.execute(sql,(idgiaovien,thongbao,toi,nguoithongbao,getdatetime(),getngay()))
                connect.commit()
        except:
            print("Loi")
        finally:
            connect.close()
    # VD xxxxxxxxx 18it5
    def themSV(self,idfacebook,idsinhvien):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                sql = "Update sinhvien set idfacebook = '"+idfacebook+"' where idsinhvien = '"+idsinhvien+"' "
                cursor.execute(sql)
                print(idfacebook + "  " + idsinhvien)
                connect.commit()
        except:
            print("Loi")
        finally:
            connect.close()
    def themGV(self,idfacebook,idgiangvien):
        try:
            connect = self.connect()
            with connect.cursor() as cursor:
                sql = "Update giangvien set idfacebook = '"+idfacebook+"' where idgiangvien = '"+idgiangvien+"' "
                cursor.execute(sql)
                print(idfacebook + "  " + idgiangvien)
                connect.commit()
        except:
            print("Loi")
        finally:
            connect.close()


