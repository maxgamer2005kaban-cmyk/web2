from django.shortcuts import render, get_object_or_404
from .models import Player


def player_profile(request, player_name):
    player = get_object_or_404(Player, name=player_name)
    data = {
        'player_name': player.name,
        'games': player.games_played,
        'wins': player.wins,
        'loses': player.games_played - player.wins,
        'winrate': f'{player.winrate()}%',
    }
    return render(request, 'players/player_profile.html', data)


def players_list(request):
    data = {
        'players': Player.objects.all()
    }
    return render(request, 'players/players_list.html', data)
