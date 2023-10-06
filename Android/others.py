from config import *

cmd1 = "taskkill /f /t /im HD-Player.exe" 
cmd2 = "taskkill /f /t /im BlueStacksServices.exe"
cmd3 = "taskkill /f /t /im python.exe"
cmd4 = "adb start-server"
cmd5 = "adb kill-server"
cmd6 = "adb connect " + ADB_SERVER_IP + ":" + str(ADB_SERVER_PORT)
