from fbchat import Client
from fbchat.models import *
from sqlpython import *
from cautruyvan import *
from ham import *


thread_type = ThreadType.USER

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if author_id != self.uid and thread_type != thread_type.GROUP:
            print(thread_id)
            self.lenhDung(message_object.text,thread_id)


    def sendMessage(self, message,thread_id):
        self.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)

    def lenhDung(self,message,thread_id):
        if (catkytu(message, 0).upper() == "THEMTHONGBAO"):
            if (lagiangvien(thread_id) == True):
                print("dang them thong bao")
                sql = sqlpython()
                sql.themThongBao(getidgiangvien_return(thread_id), catkytu(message, 1).upper(),
                                 chuoiduoi(message, 2),
                                 getnguoithongbao_return(thread_id))
                self.sendMessage("Thong bao da duoc day len", thread_id)
                # Themthongbao chung ngaymai đi chơi

        if (catkytu(message, 0).upper() == "DANGKY"):
            sql = sqlpython()
            if (catkytu(message, 1).upper() == "GIANGVIEN"):
                sql.themGV(thread_id, catkytu(message, 2).upper())
                print("dang ky thanh cong  " + thread_id + " " + catkytu(message, 1).upper())
                self.sendMessage("Ban da dang ky thanh cong", thread_id)
            if (catkytu(message, 1).upper() == "SINHVIEN"):
                sql.themSV(thread_id, catkytu(message, 2).upper())
                print("dang ky thanh cong  " + thread_id + " " + catkytu(message, 1).upper())
                self.sendMessage("Ban da dang ky thanh cong", thread_id)


        if (catkytu(message, 0).upper() == "DIEMDANH"):
            print("diem danh")
            if (catkytu(message, 1).upper() == "SOLUONG"):
                print(type(thread_id))
                message = "Số lượng sinh viên có trong lơp là :" + getsoluongdihoc_return(str(thread_id))
                self.sendMessage(message, thread_id)
            if (catkytu(message, 1).upper() == "DANHSACH"):
                print(type(thread_id))
                message = "Danh sach sinh viên có trong lơp là  :\n" + getdanhsachdihoc_return(str(thread_id))
                self.sendMessage(message, thread_id)


        if (catkytu(message, 0).upper() == "THONGBAO"):
            print("thong bao")
            print(type(thread_id))
            self.sendMessage(laythongbao_return(thread_id), thread_id)
            print(laythongbao_return(thread_id), thread_id)
        if(catkytu(message, 0).upper() == "HUONGDAN"):
            print("huong dan");
            print(thread_id)
            huongdan=\
            """ 
            Để đăng ký id facebook cho giảng viên: DANGKY GIANGVIEN 'idgiangvien' VD: DANGKY GIANGVIEN SICT1
            Để đăng ký id facebook cho sinh viên: DANGKY SINHVIEN 'idsinhvien' VD: DANGKY SINHVIEN 18IT1
            Để lấy sô lượng sinh viên đi học DIEMDANH SOLUONG 
            Để lấy danh sách sinh viên đi học DIEMDANH DANHSACH 
            Để lấy thông báo ngày hôm nay THONGBAO
            Đê giang viên thêm thông báo THEMTHONGBAO 'tới đâu' 'thong báo' Vd: THEMTHONGBAO 18IT5 Ngày mai các bạn được nghỉ
            
            
            """
            self.sendMessage(huongdan,thread_id)

client = EchoBot(docfile(1), docfile(2))

client.listen()