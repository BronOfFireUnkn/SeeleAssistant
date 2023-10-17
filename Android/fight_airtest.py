#引入运行库#
from airtest.core.api import *

#引入运行模块#
from main import *
from config import *
from assistance_airtest import *
from others import *

# 函数封装区域开始#
"看不懂的地方建议不要改"
#进攻#
def K_Short():
    touch((1781,874))
def K_long():
    touch((1781,874),duration=1.0)
def K_Elysia_ice():
    touch((1781,874),duration=10.0)
def K_GG_2_1_1():
    touch((1781,874),duration=1.0)    
def K_Universal_1():
    touch((1781,874), times=20, duration=0.05)
    
#闪避#
def J():
    touch((1514,886))
    
#大招#    
def I():
    touch((1785,615))
    
#武器技#
def U():
    touch((1506,656))
    
    
#人偶#
def O():
    touch((1334,755))
    
#W#
def W():
    touch((229,738))   
def W_long():
    touch((229,738),duration=1.0)
    
#A#
def A():
    touch((90,857))
def A_long():
    touch((90,857),duration=1.0)   
#进入#
def Enter():
    touch((1674,1009))

#S#
def S():
    touch((225,989))
def S_long():
    touch((225,989),duration=1.0)
    
#D#
def D():
    touch((353,857))
def D_long():
    touch((353,857),duration=1.0) 
    
#Z#
def Z():
    touch((262,956))

#助战1#
def A1():
    touch((1785,184))
    
#助战2#
def A2():
    touch((1781,431))
       
#往世乐土第一层#
def A_GG_2_1_1():
    touch((90,857),duration=1.0)
          
#临时储存#
def temp_GG_1():
    swipe((1000,200),(1000,300))
    touch(Template(r"\resources\GG\Elysia\tpl1696320319649.png", record_pos=(0.043, 0.004), resolution=(1920, 1080)))
    touch(Template(r"\resources\GG\Elysia\tpl1696320551698.png", record_pos=(0.043, -0.116), resolution=(1920, 1080)))
    exists(Template(r"\resources\GG\Elysia\tpl1696320672630.png", rgb=False, record_pos=(-0.017, -0.231), resolution=(1920, 1080)))
