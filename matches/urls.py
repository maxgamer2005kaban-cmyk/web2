from django.urls import path
from . import views

urlpatterns = [
    path('', views.matches_main_page),
    path('<int:match_id>/', views.matches_detail),
]