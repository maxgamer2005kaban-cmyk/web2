from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import VideoProduct
from .forms import PlayerForm
    # Create your views here.

def stats_info(request):
    all_products = VideoProduct.objects.all()
    
    data = {
        'games' : '120',
        'wins' : '100',
        'draws' : '10',
        'loses' : '10',
        'products': all_products,
    }
    return render(request, 'stats/stats_info.html', data)

def stats_detail(request, pk):
    template_name = 'stats/stats_detail.html'
    
    product = get_object_or_404(VideoProduct, pk=pk)
    
    title = f'Детали продукта: {product.title}'
    player_status = 'platinum'  # Можно поменять на 'gold', 'silver' или 'noob' для теста
    
    context = {
        'title': title,
        'player_status': player_status,
        'product': product,
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

def add_player(request):
    # Создаем экземпляр формы (аналогично 'userform = UserForm()')
    # При реальном использовании здесь также будет сохранение данных при request.method == 'POST'
    form = PlayerForm()
    
    # Передаем форму в шаблон 'add_player.html'
    return render(request, 'stats/add_player.html', {'form': form})
