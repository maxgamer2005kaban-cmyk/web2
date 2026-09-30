from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_POST

from .forms import PlayerEditForm
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


@require_http_methods(['GET', 'POST'])
def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    form = PlayerEditForm(
        request.POST if request.method == 'POST' else None,
        instance=player,
    )
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('players:list')
    return render(request, 'players/player_edit.html', {'form': form})


@require_POST
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('players:list')
