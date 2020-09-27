import datetime
import time
# Lay tu trong cau
def catkytu(chuoi,m):
        return str(chuoi.split(" ")[m])
# lay duoi cua cau trong cau
def chuoiduoi(chuoi,m):
        return str(" ".join(chuoi.split()[m:len(chuoi.split())]))
# lay thoi gian hien tai
def getdatetime():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#lay gio hom nay
def getgio():
    return str(datetime.datetime.now().strftime('%H:%M:%S'))
#lay ngay hom nay
def getthu():
    ngay = time.localtime().tm_wday
    if (ngay ==0):
        return "THU HAI"
    if (ngay == 1):
        return "THU BA"
    if (ngay == 2):
        return "THU TU"
    if (ngay == 3):
        return "THU NAM"
    if (ngay == 4):
        return "THU SAU"
    if (ngay == 5):
        return "THU BAY"
    if (ngay == 6):
        return "CHU NHAT"
def getngay():
    return str(datetime.datetime.now().strftime('%Y-%m-%d'))
def docfile(n):
    f = open('taikhoan', 'r')
    for i in range(0,n):
        f.readline()
    return f.readline()





