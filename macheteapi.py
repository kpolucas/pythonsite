import requests
 
payload={'appid': '440', 'count': '3'} # parametros get
r = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2', params=payload) 
#r.status_code
#print(r.content)
jr = r.json() # seguro hay una manera menos tumba
print(jr['appnews']['newsitems'][0]['contents'])
