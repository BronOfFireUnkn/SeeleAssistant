#引入运行库#
from airtest.core.api import *

#引入运行模块#
from main import *
from config import *
from fight_airtest import *
from others import *

# 函数封装区域开始#
"看不懂的地方建议不要改"
#官服启动#
def start_Official_1():
    stop_app("com.miHoYo.enterprise.NGHSoD")
    start_app("com.miHoYo.enterprise.NGHSoD")
    sleep(10.0)
    for U in range(1,11):
        start_Official_1_2()
        sleep(5.0)
        if (V == 1):
            break
def start_Official_1_2():    
    if exists(Template(r"resources\forstart\Official\tpl1696321843906.png", record_pos=(-0.456, 0.234), resolution=(1920, 1080))):
        global V
        V = 1
        start_Official_1_1()
    if exists(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080))):
        start_Official_fail()
def start_Official_1_1():
    wait(Template(r"resources\forstart\Official\tpl1696321843906.png", record_pos=(-0.456, 0.234), resolution=(1920, 1080)), timeout=60)
    if exists(Template(r"resources\forstart\Official\tpl1696321843906.png", record_pos=(-0.456, 0.234), resolution=(1920, 1080))):
        start_Official_2()
    else:
        start_Official_fail()
def start_Official_fail():    
    if (V == 0):
        update()
        
def start_Official_2():        
        touch((960,742),times=3)
        wait(Template(r"resources\forstart\Official\tpl1696574217584.png", record_pos=(0.303, 0.247), resolution=(1920, 1080)))
        sleep(1.0)
        wait(Template(r"resources\forstart\Official\tpl1696506420186.png", record_pos=(0.403, 0.167), resolution=(1920, 1080)), intervalfunc=click_7)
        if exists(Template(r"resources\forstart\Official\tpl1696506420186.png", record_pos=(0.403, 0.167), resolution=(1920, 1080))):
            for J in range(1,5):
                if exists(Template(r"resources\forstart\Official\tpl1696506555622.png", record_pos=(0.444, 0.117), resolution=(1920, 1080))):
                    touch(Template(r"resources\forstart\Official\tpl1696506555622.png", record_pos=(0.444, 0.117), resolution=(1920, 1080)))
                sleep(2.0)    
                if exists(Template(r"resources\forstart\Official\tpl1696506420186.png", record_pos=(0.403, 0.167), resolution=(1920, 1080))):
                    wait(Template(r"resources\forstart\Official\tpl1696506420186.png", record_pos=(0.403, 0.167), resolution=(1920, 1080)))
                    touch(Template(r"resources\forstart\Official\tpl1696506420186.png", record_pos=(0.403, 0.167), resolution=(1920, 1080)))
                    click_7()
                else:
                    break
                    
#B服启动#
def start_Bilibili():
    start_app("com.miHoYo.bh3.bilibili")

#更新#
def update():
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)),timeout=200)
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    sleep(20.0)
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)), timeout=2000, interval=2.5)
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
#邮件#
def email():
    wait(Template(r"resources\forstart\Official\tpl1696656307936.png", record_pos=(-0.426, -0.023), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696656307936.png", record_pos=(-0.426, -0.023), resolution=(1920, 1080)))
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696656465814.png", record_pos=(0.384, 0.245), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696656465814.png", record_pos=(0.384, 0.245), resolution=(1920, 1080)))
    if exists(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080))):
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    for M in range(1,4):
        sleep(2.0)
        if exists(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080))):
            sleep(1.0)
            touch(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080)))
        else:
            break
#奖励#
def award_before():
    wait(Template(r"resources\forstart\Official\tpl1696332426831.png", record_pos=(-0.461, -0.188), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696332426831.png", record_pos=(-0.461, -0.188), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332519691.png", record_pos=(0.378, -0.188), resolution=(1920, 1080)),intervalfunc=click_4)
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696332519691.png", record_pos=(0.378, -0.188), resolution=(1920, 1080)))
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
def award_after():
    award_before()
    sleep(2.0)
    touch((1821,989))
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    click_5()
    sleep(2.0)
    touch((1567,929))
    if exists(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080))):
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    touch((611,437), times=4, duration=0.05)
    sleep(1.0)
    touch((587,23), times=4, duration=0.05)
    sleep(1.0)
    touch((1324,976))
    sleep(1.0)
    touch((587,23), times=4, duration=0.05)
    
#返回#
def back_to_origin():
        if exists(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080)))

def back():
        if exists(Template(r"resources\forstart\Official\tpl1696333783080.png", record_pos=(-0.456, -0.254), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696333783080.png", record_pos=(-0.456, -0.254), resolution=(1920, 1080)))

#材料#
def daily_1():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)),intervalfunc=click_1)
    touch(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332845178.png", record_pos=(-0.045, -0.089), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332928974.png", record_pos=(0.362, 0.237), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332955498.png", record_pos=(-0.001, 0.133), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))

#委托接取#
def commission_receive():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
    touch((438,544))
    wait(Template(r"resources\forstart\Official\tpl1696334238858.png", record_pos=(0.124, 0.233), resolution=(1920, 1080)))

    touch((415,528))
    wait(Template(r"resources\forstart\Official\tpl1696334291759.png", record_pos=(0.27, -0.257), resolution=(1920, 1080)))
    for A in range(0,3):
        if exists(Template(r"resources\forstart\Official\tpl1696334318001.png", record_pos=(-0.185, 0.034), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696334318001.png", record_pos=(-0.185, 0.034), resolution=(1920, 1080)))
            touch(Template(r"resources\forstart\Official\tpl1696334568376.png", record_pos=(-0.001, 0.227), resolution=(1920, 1080)))
            touch(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
        else:
            break

#完成委托#
def commission_complete():
        wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
        touch((438,544))
        wait(Template(r"resources\forstart\Official\tpl1696334238858.png", record_pos=(0.124, 0.233), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696398214962.png", record_pos=(0.369, 0.235), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696398239402.png", record_pos=(-0.122, -0.192), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696398249520.png", record_pos=(0.38, 0.243), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696398272984.png", record_pos=(-0.463, -0.256), resolution=(1920, 1080)))
        K_Elysia_ice()
        K_Universal_1()
        touch(Template(r"resources\forstart\Official\tpl1696398272984.png", record_pos=(-0.463, -0.256), resolution=(1920, 1080)))
        exists(Template(r"resources\forstart\Official\tpl1696398503595.png", record_pos=(0.021, -0.191), resolution=(1920, 1080)))


#家园扫荡#    
def homeland_1():
    touch(Template(r"resources\forstart\Official\tpl1696335686551.png", record_pos=(0.305, 0.247), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696336358457.png", record_pos=(-0.464, 0.245), resolution=(1920, 1080)),intervalfunc=click_3)
    sleep(2.0)
    wait(Template(r"resources\forstart\Official\tpl1696913022897.png", record_pos=(-0.348, -0.17), resolution=(1920, 1080)),intervalfunc=click_3)

    #测试插入位置
    #var8 = 3
    wait(Template(r"resources\forstart\Official\tpl1696336442192.png", record_pos=(0.478, 0.002), resolution=(1920, 1080)))
    touch((536,401), times=4, duration=0.05)
    sleep(1.0)
    touch((314,450))
    wait(Template(r"resources\forstart\Official\tpl1696428093851.png", record_pos=(0.09, 0.157), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696428093851.png", record_pos=(0.09, 0.157), resolution=(1920, 1080)))
    touch((1084,62), times=4, duration=0.05)
    sleep(2.0)
    touch(Template(r"resources\forstart\Official\tpl1696428772276.png", record_pos=(0.182, 0.24), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080)))
    if exists(Template(r"resources\forstart\Official\tpl1697034112204.png", threshold=0.85, record_pos=(0.238, -0.092), resolution=(1920, 1080))):
        touch(Template(r"resources\forstart\Official\tpl1697034112204.png", threshold=0.85, record_pos=(0.238, -0.092), resolution=(1920, 1080)))
        sleep(3.0)
        if exists(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
        else:
            sleep(1.0)
            back()
            sleep(1.0)

    sleep(1.0)
    
    touch((1688,273))
    if exists(Template(r"resources\forstart\Official\tpl1697034112204.png", threshold=0.85, record_pos=(0.238, -0.092), resolution=(1920, 1080))):
        touch(Template(r"resources\forstart\Official\tpl1697034112204.png", threshold=0.85, record_pos=(0.238, -0.092), resolution=(1920, 1080)))
        sleep(3.0)
        if exists(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
        else:
            sleep(1.0)
            back()
            sleep(1.0)
            
    sleep(1.0)
    touch((1688,150))
    sleep(1.0)
    if (var13 == 1):
        sleep(1.0)
        far_away_2()
    if (var12 == 1):
        sleep(1.0)
        touch((1677,150))
        sleep(1.0)
        swipe((856,808),(883,382))
        sleep(1.0)
        
    if (var8 < 5):
        for K in range(var8):
            far_away()

    if (var8 > 4):
        for K in range(1,5):
            far_away()
        for I in range(var8-4):
            swipe((856,808),(883,100))
            far_away()
            
def homeland_2():
    #测试插入位置
    #var9 = 4
    wait(Template(r"resources\forstart\Official\tpl1696336358457.png", record_pos=(-0.464, 0.245), resolution=(1920, 1080)))
    touch((1490,1015))
    sleep(4.0)
    wait(Template(r"resources\forstart\Official\tpl1696336442192.png", record_pos=(0.478, 0.002), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696336442192.png", record_pos=(0.478, 0.002), resolution=(1920, 1080)))
    sleep(1.0)
    touch((1564,138), times=60, duration=0.1)
    
    for D in range(var9):
        touch((1569,128), times=4, duration=0.05)
        wait(Template(r"resources\forstart\Official\tpl1696336942629.png", record_pos=(0.442, -0.254), resolution=(1920, 1080)))
        if exists(Template(r"resources\forstart\Official\tpl1696336849145.png", threshold=0.69, rgb=True, record_pos=(0.443, -0.256), resolution=(1920, 1080))):
            C=1
        else:
            C=0
        touch(Template(r"resources\forstart\Official\tpl1696336650521.png", record_pos=(0.18, 0.247), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696336673680.png", record_pos=(0.388, 0.245), resolution=(1920, 1080)))
        sleep(1.0)
        if exists(Template(r"resources\forstart\Official\tpl1696336650521.png", record_pos=(0.18, 0.247), resolution=(1920, 1080))):
            if ( C == 1 ):
                touch(Template(r"resources\forstart\Official\tpl1696336942629.png", record_pos=(0.442, -0.254), resolution=(1920, 1080)))
            if ( C == 0 ):
                touch((1592,376))
                wait(Template(r"resources\forstart\Official\tpl1696336942629.png", record_pos=(0.442, -0.254), resolution=(1920, 1080)))
                touch(Template(r"resources\forstart\Official\tpl1696336650521.png", record_pos=(0.18, 0.247), resolution=(1920, 1080)))
                touch(Template(r"resources\forstart\Official\tpl1696336673680.png", record_pos=(0.388, 0.245), resolution=(1920, 1080)))
                if exists(Template(r"resources\forstart\Official\tpl1696336650521.png", record_pos=(0.18, 0.247), resolution=(1920, 1080))):
                    break

#委托#
def community():
    touch(Template(r"resources\forstart\Official\tpl1696337588915.png", record_pos=(0.17, 0.247), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696337735780.png", record_pos=(-0.11, 0.231), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696337735780.png", record_pos=(-0.11, 0.231), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696337816189.png", record_pos=(-0.378, 0.223), resolution=(1920, 1080)))
    touch((281,973))
    wait(Template(r"resources\forstart\Official\tpl1696337912595.png", record_pos=(0.374, -0.08), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696337912595.png", record_pos=(0.374, -0.08), resolution=(1920, 1080)))
    sleep(4.0)
    touch((1811,344))
    sleep(2.0)
    touch((1371,969))
    sleep(2.0)
    touch((958,806))
    sleep(4.0)
    touch((1820,206))
    for E in range(1,9):
        sleep(3.0)
        touch((186,346))
        sleep(2.0)
        touch((1417,967))
        sleep(2.0)
        touch((1233,844))
        sleep(2.0)
        touch((946,796))
    sleep(4.0)
    back()
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696655879288.png", record_pos=(0.243, 0.229), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696655879288.png", record_pos=(0.243, 0.229), resolution=(1920, 1080)))
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696655950106.png", record_pos=(-0.386, -0.124), resolution=(1920, 1080)))
    sleep(1.0)
    if exists(Template(r"resources\forstart\Official\tpl1696656024015.png", record_pos=(-0.441, -0.101), resolution=(1920, 1080))):
        L = 1
    else:
        L = 0
    
    if (L == 0):
        touch((101,275), times=4, duration=0.07)
        sleep(1.0)
        touch((519,27), times=4, duration=0.07)
        
#万象虚境#
def wonder():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    sleep(2.0)
    wait(Template(r"resources\forstart\Official\tpl1696340297559.png", record_pos=(0.136, -0.104), resolution=(1920, 1080)),intervalfunc=click_2)
    touch(Template(r"resources\forstart\Official\tpl1696340297559.png", record_pos=(0.136, -0.104), resolution=(1920, 1080)))
    sleep(2.0)
    wait(Template(r"resources\forstart\Official\tpl1696340567266.png", record_pos=(-0.344, -0.091), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696340567266.png", record_pos=(-0.344, -0.091), resolution=(1920, 1080)))
    swipe((618,101),(618,943))
    sleep(1.0)
    for G in range(1,3):
        sleep(1.0)
        if exists(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080))):
            sleep(1.0)
            touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
        sleep(1.0)    
        touch(Template(r"resources\forstart\Official\tpl1696340824827.png", record_pos=(-0.128, -0.027), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696340851156.png", record_pos=(0.374, 0.245), resolution=(1920, 1080)))
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696340883104.png", record_pos=(0.365, 0.242), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696340924007.png", record_pos=(0.377, 0.238), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696340924007.png", record_pos=(0.377, 0.238), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080)),timeout=120)
        sleep(5.0)
        if (var5 == 1):
            for F in range(1,9999):
                if exists(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080))):
                    O = 1
                else:
                    O = 0
                    
                if (O == 0):
                    break
                for P in range(1,2):
                    if (O == 0):
                        break
                    K_Elysia_ice()    

        elif (var5 == 0):
            for F in range(1,9999):
                if exists(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080))):
                    O = 1
                else:
                    O = 0
                    
                if (O == 0):
                    break
                for P in range(1,2):
                    if (O == 0):
                        break
                    K_Universal_1()
                    
        sleep(3.0)
        Z()
        sleep(3.0)
        Z()
        sleep(3.0)
        Z()
        sleep(3.0)
        Z()
        sleep(3.0)
        Z()
        touch(Template(r"resources\forstart\Official\tpl1696341596658.png", record_pos=(-0.154, 0.202), resolution=(1920, 1080)))
        
    if(var11 == 1):
        wait(Template(r"resources\forstart\Official\tpl1696820719662.png", record_pos=(0.083, 0.009), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696820719662.png", record_pos=(0.083, 0.009), resolution=(1920, 1080)))
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696820756403.png", record_pos=(0.287, -0.103), resolution=(1920, 1080)))
        sleep(1.0)
        touch((1240,586))
        for Q in range(1,9999):
            if exists(Template(r"resources\forstart\Official\tpl1696820810619.png", record_pos=(-0.374, -0.103), resolution=(1920, 1080))):
                R = 1
                touch((238,348), times=30, duration=0.03)
                touch(Template(r"resources\forstart\Official\tpl1696820983899.png", record_pos=(0.333, 0.181), resolution=(1920, 1080)))
                sleep(1.0)
                touch(Template(r"resources\forstart\Official\tpl1696821033752.png", record_pos=(0.142, 0.148), resolution=(1920, 1080)))
                sleep(1.0)
                touch(Template(r"resources\forstart\Official\tpl1696821033752.png", record_pos=(0.142, 0.148), resolution=(1920, 1080)))

            else:
                R = 0
                
            if (R == 0):
                break
        for T in range(1,9999):
            sleep(2.0)
            if exists(Template(r"resources\forstart\Official\tpl1696821100270.png", record_pos=(0.422, -0.205), resolution=(1920, 1080))):
                touch(Template(r"resources\forstart\Official\tpl1696821100270.png", record_pos=(0.422, -0.205), resolution=(1920, 1080)))
            else:
                break
            
#记忆战场#
def battlefield():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    sleep(2.0)
    wait(Template(r"resources\forstart\Official\tpl1696657542633.png", record_pos=(-0.084, -0.027), resolution=(1920, 1080)),intervalfunc=click_2)
    touch(Template(r"resources\forstart\Official\tpl1696657542633.png", record_pos=(-0.084, -0.027), resolution=(1920, 1080)))
    if exists(Template(r"resources\forstart\Official\tpl1696657673422.png", record_pos=(0.38, 0.247), resolution=(1920, 1080))):
        N = 1
    else:
        N = 0
    
    if (N == 1):
        sleep(1.0)
        touch((207,220))
        sleep(1.0)
        click_6()
        sleep(1.0)
        touch((223,356))
        sleep(1.0)
        click_6()
        sleep(1.0)
        touch((254,539))
        sleep(1.0)
        click_6()
        sleep(1.0)

#戳四戳#
def touch_click():
    for H in range(1,5):
        sleep(30.0)
        touch((780,281))
        
#购买#
def shopping():
    wait(Template(r"resources\forstart\Official\tpl1696336358457.png", record_pos=(-0.464, 0.245), resolution=(1920, 1080)))
    touch((1761,1009))
    wait(Template(r"resources\forstart\Official\tpl1696346322512.png", record_pos=(0.342, -0.257), resolution=(1920, 1080)))
    swipe((190,190),(190,957))
    sleep(1.0)
    touch((185,309),duration=0.1)
    sleep(1.0)
    swipe((1467,870),(1467,220))
    for I in range(0,5):
        if exists(Template(r"resources\forstart\Official\tpl1696346597369.png", record_pos=(-0.255, -0.019), resolution=(1920, 1080))):
            touch(Template(r"resources\forstart\Official\tpl1696346597369.png", record_pos=(-0.255, -0.019), resolution=(1920, 1080)))
            sleep(0.5)
            touch((1326,838))
            if exists(Template(r"resources\forstart\Official\tpl1696346708866.png", record_pos=(0.132, 0.114), resolution=(1920, 1080))):
                touch(Template(r"resources\forstart\Official\tpl1696346708866.png", record_pos=(0.132, 0.114), resolution=(1920, 1080)))
        else:
            break
            
    sleep(1.0)
    touch((177,870))
    sleep(1.0)
    touch((171,760))
    sleep(1.0)
    if exists(Template(r"resources\forstart\Official\tpl1696821364534.png", record_pos=(-0.226, 0.064), resolution=(1920, 1080))):
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696821364534.png", record_pos=(-0.226, 0.064), resolution=(1920, 1080)))
    
    if (var7 == 1):
        swipe((190,957),(190,190))
        sleep(1.0)
        touch((188,889))
        sleep(1.0)
        touch((188,662))
        sleep(1.0)
        swipe((1467,870),(1467,220))
        sleep(1.0)
        touch((1743,488))
        sleep(1.0)
        touch((962,847))
        touch((1326,838))
        
#购买#
def weekly_shopping():
    wait(Template(r"resources\forstart\Official\tpl1696821520097.png", record_pos=(-0.427, 0.089), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696821520097.png", record_pos=(-0.427, 0.089), resolution=(1920, 1080)))
    sleep(1.0)
    wait(Template(r"resources\forstart\Official\tpl1696821568541.png", record_pos=(-0.21, 0.067), resolution=(1920, 1080)))
    sleep(1.0)
    touch((198,290))
    sleep(1.0)
    touch((186,516))
    if exists(Template(r"resources\forstart\Official\tpl1696821708834.png", record_pos=(-0.207, 0.039), resolution=(1920, 1080))):
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696821708834.png", record_pos=(-0.207, 0.039), resolution=(1920, 1080)))
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696821708834.png", record_pos=(-0.207, 0.039), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
    sleep(1.0)    

#杂项#
"出击按钮"
def click_1():
    touch((105,292))
"挑战按钮"    
def click_2():
    touch((94,580))
"远征模块"
def far_away():
    wait(Template(r"resources\forstart\Official\tpl1696429009790.png", record_pos=(0.237, -0.091), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696429009790.png", record_pos=(0.237, -0.091), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))

    touch(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696336121221.png", record_pos=(0.364, 0.228), resolution=(1920, 1080)))
    sleep(1.0)
def far_away_2():
    sleep(1.0)
    touch((1716,290))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1697108310433.png", threshold=0.85, rgb=True, target_pos=6, record_pos=(-0.096, -0.104), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))

    touch(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696336121221.png", record_pos=(0.364, 0.228), resolution=(1920, 1080)))
    sleep(1.0)
    

"家园抽风点确定"
def click_3():
    touch((954,884))
"作战任务"
def click_4():
    touch((168,200))
"作战奖励"
def click_5():
    touch((166,345))
"记忆战场扫荡"
def click_6():
    global S
    S = 1
    for S in range(1,6):
        touch((1386,1021), times=15, duration=0.12)
        touch((985,784), times=15, duration=0.14)
"开场"
def click_7():
    touch((1902,67), times=20, duration=0.05)
""
#进攻#
def K_Short():
    touch((1781,874))
def K_long():
    touch((1781,874),duration=1.0)
def K_Elysia_ice():
    touch((1781,874),duration=20.0)
def K_GG_2_1_1():
    touch((1781,874),duration=1.0)    
def K_Universal_1():
    touch((1781,874), times=50, duration=0.05)
def K_Seele_Elysian_Realm_SuLing_2():
    touch((1781,874), times=20, duration=0.02)
def K_Seele_Elysian_Realm_SuLing_3():
    touch((1781,874),duration=5.0)
def K_Seele_Elysian_Realm_SuLing_1():
    I_Seele_Elysian_Realm_SuLing()
    sleep(6.5)
    K_Seele_Elysian_Realm_SuLing_3()
    sleep(1.0)
    K_Seele_Elysian_Realm_SuLing_2()
    sleep(2.0)
    K_Seele_Elysian_Realm_SuLing_3()
    sleep(1.0)
    K_Seele_Elysian_Realm_SuLing_2()
    sleep(2.0)
    K_Seele_Elysian_Realm_SuLing_3()
    sleep(1.0)
    K_Seele_Elysian_Realm_SuLing_2()
    sleep(2.0)

#闪避#
def J():
    touch((1514,886))
    
#大招#    
def I():
    touch((1785,615))
def I_Seele_Elysian_Realm_SuLing():
    touch((1785,615), duration=1.0)
    
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
