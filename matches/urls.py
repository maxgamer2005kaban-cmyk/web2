from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('', views.matches_main_page, name='main'),
    path('<int:match_id>/', views.matches_detail, name='detail'),
]