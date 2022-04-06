import linecache, requests, json, os, linecache
from time import sleep as sleep
from datetime import datetime
from datetime import date
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


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
