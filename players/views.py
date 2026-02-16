from django.shortcuts import render

def player_profile(request, player_name):
    data = {
        'player_name' : player_name,
        'games' : '120',
        'wins' : '100',
        'draws' : '10',
        'loses' : '10',
        'winrate' : '83.33%',
    }
    return render(request, 'players/player_profile.html', data)

def players_list(requests):
    data = {
        'players' : ['player1', 'player2', 'player3']
    }
    return render(requests, 'players/players_list.html', data)
