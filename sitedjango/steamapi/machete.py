'''
import requests
import json

def gamesPlayedImgUrl(key,steamid):
    payload={'key': key, 'steamid': steamid, 'format': 'json'}
    r = requests.get('http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001', params=payload)
    gamesplayed = json.loads(r.text)
    urls = []
    for i in gamesplayed['response']['games']:
        urls.append('https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/' + str(i['appid']) + '/' + str(i['img_logo_url']) + '.jpg')
    return urls

print(gamesPlayedImgUrl('',''))
'''
