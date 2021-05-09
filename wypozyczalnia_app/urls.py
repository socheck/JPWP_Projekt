from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cena/', views.cena),
    path('flota/', views.flota),
    path('kontakt/', views.kontakt),
    path('rejestracja/', views.rejestracja),
    path('test/', views.test),
    path('logowanie/', views.logowanie, name="logowanie"),
    path('wylogowywanie/', views.wylogowywanie, name="wylogowywanie"),
    path('testujemape/', views.testujemape,),
    path('dodajmiasto/', views.dodajmiasto),
    path('dlugoterminowyform/', views.dlugoterminowyform),
    path('dodajmiasto/ajax/get_samochody', views.pobieranie_samochodow, name = "pobieranie_samochodow"),
    path('dodaj_strefe/', views.dodaj_strefe),
    path('dodaj_strefe/ajax/post_punkty', views.dodawanie_strefy_baza, name = "dodawanie_strefy_baza"),

]