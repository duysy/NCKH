from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.models import User ,UserManager
from django.urls import path
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from main.models import *
from .my_sql import *
from django.contrib.auth import get_user

# from django.core.files.storage import FileSystemStorage
# from django.utils import timezone
# Create your views here.
def login(request):
        if request.method == 'POST':
                Username = request.POST["Username"]
                Password = request.POST["Password"]
                user = authenticate(username=Username, password=Password)
                if user is None:
                        return HttpResponseRedirect('/signup/', )
                else:
                        Login(request, user)
                        return HttpResponseRedirect('/')
        else:
                return render(request, 'main/login.html', )
def logout(request):
    Logout(request)
    return HttpResponseRedirect("/login/")

def signup(request):
        if request.method == 'POST':
               try:
                       Username = request.POST["Username"]
                       Password = request.POST["Password"]
                       Email = request.POST["Email"]
                       user = authenticate(username=Username, password=Password)
                       if user is None:
                               user = User.objects.create_user(Username, Email, Password)
                               user.save()
                               Quan_ly(User=user, Co_quan="*", Ten_quan_ly="*", Dia_chi="*",Sdt="*", Email="*",Ma_so=str(user), Loai="*").save()
                               return HttpResponseRedirect('/login/')
                       else:
                               return HttpResponse("Bạn đã có tài khoản")


               except:
                       return render(request, 'main/signup.html', )
        else:
                return render(request, 'main/signup.html', )
def index(request):
        if request.user.is_authenticated:
                user = get_user(request).get_username()
                try:
                        quanly = Quan_ly.objects.get(pk=user)
                        sohocsinh=quanly.sinh_vien_set.all().count()
                        solop=quanly.sinh_vien_set.values('Lop').distinct().count()
                        sophong=quanly.lich_hoc_set.values('Phong').distinct().count()
                        somonhoc=quanly.lich_hoc_set.values('Ten_mon_hoc').distinct().count()
                        tenmonhoc = quanly.lich_hoc_set.values('Ten_mon_hoc').distinct()
                        soluong={"sohocsinh":sohocsinh,"solop":solop,"sophong":sophong,"somonhoc":somonhoc}
                        return render(request, 'main/index.html',{"user":user,"soluong":soluong,"tenmonhoc":tenmonhoc})
                except:
                        return render(request, 'main/index.html',{"user":user})
        else:
                return HttpResponseRedirect('/login/')
def chart(request):
        if request.user.is_authenticated:
                user = get_user(request).get_username()
                try:
                        return render(request, 'main/chart.html',{"user":user})
                except:
                        return render(request, 'main/chart.html',{"user":user})
        else:
                return HttpResponseRedirect('/login/')
def chon_chi_tiet(request):
        if request.user.is_authenticated:
                user = get_user(request).get_username()
                quanly = Quan_ly.objects.get(pk=user)
                try:
                        table = quanly.lich_hoc_set.values("Lop").distinct()
                        return render(request, 'main/chon_chi_tiet.html',{"user":user,"table":table})
                except:
                        return render(request, 'main/chon_chi_tiet.html',{"user":user})
        else:
                return HttpResponseRedirect('/login/')
#########################################################################################################################
def profile(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        quanly1 = Quan_ly.objects.get(pk=user)
                        if request.method == 'POST':
                                tentochuc = request.POST['tentochuc']
                                quanly = request.POST['quanly']
                                sodienthoai = request.POST['sodienthoai']
                                email = request.POST['email']
                                diachi = request.POST['diachi']
                                masudung = request.POST['masudung']
                                loaitochuc = request.POST['loaitochuc']
                                quanly2 = Quan_ly.objects.filter(pk=user)
                                quanly2.update(Co_quan=tentochuc,Ten_quan_ly=quanly,Dia_chi=diachi,Sdt=sodienthoai,Email=email,
                                        Ma_so=masudung,Loai=str(loaitochuc).upper()).save()
                                return render(request, 'main/profile.html',{"user":user,"quanly":quanly1})
                        else:
                                return render(request, 'main/profile.html', {"user": user,"quanly":quanly1})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/profile.html', {"user": user,"quanly":quanly1})
def form_sinhvien(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        if request.method == 'POST':
                                idsinhvien = request.POST['idsinhvien']
                                rfid = request.POST['rfid']
                                fgid = request.POST['fgid']
                                hovaten = request.POST['hovaten']
                                lop = request.POST['lop']
                                email = request.POST['email']
                                sodienthoai = request.POST['sodienthoai']
                                quan_ly = Quan_ly.objects.get(pk=user)
                                Sinh_vien(ppk_Sinh_vien=quan_ly,User=user,ID_sinh_vien=str(idsinhvien).upper(),
                                          Rfid=rfid,Fgid=fgid,Ten=hovaten,Lop=str(lop).upper(),Email=email,Sdt=sodienthoai).save()

                                return render(request, 'main/form_sinhvien.html',{"user":user} )
                        else:
                                return render(request, 'main/form_sinhvien.html', {"user":user})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/form_sinhvien.html',{"user":user} )

def form_giangvien(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        if request.method == 'POST':
                                idgiangvien = request.POST['idgiangvien']
                                tengiangvien = request.POST['tengiangvien']
                                email = request.POST['email']
                                sodienthoai = request.POST['sodienthoai']
                                quan_ly = Quan_ly.objects.get(pk=user)
                                Giang_vien(ppk_Giang_vien=quan_ly,User=user,ID_giang_vien=str(idgiangvien).upper(),Ten=tengiangvien,
                                           Email=email,Sdt=sodienthoai).save()
                                return render(request, 'main/form_giangvien.html',{"user":user})
                        else:
                                return render(request, 'main/form_giangvien.html',{"user":user})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/form_giangvien.html',{"user":user})
def form_phong_lop(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        if request.method == 'POST':
                                lop = request.POST['lop']
                                tongsohocsinh = request.POST['tongsohocsinh']
                                khoahoc = request.POST['khoahoc']
                                quan_ly = Quan_ly.objects.get(pk=user)
                                Phong(ppk_Phong=quan_ly,User=user,Lop=str(lop).upper(),Tong_so_hoc_sinh=tongsohocsinh,
                                           Khoa_bat_dau=khoahoc).save()
                                return render(request, 'main/form_phong_lop.html',{"user":user})
                        else:
                                return render(request, 'main/form_phong_lop.html',{"user":user})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/form_phong_lop.html',{"user":user})
def form_lichhoc(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        if request.method == 'POST':
                                print(request.POST)
                                idmonhoc = request.POST['idmonhoc']
                                idgiangvien = request.POST['idgiangvien']
                                tengiangvien = request.POST['tengiangvien']
                                tenmonhoc = request.POST['tenmonhoc']
                                sotinchi = request.POST['sotinchi']
                                thu = request.POST['thu']
                                lop = request.POST['lop']
                                giobatdau = request.POST['giobatdau']
                                gioketthuc = request.POST['gioketthuc']
                                phong = request.POST['phong']
                                quan_ly = Quan_ly.objects.get(pk=user)
                                Lich_hoc(ppk_Lich_hoc=quan_ly,User=user,ID_mon_hoc=str(idmonhoc).upper(),ID_giang_vien=str(idgiangvien).upper(),
                                         Ten=tengiangvien,Ten_mon_hoc=str(tenmonhoc).upper(),Tin_chi=sotinchi,Thu=str(thu),Lop=str(lop).upper(),
                                         Bat_dau=giobatdau,Ket_thuc=gioketthuc,Phong=str(phong).upper()).save()

                                return render(request, 'main/form_lichhoc.html',{"user":user})
                        else:
                                return render(request, 'main/form_lichhoc.html',{"user":user})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/form_lichhoc.html',{"user":user})

########################################################################################################################
def table_sinhvien(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        quanly = Quan_ly.objects.get(pk=user)
                        table = quanly.sinh_vien_set.all().order_by('Lop')
                        return render(request, 'main/table_sinhvien.html', {"user": user, 'table': table})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_sinhvien.html', {"user": user,'table':table})
def table_giangvien(request):
        try:
                if request.user.is_authenticated:

                        user = get_user(request).get_username()

                        quanly = Quan_ly.objects.get(pk=user)
                        table = quanly.giang_vien_set.all()

                        return render(request, 'main/table_giangvien.html', {"user": user, 'table': table})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_giangvien.html', {"user": user,'table':table})
def table_lichhoc(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        quanly = Quan_ly.objects.get(pk=user)
                        table = quanly.lich_hoc_set.all()
                        return render(request, 'main/table_lichhoc.html', {"user": user, 'table': table})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_lichhoc.html', {"user": user,'table':table})
def table_phong_lop(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        quanly = Quan_ly.objects.get(pk=user)
                        table = quanly.phong_set.all()
                        return render(request, 'main/table_phong_lop.html', {"user": user, 'table': table})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_phong_lop.html', {"user": user,'table':table})
def table_diemdanh(request):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        quanly = Quan_ly.objects.get(pk=user)
                        # table = quanly.diem_danh_set.all()
                        table=truy_van(get_dssvdiemdanh(user))
                        return render(request, 'main/table_diemdanh.html', {"user": user, 'table': table})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_diemdanh.html', {"user": user,'table':table})

def table_chon_chi_tiet(request,lop,monhoc,idgv):
        try:
                if request.user.is_authenticated:
                        user = get_user(request).get_username()
                        table=truy_van(get_dssvdihoc(user,lop,monhoc,idgv))
                        return render(request, 'main/table_chon_chi_tiet.html', {"user": user, 'table': table,'monhoc':monhoc})
                else:
                        return HttpResponseRedirect('/login/')
        except:
                return render(request, 'main/table_chon_chi_tiet.html', {"user": user,'table':table})
################################################################################################################################
def diem_danh_post(request,user):
       if request.method == 'POST':
                print(request.POST)
                phong=request.POST['phong']
                fgid = request.POST['fgid']
                Diem_danh(User=str(user), Rfid='null', Fgid=fgid, Thu=getthu(), Ngay=getngay(), Gio=getgio(),Time=getdatetime(),
                          Phong=str(phong).upper(), ppk_id=str(user)).save()
                return HttpResponse("OK" + user + phong + str(fgid))
def diem_danh(request,user,phong,fgid):
        Diem_danh(User=str(user),Rfid = 'null',Fgid=fgid,Thu=getthu(),Ngay=getngay(),Gio=getgio(),Time=getdatetime(),
                  Phong=str(phong).upper(),ppk_id=str(user)).save()
        return HttpResponse("OK"+user+phong+str(fgid)+getdatetime())
def xoa(request,bang,id):
        if request.user.is_authenticated:
                user = get_user(request).get_username()
                try:
                       if str(bang) == "Giang_vien":
                               if str(id) == 'all':
                                       Giang_vien.objects.all().delete()
                               else:
                                       Giang_vien.objects.filter(pk=id, User=user).delete()
                       if str(bang) == "Lich_hoc":
                               if str(id) == 'all':
                                       Lich_hoc.objects.all().delete()
                               else:
                                       Lich_hoc.objects.filter(pk=id, User=user).delete()
                       if str(bang) == "Sinh_vien":
                               if str(id) == 'all':
                                       Sinh_vien.objects.all().delete()
                               else:
                                       Sinh_vien.objects.filter(pk=id, User=user).delete()
                       if str(bang) == "Diem_danh":
                               if str(id) == 'all':
                                       Diem_danh.objects.all().delete()
                               else:
                                       Diem_danh.objects.filter(pk=id, User=user).delete()


                       return HttpResponse("<p>Giang_vien-Lich_hoc-Sinh_vien-Diem_danh@diem_danh-user-phong-fgid(all)</p>")
                except:

                        return HttpResponse("<p>Giang_vien-Lich_hoc-Sinh_vien-Diem_danh@diem_danh-user-phong-fgid(all)</p>")

        else:
                return HttpResponseRedirect('/login/')
