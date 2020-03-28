from django.urls import path

from . import views

urlpatterns = [
    # http://localhost:8000/bar/
    path('', views.index, name = 'index'),
    # http://localhost:8000/bar/beers
    path('beers/', views.beers, name = 'beers'),
    # http://localhost:8000/bar/counters
    path('counters/', views.counters, name = 'counters'),
    # http://localhost:8000/bar/get_beers
    path('get_beers/', views.get_beers, name = 'get_beers'),
    # http://localhost:8000/bar/get_counters
    path('get_counters/', views.get_counters, name = 'get_counters'),
]
