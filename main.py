import linecache, requests, json, os, time , linecache
from time import sleep as sleep
from datetime import datetime
from datetime import date



roblox_api_req =requests.get('https://games.roblox.com/v1/games?universeIds=113491250')
roblox_api_txt = roblox_api_req.text
roblox_api_json = json.loads(roblox_api_req.text)
visits = roblox_api_json['data'][0]['visits']
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
todaydate = date.today()

print(visits)
sleep (50)
