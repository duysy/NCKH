from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.login,name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('', views.index, name="index"),
    path('chart/', views.chart, name="chart"),
    path('profile/', views.profile, name="profile"),
    path('chon_chi_tiet/', views.chon_chi_tiet, name="chon_chi_tiet"),
    path('form/form_sinhvien/', views.form_sinhvien, name="form_sinhvien"),
    path('form/form_giangvien/', views.form_giangvien, name="form_giangvien"),
    path('form/form_lichhoc/', views.form_lichhoc, name="form_lichhoc"),
    path('form/form_phong_lop/', views.form_phong_lop, name="form_phong_lop"),
    path('table/table_sinhvien/', views.table_sinhvien, name="table_sinhvien"),
    path('table/table_giangvien/', views.table_giangvien, name="table_giangvien"),
    path('table/table_lichhoc/', views.table_lichhoc, name="table_lichhoc"),
    path('table/table_phong_lop/', views.table_phong_lop, name="table_phong_lop"),
    path('table/table_diemdanh/', views.table_diemdanh, name="table_diemdanh"),
    path('chon_chi_tiet/table_chon_chi_tiet/<lop>/<monhoc>/<idgv>', views.table_chon_chi_tiet, name="table_chon_chi_tiet"),
    path('diem_danh_post/<user>/', views.diem_danh_post, name="diem_danh_post"),
    path('diem_danh/<user>/<phong>/<fgid>', views.diem_danh, name="diem_danh"),
    path('xoa/<bang>/<id>/', views.xoa, name="xoa"),

]