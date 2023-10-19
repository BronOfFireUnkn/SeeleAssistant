# -*- encoding=utf8 -*-
__author__ = "BronOfFire_无铭"

from airtest.core.api import *
ST.THRESHOLD = 0.8

from config import *
from others import *
from fight_airtest import *
from assistance_airtest import *
from fight_opencv import *
from assistance_opencv import *

import subprocess, os, shutil, shlex
if os.path.exists("Android/log"):
    shutil.rmtree("Android/log")

if (ChangeToSpecialCommandlineArgs == 0):
    p = subprocess.Popen([Simulator_Path], shell=True)

elif (ChangeToSpecialCommandlineArgs == 1):
    p = subprocess.Popen([Simulator_Path, Special_Commandline_Args], shell=True)
    
sleep(30.0)

os.system(cmd4)
os.system(cmd5)
os.system(cmd6)

from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android:///",], project_root="F:/Cache/AirtestIDE/scripts/SeeleAssistantCode")


# script content
print("start...")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


#脚本主干部分开始#

if (var1 == 1):
    start_Official_1()
    
sleep(4.0)
email()
sleep(4.0)
award_before()
sleep(4.0)
back_to_origin()
sleep(4.0)
daily_1()
sleep(4.0)
back_to_origin()
sleep(4.0)

if (var2 == 1):
    commission_receive()
    sleep(4.0)
    back()
    sleep(4.0)
    back_to_origin()
    sleep(4.0)
    
homeland_1()
sleep(4.0)
back()
sleep(4.0)
homeland_2()
sleep(4.0)

if (var6 == 0):
    back()
    sleep(5.0)
    back()
    sleep(5.0)
elif (var6 == 1):
    back()
    shopping()
    sleep(5.0)
    back_to_origin()
    sleep(5.0)
    
community()
sleep(4.0)
back_to_origin()
sleep(4.0)
weekly_shopping()
sleep(4.0)
back_to_origin()
sleep(4.0)

if (var4 == 1):
    wonder()
    sleep(5.0)
    back_to_origin()
    sleep(5.0)
    
if (var10 == 1):
    battlefield()
    sleep(5.0)
    back_to_origin()
    sleep(5.0)
    
award_after()
sleep(4.0)
back_to_origin()
sleep(4.0)
touch_click()

#脚本主干部分结束#
          
#收尾#         
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)