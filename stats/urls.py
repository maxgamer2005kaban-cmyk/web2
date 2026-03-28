from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.stats_info, name='info'),
    path('<int:pk>/', views.stats_detail, name='detail'),
    path('leaderboard/',
         views.stats_leaderboard,
         name='leaderboard'),
    path('add/', views.add_player, name='add_player'),
]
