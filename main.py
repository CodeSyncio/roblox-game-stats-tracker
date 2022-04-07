import requests, json, os, linecache, webbrowser
from xmlrpc.client import boolean
from time import sleep as sleep
from datetime import datetime
from datetime import date
from linecache import getline as getl
curdir = os.getcwd()
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

conpath = 'config.txt'

TutSetting = (str(getl(conpath, 2))).strip()
if str(TutSetting) == ('True') :
    print('To get the universe id, u need to copy at the numbers after the "universeId" \n on the page that opens when u entered the placeid below.\n\n')
    placeid = input('please type the prefered place id ...')
    cls()
    webbrowser.open('https://games.roblox.com/v1/games/multiget-place-details?placeIds='+ placeid)
    tempclck = input('press enter when you have entered the copied value into the config.txt, saved it and closed it.')
    cls()
    UnivId = getl(conpath, 1).strip()
    print('Universal Id has been set to '+UnivId + ' press enter to start logging.')
    tempclck = input()
    sleep (2)
    cls()
    with open(conpath,'r',encoding='utf-8') as file:
        data = file.readlines()              #makes a list of config.txt
    data[1] = "False   \n"                   #modifies the second line to "False" to avoid always having the tutorial
    with open(conpath, 'w', encoding='utf-8') as file:
        file.writelines(data)                #rewrites the config with the modified data
    cls()
UnivId = getl(conpath, 1)
delaystrng = str(getl(conpath, 3))
reqdelay = int(delaystrng) / 1000
MaxLogSetting = (str(getl(conpath, 4))).strip()
MaxLogLines = int(getl(conpath, 5))
MinifiedSetting = (str(getl(conpath, 6))).strip()

roblox_gnamerequest =requests.get('https://games.roblox.com/v1/games?universeIds='+ UnivId)
robloxgnametext = roblox_gnamerequest.text
roblox_gnamejson = json.loads(roblox_gnamerequest.text)
gname = roblox_gnamejson['data'][0]['name']
if os.path.exists(curdir+'/logs'):
    print('logs folder was found!')
    cls()
    pass
else:
    print('The logs folder could not be found. Creating one...')
    os.mkdir(curdir+'/logs')
    sleep(1)
    print('Folder "logs" has been created. continuing... (If you see this message on next start, please make an issue on github)')
    sleep(3)
    cls()
MaxLogCounter = int(0)
while 1 != 2:
     
    
    roblox_api_req =requests.get('https://games.roblox.com/v1/games?universeIds='+ UnivId)
    roblox_api_txt = roblox_api_req.text
    roblox_api_json = json.loads(roblox_api_req.text)
    visits = roblox_api_json['data'][0]['visits']
    playing = roblox_api_json['data'][0]['playing']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    todaydate = date.today()
    txtstring = (str(todaydate) + '   ' + str(current_time) + '   ' +'Game: '+str(gname) + '  Total Visits: '+str(visits) + '  Curr Playing: '+str(playing) +'\n')
    minifiedTxtString =(str(todaydate) + '  ' + str(current_time) + '  ' +str(gname) + '  V: '+str(visits) + '  P: '+str(playing) +'\n')
    if str(MinifiedSetting) == ('False'):
        file = open(curdir+'/logs/'+'log_'+gname+'.txt','a')
        file.write(txtstring)
        file.close
    else:
        file = open(curdir+'/logs/'+'log_'+gname+'.txt','a')
        file.write(minifiedTxtString)
        file.close
        
    print (txtstring)
    sleep (reqdelay)
    cls()
    MaxLogCounter = MaxLogCounter + 1
    if str(MaxLogSetting) == ('True') and MaxLogCounter == MaxLogLines:
        print('Script has reached max logging lines ('+MaxLogSetting+'), press enter to quit')
        ghostinput = input()
        quit()
    else:
        pass
        
    
    
    
    
    

