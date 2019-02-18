import requests
 
payload={'appid': '440', 'count': '3'} # parametros get
r = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2', params=payload) 
#r.status_code
#print(r.content)
jr = r.json() # seguro hay una manera menos tumba # aparentemente no
print(jr['appnews']['newsitems'][0]['contents'])




#steam api
# https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0001.29
# http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C4A47AC9177F2BB6D651A010C5DAD268&steamids=76561198089980282
# https://steamcommunity.com/dev
# https://steamcommunity.com/dev/apikey
