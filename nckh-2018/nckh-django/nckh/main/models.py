from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Quan_ly(models.Model):
    User = models.CharField(primary_key=True,max_length=200)
    Co_quan =models.CharField(max_length=200)
    Ten_quan_ly = models.CharField(max_length=200)
    Dia_chi=models.CharField(max_length=200)
    Sdt=models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Ma_so=models.CharField(unique=True,max_length=50)
    Loai=models.CharField(max_length=100)

class Diem_danh(models.Model):
    User = models.CharField( max_length=200)
    Rfid=models.CharField(max_length=100)
    Fgid=models.CharField(max_length=100)
    Thu=models.CharField(max_length=100)
    Ngay=models.DateField()
    Gio=models.TimeField()
    Time=models.DateTimeField()
    Phong=models.TextField(max_length=100)
    ppk=models.ForeignKey(Quan_ly,on_delete=models.CASCADE)

class Giang_vien(models.Model):
    User = models.CharField(max_length=200)
    ID_giang_vien = models.CharField(max_length=100)
    Ten = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Sdt = models.CharField(max_length=100)
    ppk_Giang_vien = models.ForeignKey(Quan_ly, on_delete=models.CASCADE)

class Lich_hoc(models.Model):
    User = models.CharField( max_length=200)
    ID_mon_hoc = models.CharField(max_length=100)
    ID_giang_vien = models.CharField(max_length=100)
    Ten = models.CharField(max_length=100)
    Ten_mon_hoc = models.CharField(max_length=100)
    Tin_chi = models.IntegerField()
    Thu = models.CharField(max_length=100)
    Lop = models.CharField(max_length=100)
    Bat_dau = models.TimeField()
    Ket_thuc = models.TimeField()
    Phong = models.CharField(max_length=100)
    ppk_Lich_hoc = models.ForeignKey(Quan_ly, on_delete=models.CASCADE)
class Sinh_vien(models.Model):
    User = models.CharField(max_length=200)
    ID_sinh_vien = models.CharField(max_length=100,)
    Rfid = models.CharField(max_length=100, unique=True,null=True,blank=True)
    Fgid = models.CharField(max_length=100)
    Ten = models.CharField(max_length=100)
    Lop = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Sdt = models.CharField(max_length=100)
    ppk_Sinh_vien = models.ForeignKey(Quan_ly, on_delete=models.CASCADE)
class Phong(models.Model):
    User = models.CharField(max_length=200)
    Lop = models.CharField(max_length=100)
    Tong_so_hoc_sinh = models.IntegerField()
    Chu_nhiem = models.CharField(max_length=100)
    Khoa_bat_dau = models.IntegerField()
    ppk_Phong = models.ForeignKey(Quan_ly, on_delete=models.CASCADE)

