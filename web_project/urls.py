from django.contrib import admin
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.main_page),
    path('stats/', include('stats.urls')),
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls'))
]
