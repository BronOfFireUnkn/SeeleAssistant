# -*- encoding=utf8 -*-
__author__ = "BronOfFire_无铭"

from airtest.core.api import *

import subprocess, os

p = subprocess.Popen([r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"], shell=True)

cmd1 = "taskkill /f /t /im HD-Player.exe" 
cmd2 = "taskkill /f /t /im BlueStacksServices.exe"
cmd3 = "taskkill /f /t /im python.exe"
cmd4 = "adb start-server"
cmd5 = "adb kill-server"
cmd6 = "adb connect 127.0.0.1:5555"

sleep(30.0)

os.system(cmd5)
os.system(cmd4)
os.system(cmd6)

from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android:///",], project_root="F:/Cache/AirtestIDE/scripts/SeeleAssistantCode")


# script content
print("start...")

from config import *
from fight import *
from assistance import *

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


#脚本主干部分开始#

if (var1 == 1):
    start_Official()
    
award()
back_to_origin()
daily_1()
back_to_origin()

if (var2 == 1):
    commission()
    back()
    back_to_origin()
    
homeland_1()
back()
homeland_2()

if (var6 == 0):
    back()
    back()
elif (var6 == 1):
    shopping()
    back_to_origin()
    
community()
back_to_origin()

if (var4 == 1):
    wonder()
    back_to_origin()
    
touch_click()  

#脚本主干部分结束#
          

#收尾#         
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)