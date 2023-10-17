import toml

config = toml.load('config.toml')

variables = {}

ADB_SERVER_IP = config['ADB_SERVER_IP']
ADB_SERVER_PORT = config['ADB_SERVER_PORT']
Simulator_Path = config['Game_Path']
ChangeToSpecialCommandlineArgs = int(config['ChangeToSpecialCommandlineArgs'])
Special_Commandline_Args = config['Special_Commandline_Args']

for key, value in config.items():
    if key.startswith('var'):
        variable_name = key.replace('_A', '')
        variables[variable_name] = value

var1 = int(variables['var1'])
var2 = int(variables['var2'])
var4 = int(variables['var4'])
var5 = int(variables['var5'])
var6 = int(variables['var6'])
var7 = int(variables['var7'])
var8 = int(variables['var8'])
var9 = int(variables['var9'])
var10 = int(variables['var10'])
var11 = int(variables['var11'])
var12 = int(variables['var12'])
var13 = int(variables['var13'])

