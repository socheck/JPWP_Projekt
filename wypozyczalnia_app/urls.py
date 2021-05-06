from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cena/', views.cena),
    path('flota/', views.flota),
    path('kontakt/', views.kontakt),
    path('rejestracja/', views.rejestracja),
]