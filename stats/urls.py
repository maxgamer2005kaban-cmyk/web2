from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_info, name='stats_info'),
    path('<int:pk>/', views.stats_detail, name='stats_detail'),
    path('leaderboard/',
         views.stats_leaderboard,
         name='stats_leaderboard'),
]
