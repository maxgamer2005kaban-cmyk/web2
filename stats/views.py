from django.shortcuts import render
from django.http import HttpResponse
import datetime
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
    template_name = 'stats/stats_detail.html'
    
    title = f'Детали статистики #{pk}'
    player_status = 'platinum'  # Можно поменять на 'gold', 'silver' или 'noob' для теста
    
    context = {
        'title': title,
        'player_status': player_status,
        'pk': pk,
        'long_string': 'fghkjnljglshdvblisbdvilbiuvubvidbidvbivbihbdibidbvidbvlisdbvildbvsgdvbhbdlkdbvlisdbviydvddddddddddddddddddddddddddddddddd',
        'html_test': '<h1>Hello</h1>',
        'string_with_newlines': 'aaa\nbbb\nccc',
        'my_date': datetime.datetime.now(),
        'test_text': 'ЭТО ОДиН маЛЕНЬкий шаг для чеЛОВека и оГрОмНый СКачОК для челоВЕЧЕсТВА',
    }
    
    return render(request, template_name, context)

def stats_category(request, slug):
    return render(request, 'stats/stats_category.html')

def stats_leaderboard(request):
    template_name = 'stats/stats_leaderboard.html'
    
    title = 'Таблица лидеров'
    players = [
        'Игрок_Алекс',
        'Мастер_123',
        'Про_Геймер',
        'Легенда_Ник',
        'Новичок_007'
    ]
    
    context = {
        'title': title,
        'long_string': 'fghkjnljglshdvblisbdvilbiuvubvidbidvbivbihbdibidbvidbvlisdbvildbvsgdvbhbdlkdbvlisdbviydvdddddddddddddddd00000000000000000000000000000000000000000000000000000000000000000000000',
        'players': players
    }
    
    return render(request, template_name, context)
