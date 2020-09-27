import datetime
import time
from django.db import connection
def getthu():
    ngay = time.localtime().tm_wday
    if (ngay ==0):
        return "THỨ HAI"
    if (ngay == 1):
        return "THỨ BA"
    if (ngay == 2):
        return "THỨ TƯ"
    if (ngay == 3):
        return "THỨ NĂM"
    if (ngay == 4):
        return "THỨ SÁU"
    if (ngay == 5):
        return "THỨ BẢY"
    if (ngay == 6):
        return "CHỦ NHẬT"
def getngay():
    return str(datetime.datetime.now().strftime('%Y-%m-%d'))
def getgio():
    return str(datetime.datetime.now().strftime('%H:%M:%S'))
def getdatetime():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
################################SQL###################################################################################
#--------lấy danh sách sinh viên có điểm danh thôi
def get_dssvdiemdanh(user):
    sql="SELECT sv.id,sv.fgid,sv.id_sinh_vien,sv.ten,sv.sdt,sv.email,sv.lop,dd.thu,dd.ngay,dd.gio,dd.time,dd.phong,dd.id " \
        "FROM main_diem_danh as dd ,main_sinh_vien as sv where dd.fgid =sv.fgid and dd.user='{}' and sv.user='{}' ".format(user,user)
    return sql
#------------lấy danh sách sinh viên có mặt trong lop,môn,ngày hôm đó
def get_dssvdihoc(user,lop,mon,idgiangvien):
    sql="select distinct sv1.id,sv1.id_sinh_vien,sv1.ten,sv1.lop,sv1.sdt,sv1.email,sv1.phong,lh.ten,sv1.ngay,sv1.gio from ({}) as sv1,main_lich_hoc as lh " \
        "where sv1.lop = '{}' and lh.lop ='{}' and sv1.thu='{}' and (sv1.gio between lh.bat_dau and lh.ket_thuc) " \
        "and lh.ten_mon_hoc ='{}' and lh.phong=sv1.phong  and lh.id_giang_vien='{}' and lh.user='{}'".format(get_dssvdiemdanh(user),lop,lop,getthu(),mon,idgiangvien,user)
    return sql
#-----------------Lay so luong sinh vien di hoc
def get_slsinhvienmon(user,mon):
    sql = "select count(distinct sv1.id) from ({}) as sv1,main_lich_hoc as lh " \
          "where (sv1.gio between lh.bat_dau and lh.ket_thuc) " \
          "and lh.ten_mon_hoc ='{}' and lh.user='{}' and sv1.ngay='{}' and sv1.thu=lh.thu and sv1.lop=lh.lop".format(get_dssvdiemdanh(user), mon,user,getngay())
    return sql
#-----------------Lay so tòn bộ luong sinh vien di hoc
def get_slsinhvienmonall(user,mon):
    sql = "select count(distinct sv1.id) from main_sinh_vien as sv1,main_lich_hoc as lh " \
          "where lh.ten_mon_hoc ='{}' and lh.user='{}' and sv1.lop=lh.lop and lh.thu='{}'".format( mon,user,getthu())
    return sql
def truy_van(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    ketqua=[]
    print(cursor)
    for i in cursor:
        ketqua.append(i)
    return ketqua


