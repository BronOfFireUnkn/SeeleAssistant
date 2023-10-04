from airtest.core.api import *

auto_setup(__file__)

from main import *
from config import *
from fight import *

# 函数封装区域开始#
"看不懂的地方建议不要改"
#启动#

def start_Official():
    stop_app("com.miHoYo.enterprise.NGHSoD")
    start_app("com.miHoYo.enterprise.NGHSoD")
    sleep(10.0)
    wait(Template(r"resources\forstart\Official\tpl1696321843906.png", record_pos=(-0.456, 0.234), resolution=(1920, 1080)), timeout=60, intervalfunc=update)
    touch((960,742),times=3)
    wait(Template(r"resources\forstart\Official\tpl1696397869093.png", record_pos=(0.053, 0.246), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696397869093.png", record_pos=(0.053, 0.246), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)),timeout=200)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    sleep(1.0)
    if exists(Template(r"resources\forstart\Official\tpl1696397869093.png", record_pos=(0.053, 0.246), resolution=(1920, 1080))):
        touch(Template(r"resources\forstart\Official\tpl1696397869093.png", record_pos=(0.053, 0.246), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)),timeout=200)
        touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
        touch((612,10), times=20, duration=0.05)

def start_Bilibili():
    start_app("com.miHoYo.bh3.bilibili")

#更新#
def update():
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)),timeout=200)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)),timeout=2000)
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))
#奖励#
def award():
    touch(Template(r"resources\forstart\Official\tpl1696332426831.png", record_pos=(-0.461, -0.188), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332519691.png", record_pos=(0.378, -0.188), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))

#返回#
def back_to_origin():
    touch(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080)))
def back():
    touch(Template(r"resources\forstart\Official\tpl1696333783080.png", record_pos=(-0.456, -0.254), resolution=(1920, 1080)))

#材料#
def daily_1():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332845178.png", record_pos=(-0.045, -0.089), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332928974.png", record_pos=(0.362, 0.237), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332955498.png", record_pos=(-0.001, 0.133), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696333016620.png", record_pos=(-0.001, 0.144), resolution=(1920, 1080)))

#委托接取#
def commission():
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

#家园扫荡#    
def homeland_1():
    touch(Template(r"resources\forstart\Official\tpl1696335686551.png", record_pos=(0.305, 0.247), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696336358457.png", record_pos=(-0.464, 0.245), resolution=(1920, 1080)))
    touch((1262,1013))
    wait(Template(r"resources\forstart\Official\tpl1696332618146.png", record_pos=(-0.353, -0.254), resolution=(1920, 1080)))
    touch((1396,366))
    touch(Template(r"resources\forstart\Official\tpl1696335999759.png", record_pos=(-0.001, 0.142), resolution=(1920, 1080)))
    touch((1417,360))
    touch(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696336121221.png", record_pos=(0.364, 0.228), resolution=(1920, 1080)))
    touch((1417,551))
    touch(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696336121221.png", record_pos=(0.364, 0.228), resolution=(1920, 1080)))
    touch((1412,731))
    touch(Template(r"resources\forstart\Official\tpl1696336106511.png", record_pos=(0.116, 0.226), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696336121221.png", record_pos=(0.364, 0.228), resolution=(1920, 1080)))
def homeland_2():
    wait(Template(r"resources\forstart\Official\tpl1696336358457.png", record_pos=(-0.464, 0.245), resolution=(1920, 1080)))
    touch((1490,1015))
    wait(Template(r"resources\forstart\Official\tpl1696336442192.png", record_pos=(0.478, 0.002), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696336442192.png", record_pos=(0.478, 0.002), resolution=(1920, 1080)))
    touch((1564,138), times=60, duration=0.1)
    
    for D in range(1,5):
        touch((1569,128))
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
    sleep(2.0)
    touch((1811,344))
    sleep(1.0)
    touch((1371,969))
    sleep(1.0)
    touch((958,806))
    sleep(1.0)
    touch((1820,206))
    for E in range(1,9):
        sleep(2.0)
        touch((186,346))
        sleep(1.0)
        touch((1417,967))
        sleep(1.0)
        touch((1233,844))
        sleep(1.0)
        touch((946,796))

#万象虚境#
def wonder():
    wait(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696332763358.png", record_pos=(0.364, -0.159), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696332801053.png", record_pos=(0.336, 0.109), resolution=(1920, 1080)))
    touch((85,572))
    sleep(1.0)
    touch(Template(r"resources\forstart\Official\tpl1696340297559.png", record_pos=(0.136, -0.104), resolution=(1920, 1080)))
    wait(Template(r"resources\forstart\Official\tpl1696340567266.png", record_pos=(-0.344, -0.091), resolution=(1920, 1080)))
    touch(Template(r"resources\forstart\Official\tpl1696340567266.png", record_pos=(-0.344, -0.091), resolution=(1920, 1080)))
    swipe((618,101),(618,943))
    sleep(1.0)
    for G in range(1,3):
        touch(Template(r"resources\forstart\Official\tpl1696340824827.png", record_pos=(-0.128, -0.027), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696340851156.png", record_pos=(0.374, 0.245), resolution=(1920, 1080)))
        sleep(1.0)
        touch(Template(r"resources\forstart\Official\tpl1696340883104.png", record_pos=(0.365, 0.242), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696340924007.png", record_pos=(0.377, 0.238), resolution=(1920, 1080)))
        touch(Template(r"resources\forstart\Official\tpl1696340924007.png", record_pos=(0.377, 0.238), resolution=(1920, 1080)))
        wait(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080)),timeout=120)
        if (var5 == 1):
            for F in range(1,9999):
                K_Elysia_ice()
                if assert_not_exists(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080))):
                    break

        elif (var5 == 0):
            for F in range(1,9999):
                K_Universal_1()
                if assert_not_exists(Template(r"resources\forstart\Official\tpl1696340973424.png", record_pos=(-0.46, -0.256), resolution=(1920, 1080))):
                    break
        sleep(15.0)
        Z()
        sleep(15.0)

        touch(Template(r"resources\forstart\Official\tpl1696341596658.png", record_pos=(-0.154, 0.202), resolution=(1920, 1080)))

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
        