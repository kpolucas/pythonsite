from django.shortcuts import render

def index(request):
    import requests
     
    #Funciona pero no formatea html
    #payload={'appid': '440', 'count': '3'} # parametros get
    #r = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2', params=payload) 
    #jr = r.json() # seguro hay una manera menos tumba
    #print(jr['appnews']['newsitems'][0]['contents'])
    #c = {'api_response': jr['appnews']['newsitems'][0]['contents']}
    #return render(request, 'index.html', c)
    return render(request, 'index.html', {'api_response': '<b>peron</b>'})
