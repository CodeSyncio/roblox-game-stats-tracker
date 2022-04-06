import linecache, requests, json, os, linecache, webbrowser
from time import sleep as sleep
from datetime import datetime
from datetime import date
from linecache import getline as getl
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

TutSetting = bool(getl('config.txt', 2))
print (TutSetting)

if bool(TutSetting) == True :
    print('To get the universe id, u need to look at the numbers after the \n on the page that opens when u press enter, and then put it in the config')
    temp = input('press enter to open link...')
else:
    pass






UnivId = getl('config.txt', 1)


while 1 != 2:
    roblox_api_req =requests.get('https://games.roblox.com/v1/games?universeIds=113491250')
    roblox_api_txt = roblox_api_req.text
    roblox_api_json = json.loads(roblox_api_req.text)

    visits = roblox_api_json['data'][0]['visits']
    gamename = roblox_api_json['data'][0]['name']
    playing = roblox_api_json['data'][0]['playing']

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    todaydate = date.today()
    txtstring = (str(todaydate) + '   ' + str(current_time) + '   ' +'Game: '+str(gamename) + '  Total Visits: '+str(visits) + '  Curr Playing: '+str(playing) +'\n')
    file = open('log_'+gamename+'.txt','a')
    file.write(str(txtstring))
    file.close
    
    
    print(visits)
    print(gamename)
    sleep (1)
