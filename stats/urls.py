from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_info),
    path('<int:pk>/', views.stats_detail),
    path('leaderboard/', views.stats_leaderboard),
]
