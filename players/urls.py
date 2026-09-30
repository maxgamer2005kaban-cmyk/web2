from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.players_list, name='list'),
    path('players_list/', views.players_list, name='list_alt'),
    path('<int:pk>/edit/', views.player_edit, name='edit'),
    path('<int:pk>/delete/', views.player_delete, name='delete'),
    path('<str:player_name>/', views.player_profile, name='profile'),
]
