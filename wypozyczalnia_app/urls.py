from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('cena/', views.cena),
    path('krotkoterminowy/<slug:car_type>/<slug:auto_id>/podliczanie', views.krotkoterminowy_wynajety_podliczanie),
    path('krotkoterminowy/<slug:car_type>/<slug:auto_id>/zwrot', views.krotkoterminowy_wynajety_zwrot),
    path('krotkoterminowy/<slug:car_type>/<slug:auto_id>', views.krotkoterminowy_wynajety),
    path('krotkoterminowy/<slug:car_type>/', views.car_type_selection),
    path('dlugoterminowy/przeglad/<slug:car_type>/', views.dlugoterminowy_przeglad),
    path('dlugoterminowy/wynajmij/<slug:car_type>/<slug:auto_id>/', views.dlugoterminowy_wynajmij, name="dlugoterminowy_wynajmij"),
    path('flota/', views.flota),
    path('kontakt/', views.kontakt),
    path('rejestracja/', views.rejestracja, name="rejestracja"),
    path('test/', views.test),
    path('logowanie/', views.logowanie, name="logowanie"),
    path('wylogowywanie/', views.wylogowywanie, name="wylogowywanie"),
    path('testujemape/', views.testujemape,),
    path('dodajmiasto/', views.dodajmiasto),
    path('dlugoterminowy/', views.dlugoterminowyform),
    path('dodajmiasto/ajax/get_samochody', views.pobieranie_samochodow, name = "pobieranie_samochodow"),
    path('dodaj_strefe/', views.dodaj_strefe),
    path('dodaj_strefe/ajax/post_punkty', views.dodawanie_strefy_baza, name = "dodawanie_strefy_baza"),
    path('uzupelnijprofil/', views.uzupelnijprofil, name="uzupelnijprofil"),
    path('wynajemkrotkoterminowy/', views.wynajemkrotkoterminowy, name="wynajemkrotkoterminowy"),
    path('404/', views.error_404),
    
]