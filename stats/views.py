from django.shortcuts import render
from django.http import HttpResponse

    # Create your views here.

def stats_info(request):
    data = {
        'games' : '120',
        'wins' : '100',
        'draws' : '10',
        'loses' : '10',
    }
    return render(request, 'stats/stats_info.html', data)

def stats_detail(request, pk):
    return render(request, 'stats/stats_detail.html')

def stats_category(request, slug):
    return render(request, 'stats/stats_category.html')

def stats_leaderboard(request):
    return render(request, 'stats/stats_leaderboard.html')
