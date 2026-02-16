from django.urls import path
from . import views

urlpatterns = [
    path('', views.players_list),
    path('players_list/', views.players_list),
    path('<str:player_name>/', views.player_profile),
]
