import requests
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'api/main.html',)


def summoner(request):
    if request.method == 'POST':
        form = request.POST['textfield']
        url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + form + \
              "?api_key=RGAPI-337e2c15-5b09-4a26-a7ba-3560e548497c"
        r = requests.get(url).json()
        # print(r)
        summoner_info = {
            'name': r['name'],
            }
        # print(summoner_info)
        summoner_id = r['id']
        url_league = "https://euw1.api.riotgames.com/lol/league/v4/positions/by-summoner/" + summoner_id + \
                     "?api_key=RGAPI-337e2c15-5b09-4a26-a7ba-3560e548497c"
        r2 = requests.get(url_league).json()[0]
        # print(r2)
        division_info = {
            'type': r2['queueType'],
            'tier': r2['tier'],
            'rank': r2['rank']

        }

        context = {'summoner_info': summoner_info, 'division_info': division_info}
        return render(request, 'api/main.html', context)
    else:
        return redirect('index')
