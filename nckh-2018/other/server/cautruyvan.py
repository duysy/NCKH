from ham import *
from sqlpython import *
#lay idgiangvien tu idfacebook cua giang vien
def getidgiangvien(idfacebook):
    return "SELECT idgiangvien FROM giangvien where idfacebook='"+idfacebook+"'"

#lay idsuinhvien tu idfacebook cua sinh vien
def getidsinhvien(idfacebook):
    return "SELECT idsinhvien FROM sinhvien where idfacebook='"+idfacebook+"'"

def getgiohocbatdau(time,idgiangvien,thu,phong):
    return "SELECT batdau FROM lichhoc where '"+time+"' > batdau and '"+time+"' < ketthuc and idgiangvien='"+idgiangvien+"' and phong ='"+phong+"' and thu ='"+thu+"'"

def getgiohocketthuc(time,idgiangvien,thu,phong):
    return "SELECT ketthuc FROM lichhoc where '"+time+"' > batdau and '"+time+"' < ketthuc and idgiangvien='"+idgiangvien+"' and phong ='"+phong+"' and thu ='"+thu+"'"

def getlop_time(time,idgiangvien,thu):
    return "SELECT lop FROM lichhoc where '"+time+"' > batdau and '"+time+"' < ketthuc and idgiangvien = '"+idgiangvien+"' and thu ='"+thu+"'"
def getphong_time(time,idgiangvien,thu):
    return "SELECT phong FROM lichhoc where '"+time+"' > batdau and '"+time+"' < ketthuc and idgiangvien = '"+idgiangvien+"' and thu ='"+thu+"'"
def getidmonhoc_time(time,idgiangvien,phong,thu):
    return "SELECT idmonhoc FROM lichhoc where '"+time+"' > batdau and '"+time+"' < ketthuc and idgiangvien = '"\
           +idgiangvien+"' and phong = '"+phong+"' and thu ='"+thu+"'"
def getidsinhvien_lop(lop):
    return "SELECT idsinhvien FROM sinhvien where lop = '"+lop+"'"
def getdanhsachdihoc(lop,ngay,phong,batdau,ketthuc):
    return "SELECT  DISTINCT sinhvien.tensv, diemdanh.idrfid FROM diemdanh,sinhvien where sinhvien.idrfid = diemdanh.idrfid  and diemdanh.gio >='"+batdau+"' and diemdanh.gio <= '"+ketthuc+"' and " \
    "sinhvien.lop='"+lop+"' and diemdanh.ngay='"+ngay+"' and diemdanh.phong ='"+phong+"'"
def getsoluongdihoc(lop,ngay,phong,batdau,ketthuc):
    return "SELECT COUNT(DISTINCT diemdanh.idrfid) AS soluong FROM diemdanh,sinhvien where sinhvien.idrfid = diemdanh.idrfid  and diemdanh.gio >='"+batdau+"' and diemdanh.gio <= '"+ketthuc+"' and " \
    "sinhvien.lop='"+lop+"' and diemdanh.ngay='"+ngay+"' and diemdanh.phong ='"+phong+"'"
def getnguoithongbao(idfacebook):
    return "SELECT ten FROM giangvien where idfacebook='" + idfacebook + "'"
def lagiangvien(idfacebook):
    return "SELECT idgiangvien FROM giangvien where idfacebook='"+idfacebook+"'"
def laythongbao(idfacebook):
    return "SELECT datetime,nguoithongbao,thongbao FROM sinhvien,thongbao where sinhvien.lop = thongbao.toi and sinhvien.idfacebook='"+idfacebook+"' and thongbao.date ='"+getngay()+"'"

# ------------------------------------------------------------------------------------------------------#

def getsoluongdihoc_return(idfacebook):
    try:
        sql = sqlpython()
        idgiangvien = sql.cautruyvan(getidgiangvien(idfacebook))["idgiangvien"]
        phong = sql.cautruyvan(getphong_time(getgio(), idgiangvien, getthu()))["phong"]
        lop = sql.cautruyvan(getlop_time(getgio(), idgiangvien, getthu()))["lop"]
        batdau = str(sql.cautruyvan(getgiohocbatdau(getgio(), idgiangvien, getthu(), phong))["batdau"])
        ketthuc = str(sql.cautruyvan(getgiohocketthuc(getgio(), idgiangvien, getthu(), phong))["ketthuc"])

        return str(sql.cautruyvan(getsoluongdihoc(lop, getngay(), phong, batdau, ketthuc))["soluong"])
    except:
        return "Co the lay nham gio"
def getidgiangvien_return(idfacebook):
    try:
        sql = sqlpython()
        return str(sql.cautruyvan(getidgiangvien(idfacebook))["idgiangvien"])
    except:
        return "Co the lay nham gio"

def getnguoithongbao_return(idfacebook):
    try:
        sql = sqlpython()
        return str(sql.cautruyvan(getnguoithongbao(idfacebook))["ten"])
    except:
        return "Co the lay nham gio"
def lagiangvien(idfacebook):
    try:
        sql = sqlpython()
        if(str(sql.cautruyvan(getidgiangvien(idfacebook))["idgiangvien"])=="0"):
            return False
        else:
            return True
    except:
        return "co gi day sai sai"
def laythongbao_return(idfacebook):
    try:
        sql = sqlpython()
        dic_thongbao=sql.truyvandanhsach(laythongbao(idfacebook))
        message="\n"
        for i in dic_thongbao:
            message = message+ str(i["datetime"]) + "\nNguoi gui: " + str(i["nguoithongbao"]) + "\nThong bao:" + str(i["thongbao"]) +"\n \n"
    except:
        return "Khong co thong bao "
    finally:
        return message
def getdanhsachdihoc_return(idfacebook):
    try:
        sql = sqlpython()
        idgiangvien = sql.cautruyvan(getidgiangvien(idfacebook))["idgiangvien"]
        phong = sql.cautruyvan(getphong_time(getgio(), idgiangvien, getthu()))["phong"]
        lop = sql.cautruyvan(getlop_time(getgio(), idgiangvien, getthu()))["lop"]
        batdau = str(sql.cautruyvan(getgiohocbatdau(getgio(), idgiangvien, getthu(), phong))["batdau"])
        ketthuc = str(sql.cautruyvan(getgiohocketthuc(getgio(), idgiangvien, getthu(), phong))["ketthuc"])
        message =""
        dic_danhsach =sql.truyvandanhsach(getdanhsachdihoc(lop, getngay(), phong, batdau, ketthuc))
        for i in dic_danhsach:
            message = message + str(i["tensv"] +"\n")

    except:
        return "Co the lay nham gio"
    finally:
        return message


