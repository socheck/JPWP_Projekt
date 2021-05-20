
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .forms import ProfilForm
from .forms import UserUpdateForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import *

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.utils import timezone
import pytz

import json

# Create your views here.
def home(request):
    miasta = Miasto.objects.all()
    return render(request, 'index.html', {'miasta' : miasta})

def cena(request):
    typy_aut = TypAuta.objects.all()
    hulajnoga = Hulajnoga.objects.get(nr_identyfikacyjny = 1)
    content = {
        "typy_aut" : typy_aut,
        'hulajnoga_image' : hulajnoga.image,
        'hulajnoga_cena' : hulajnoga.cena,
        'hulajnoga_name' : "Hulajnoga TX300",
    } 
    return render(request, 'cena.html', content)

def flota(request):
    typy_aut = TypAuta.objects.all()
    hulajnoga = Hulajnoga.objects.get(nr_identyfikacyjny = 1)
    content = {
        "typy_aut" : typy_aut,
        'hulajnoga_image' : hulajnoga.image,
        'hulajnoga_cena' : hulajnoga.cena,
        'hulajnoga_name' : "Hulajnoga TX300",
    } 
    return render(request, 'flota.html',  content)

def kontakt(request):
    miasta = Miasto.objects.all()
    oddzialy = Oddzial.objects.all()
    return render(request, 'kontakt.html', {'miasta': miasta, 'oddzialy' : oddzialy})

def rejestracja(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało pomyślnie założone! Witaj ' + user)

            return redirect('logowanie')

    context = {'form':form}

    return render(request, 'rejestracja.html', context)


def test(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'test.html', context)

def logowanie(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nazwa użytkownika lub hasło jest niepoprawne')
            

    context = {}
    return render(request, 'logowanie.html', context)

def wylogowywanie(request):
    logout(request)
    return redirect('logowanie')

def testujemape(request):
    return render(request, 'testujemape.html')

def dodajmiasto(request):
    miasta = Miasto.objects.all()
    samochody = Samochod.objects.all()
    return render(request, 'dodajmiasto.html', {'miasta': miasta, 'samochody' : samochody})

@csrf_exempt
def dlugoterminowyform(request, typ_auta = 'miejski'):
# nie wiem czy to działa bo w urls są 2 rekordy a jeszcze nie mam jak sprawdzić bo trzeba pewne rzeczy ustalić
    # try:
    #     data = json.loads(request.body.decode('utf-8'))
    # except:
    #     cena = TypAuta.objects.filter(nazwa = typ_auta).values('cena')
        
    # if request.is_ajax and request.method == "POST":
          
    #     cena = data["cena"]
    # else:
    #     cena = TypAuta.objects.filter(nazwa = typ_auta).values('cena')
    # koniec ajaxa
    if request.method == 'POST':
        zaznaczona_cena = request.POST["cena"]
        zaznaczony_typ_auta_id = request.POST["typ_auta_id"]
        # print(request.POST["typ_auta_id"])
        
        samochody_wybrany_typ = Samochod.objects.filter(typ_auta_id = zaznaczony_typ_auta_id)

    

    # nie wiem w sumie co zwracać????

    return render(request, 'dlugoterminowyform.html', {"zaznaczona_cena": zaznaczona_cena, "zaznaczony_typ_auta_id": zaznaczony_typ_auta_id, "samochody_zaznaczone_id": samochody_wybrany_typ})

def pobieranie_samochodow(request):

    if request.is_ajax and request.method == "GET":

        id_miasta = request.GET.get("id_miasta", None)
        nazwa_miasta = request.GET.get("nazwa", None)
        print(id_miasta +" "+ nazwa_miasta)

        if Samochod.objects.filter(miasto_id = id_miasta).exists() and id_miasta is not None:
            zwracane_samochody = list(Samochod.objects.filter(miasto_id = id_miasta))
            context = [{
                "nazwa":car.__str__(),
                "pozycja": car.pozycja,

            } for car in zwracane_samochody]

            return JsonResponse(context, safe=False,status = 200)
        else:
            return JsonResponse({}, status = 200)

    return JsonResponse({}, status = 400)




@login_required
def uzupelnijprofil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Informacje zostały zaaktualizowane')
            return redirect('uzupelnijprofil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'uzupelnijprofil.html', context)

@csrf_exempt
def dodawanie_strefy_baza(request):

    try:
        data = json.loads(request.body.decode('utf-8'))
    except:
        return JsonResponse({}, status = 200)
    print(data["miasto_id"])
    print(data["rodzaj_strefy"])
    print(data["punkty"])
    if Strefa.objects.filter(miasto_id = data["miasto_id"], rodzaj = data["rodzaj_strefy"]).exists():
        return JsonResponse({"message" : "Taka strefa już istnieje. Przejdź do panelu administratora aby dokonać edycji"}, safe=False, status = 200)

        
    if request.is_ajax and request.method == "POST":
        
        nowa_strefa = Strefa()        
        nowa_strefa.rodzaj = data["rodzaj_strefy"]
        nowa_strefa.miasto_id = data["miasto_id"]
        nowa_strefa.lista_pozycji = data["punkty"]
        nowa_strefa.save()
        return JsonResponse({"message" : "Pomyślnie dodano strefę"}, status = 200)
        
    return JsonResponse({}, status = 200)

def dodaj_strefe(request):
    miasta = Miasto.objects.all()
    return render(request, 'dodaj_strefe.html', {'miasta': miasta})

def wynajemkrotkoterminowy(request):
    context = {}
    rent_content = request.POST.get('rent', None)
    context['rent_context'] = rent_context
    return(request, 'wynajemkrotkoterminowy.html', context)

def car_type_selection(request, car_type):
    if(car_type == "hulajnoga"):
        print("hulajnoga")
        hulajnogi =  Hulajnoga.objects.all()
        miasta = Miasto.objects.all()
        strefy = Strefa.objects.filter(rodzaj = "h")
        # trzeba dać żeby zwracało jakiś inny html ale na razie jest tak
        return render(request, 'przeglad_hulajnoga.html', {'miasta': miasta,"hulajnogi" : hulajnogi, 'strefy': strefy, 'hulajnoga_name' : "Hulajnoga TX300",})
    else:
        typ = get_object_or_404(TypAuta, slug=car_type)
        samochody =  Samochod.objects.filter(typ_auta = typ, typ_wynajmu = "k")
        miasta = Miasto.objects.all()
        strefy = Strefa.objects.filter(rodzaj = "s")
        return render(request, 'przeglad.html', {'miasta': miasta,"samochody" : samochody, 'strefy': strefy})

# def krotkoterminowy_wynajety(request, car_type, auto_id):
#     auto = get_object_or_404(Samochod, id=auto_id)
#     if request.method == 'POST':
#         if(request.POST['kod_samochod'] == auto.kod ): # tutaj dodać pole kod
#             return render(request, 'koszt.html', {})
#         else:
#             messages.info(request, 'Wprowadzono niepoprawny kod! Spróbuj ponownie')
    
#     miasta = Miasto.objects.all()
#     return render(request, 'krotkoterminowy_wynajety.html', {'miasta': miasta,'czy_super' : 'jest super', })

def krotkoterminowy_wynajety(request, car_type, auto_id):
    if(car_type == "hulajnoga"):
        auto = get_object_or_404(Hulajnoga, id=auto_id)
        print("hulajnoga")
    else:
        auto = get_object_or_404(Samochod, id=auto_id)
        print("samochód")
    if request.method == 'POST':
        if(request.POST['kod_samochod'] == auto.kod ): # tutaj dodać pole kod
            # user_m = User.objects.get(id= request.user.id)
            # user_profile = user_m.profile
            # if(auto.czy_wynajety == None):
            #     now = datetime.now()
            #     now = make_aware(now, timezone.utc)
            #     auto.czy_wynajety = now
            #     auto.save()
            
            # now_dynamic = datetime.now()
            # now_dynamic = make_aware(now_dynamic, timezone.utc)
            # duration = (now_dynamic - auto.czy_wynajety)
            # duration_in_s = int(duration.total_seconds())
            # print('Z bazy: ')
            # print(auto.czy_wynajety)
            # print('Dynamiczny: ')
            # print(now_dynamic)
            # print(duration_in_s)
            # hours = int(duration_in_s/3600)
            # minutes = int((duration_in_s - 3600*hours)/60)
            # seconds = int(duration_in_s - int(60*minutes) - int(3600*hours))

            # content = {
            #     'user' : user_m,
            #     'user_profile' : user_profile,
            #     'samochod' : auto,
            #     'date_now' : auto.czy_wynajety,
            #     'h' : hours,
            #     'm' : minutes,
            #     's' : seconds,
            # } 

            # return render(request, 'koszt.html', content)
            return redirect('/krotkoterminowy/'+car_type+'/'+auto_id+'/podliczanie')
        else:
            messages.info(request, 'Wprowadzono niepoprawny kod! Spróbuj ponownie')
    
    miasta = Miasto.objects.all()
    return render(request, 'krotkoterminowy_wynajety.html', {'miasta': miasta,'czy_super' : 'jest super', })

def krotkoterminowy_wynajety_podliczanie(request, car_type, auto_id):
    if(car_type == "hulajnoga"):
        auto = get_object_or_404(Hulajnoga, id=auto_id)
        print("hulajnoga")
        pojazd_zmienna = "h"
    else:
        auto = get_object_or_404(Samochod, id=auto_id)
        print("samochód")
        pojazd_zmienna = "s"
    
    user_m = User.objects.get(id= request.user.id)
    user_profile = user_m.profile
    if(auto.czy_wynajety == None):
        print('none')
        now = datetime.now()
        now = make_aware(now, timezone.utc)
        auto.czy_wynajety = now
        auto.save()
    
    now_dynamic = datetime.now()
    now_dynamic = make_aware(now_dynamic, timezone.utc)
    duration = (now_dynamic - auto.czy_wynajety)
    duration_in_s = int(duration.total_seconds())

    hours = int(duration_in_s/3600)
    minutes = int((duration_in_s - 3600*hours)/60)
    seconds = int(duration_in_s - int(60*minutes) - int(3600*hours))

    content = {
        'user' : user_m,
        'user_profile' : user_profile,
        'samochod' : auto,
        'pojazd' : pojazd_zmienna,
        'date_now' : auto.czy_wynajety,
        'h' : hours,
        'm' : minutes,
        's' : seconds,
    } 
    return render(request, 'koszt.html', content)

def dlugoterminowy_przeglad(request, car_type):
    typ = get_object_or_404(TypAuta, slug=car_type)
    samochody =  Samochod.objects.filter(typ_auta = typ, typ_wynajmu = "d", service=False,)
    miasta = Miasto.objects.all()
    return render(request, 'dlugoterminowy_przeglad.html', {'miasta': miasta,"samochody" : samochody, })

def dlugoterminowy_wynajmij(request, car_type, auto_id):
    auto = get_object_or_404(Samochod, id=auto_id)
    typ = get_object_or_404(TypAuta, slug=car_type)
    user_m = User.objects.get(id= request.user.id)
    user_email_ = user_m.email
 
    if request.method == 'POST':
        message = "Imię i Nazwisko: " + request.POST['imie_nazwisko'] + " email: " + request.POST['email'] + " usernaname: " + request.POST['username'] + " Samochód: " + request.POST['samochod']
        print(message)
        send_mail(
        'Wynajem długoterminowy id= ' + auto_id + ' ' + auto.__str__(),
         message, 
         settings.EMAIL_HOST_USER,
         ['wypozyczalniajpwp@gmail.com'],
         fail_silently=False,
         )
        return render(request, 'dlugoterminowy_formularz.html', {'message_name' : message})

    return render(request, 'dlugoterminowy_formularz.html', {'samochod': auto, 'user_mail' : user_email_})

