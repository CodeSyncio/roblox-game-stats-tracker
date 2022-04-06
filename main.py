import linecache, requests, json, os, linecache, webbrowser
from xmlrpc.client import boolean
from time import sleep as sleep
from datetime import datetime
from datetime import date
from linecache import getline as getl
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
TutSetting = (str(getl('config.txt', 2))).strip()
if str(TutSetting) == ('True') :
    print('To get the universe id, u need to copy at the numbers after the "universeId" \n on the page that opens when u entered the placeid below.\n\n')
    placeid = input('please type the prefered place id ...')
    cls()
    webbrowser.open('https://games.roblox.com/v1/games/multiget-place-details?placeIds='+ placeid)
    tempclck = input('press enter when you have entered the copied value into the config.txt, saved it and closed it.')
    cls()
    UnivId = getl('config.txt', 1).strip()
    print('Universal Id has been set to '+UnivId + ' press enter to start logging.')
    tempclck = input()
    sleep (2)
    cls()
    with open('config.txt','r',encoding='utf-8') as file:
        data = file.readlines()              #makes a list of config.txt
    data[1] = "False   \n"                   #modifies the second line to "False" to avoid always having the tutorial
    with open('config.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)                #rewrites the config with the modified data
    cls()
UnivId = getl('config.txt', 1)
delaystrng = str(getl('config.txt', 3))
reqdelay = int(delaystrng) / 1000

roblox_gnamerequest =requests.get('https://games.roblox.com/v1/games?universeIds='+ UnivId)
robloxgnametext = roblox_gnamerequest.text
roblox_gnamejson = json.loads(roblox_gnamerequest.text)
gname = roblox_gnamejson['data'][0]['name']


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
    print (txtstring)
    file = open('log_'+gname+'.txt','a')
    file.write(txtstring)
    file.close
    print (txtstring)
    sleep (reqdelay)
    cls()
    
    
    
    

