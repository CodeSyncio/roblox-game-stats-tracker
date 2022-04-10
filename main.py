#--start of all importing--
import requests, json , os , webbrowser
from time import sleep as sleep
from datetime import datetime
from datetime import date
from linecache import getline as getl
#--end of all importing--

curdir = os.getcwd() #variable for the current working directory

def cls():
    os.system('cls' if os.name=='nt' else 'clear') #used to clear the console (cls or clear)

conpath = 'config.txt' #name of the config file

TutSetting = (str(getl(conpath, 2))).strip() #gets the stripped data of the second line in config
if str(TutSetting) == ('True') : #if that line is True it will start the tutorial, or it will skip if it isn't
    print('To get the universe id, u need to copy at the numbers after the "universeId" \n on the page that opens when u entered the placeid below.\n\n')
    placeid = input('please type the prefered place id ...')
    cls()
    webbrowser.open('https://games.roblox.com/v1/games/multiget-place-details?placeIds='+ placeid) #opens the webapi in the default browser
    tempclck = input('press enter when you have entered the copied value into the config.txt, saved it and closed it.')
    cls()
    UnivId = getl(conpath, 1).strip() #sets the universe id to the first line of the config (stripped because of newline character)
    print('Universal Id has been set to '+UnivId + ' press enter to start logging.')
    tempclck = input()
    sleep (2)
    cls()
    with open(conpath,'r',encoding='utf-8') as file:
        data = file.readlines() #makes a list of config.txt
    data[1] = "False   \n" #modifies the second line to "False" to avoid always having the tutorial
    with open(conpath, 'w', encoding='utf-8') as file:
        file.writelines(data) #rewrites the config with the modified data
    cls()

#--start of extracting all settings from config--
UnivId = getl(conpath, 1)
delaystrng = str(getl(conpath, 3))
reqdelay = int(delaystrng) / 1000
MaxLogSetting = (str(getl(conpath, 4))).strip()
MaxLogLines = int(getl(conpath, 5))
MinifiedSetting = (str(getl(conpath, 6))).strip()
#--end of extracting all settings from config--

roblox_gnamerequest =requests.get('https://games.roblox.com/v1/games?universeIds='+ UnivId) #gets the gamedata from the given UniverseId
robloxgnametext = roblox_gnamerequest.text #converts the above data to text
roblox_gnamejson = json.loads(roblox_gnamerequest.text) #Load it into a json
gname = roblox_gnamejson['data'][0]['name'] #extract the data "name" from the json

if os.path.exists(curdir+'/logs'): #checks for the folder "logs", if not found it will create one
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
while 1 != 2: #infinite loop
     
    
    roblox_api_req =requests.get('https://games.roblox.com/v1/games?universeIds='+ UnivId) #info on line 45 till 48
    roblox_api_txt = roblox_api_req.text
    roblox_api_json = json.loads(roblox_api_req.text)
    visits = roblox_api_json['data'][0]['visits']
    playing = roblox_api_json['data'][0]['playing']
    now = datetime.now() #now
    current_time = now.strftime("%H:%M:%S") #sets time
    todaydate = date.today() #date
    #start of constructing the text string for the log file (complete and minimized)
    txtstring = (str(todaydate) + '   ' + str(current_time) + '   ' +'Game: '+str(gname) + '  Total Visits: '+str(visits) + '  Curr Playing: '+str(playing) +'\n')
    minifiedTxtString =(str(todaydate) + '  ' + str(current_time) + '  ' +str(gname) + '  V: '+str(visits) + '  P: '+str(playing) +'\n')
    #end of constructing
    if str(MinifiedSetting) == ('False'): #if min setting is true, it will use the shortened version, else it will use the full version
        file = open(curdir+'/logs/'+'log_'+gname+'.txt','a')
        file.write(txtstring)
        file.close
    else:
        file = open(curdir+'/logs/'+'log_'+gname+'.txt','a')
        file.write(minifiedTxtString)
        file.close
        
    print (txtstring) #prints the text
    sleep (reqdelay) #sleeps for a given amount of time
    cls() #clears the screen
    MaxLogCounter = MaxLogCounter + 1 
    if str(MaxLogSetting) == ('True') and MaxLogCounter == MaxLogLines:
        print('Script has reached max logging lines ('+MaxLogSetting+'), press enter to quit')
        ghostinput = input()
        quit()
    else:
        pass
        
    
    
    
    
    

