from django import template
from random import randint
from main.models import *
from main.my_sql import *
register = template.Library()

@register.simple_tag
def get_mon_hoc(lop,user):
    lich = Lich_hoc.objects.filter(Lop=lop,User=user,Thu=getthu())
    return lich
@register.simple_tag
def get_sl_mon_di(user,mon):
    soluong=truy_van(get_slsinhvienmon(user,mon))
    return soluong
@register.simple_tag
def get_sl_mon_diall(user,mon):
    soluong=truy_van(get_slsinhvienmonall(user,mon))
    return soluong
@register.simple_tag
def tileindex(tong,co):
    if tong == 0:
        tong =1;
    soluongco = int((int(co)*100)/int(tong))
    soluongkhong = int(co-soluongco)
    soluong=[soluongkhong,soluongco]
    return soluong
