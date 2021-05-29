
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
import math
from decimal import Decimal

import json

# Create your views here.
def home(request):
    miasta = Miasto.objects.all()
    oddzialy = Oddzial.objects.all()
    return render(request, 'index.html', {'miasta' : miasta, 'oddzialy' : oddzialy})

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
    if request.method == 'POST':
        zaznaczona_cena = request.POST["cena"]
        zaznaczony_typ_auta_id = request.POST["typ_auta_id"]
        
        samochody_wybrany_typ = Samochod.objects.filter(typ_auta_id = zaznaczony_typ_auta_id)

    

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
        nowa_strefa.rodzaj = data["rodzaj_strefy"][0:1]
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
        hulajnogi =  Hulajnoga.objects.filter(service=False, czy_wynajety = None)
        miasta = Miasto.objects.all()
        strefy = Strefa.objects.filter(rodzaj = "h")
        return render(request, 'przeglad_hulajnoga.html', {'miasta': miasta,"hulajnogi" : hulajnogi, 'strefy': strefy, 'hulajnoga_name' : "Hulajnoga TX300",})
    else:
        typ = get_object_or_404(TypAuta, slug=car_type)
        samochody =  Samochod.objects.filter(typ_auta = typ, typ_wynajmu = "k", service=False, czy_wynajety = None)
        miasta = Miasto.objects.all()
        strefy = Strefa.objects.filter(rodzaj = "s")
        return render(request, 'przeglad.html', {'miasta': miasta,"samochody" : samochody, 'strefy': strefy})


def krotkoterminowy_wynajety(request, car_type, auto_id):
    if(car_type == "hulajnoga"):
        auto = get_object_or_404(Hulajnoga, id=auto_id)
        rodzaj = "h"
        print("hulajnoga")
    else:
        auto = get_object_or_404(Samochod, id=auto_id)
        rodzaj = "s"
        print("samochód")
    if request.method == 'POST':

        user_m = get_object_or_404(User, id= request.user.id)
        zamowienia = Zamowienia.objects.filter(id_usera = request.user.id, czy_obecnie_wynajety = True)
        print(zamowienia)
        if not zamowienia:
            print("Podane zamowienie nie istnieje")
        if auto.czy_wynajety == None:
            print("Auto nie jest wynajete")
        if auto.service == False:
            print("Auto nie jest w serwisie")
        if user_m.profile.karta != None:
            print("Pole karta jest uzupełnione")
        if(request.POST['kod_samochod'] == auto.kod and not zamowienia and auto.czy_wynajety == None and auto.service == False and user_m.profile.karta != None): # tutaj dodać pole kod
            now = datetime.now()
            now = make_aware(now, timezone=None)
            auto.czy_wynajety = now
            auto.save()

            nowe_zamowienie = Zamowienia()        
            nowe_zamowienie.id_usera = request.user.id
            nowe_zamowienie.nr_karty = user_m.profile.karta
            nowe_zamowienie.rodzaj_pojazdu = rodzaj
            nowe_zamowienie.typ_wynajmu = "k" 
            nowe_zamowienie.id_pojazdu = auto.id
            nowe_zamowienie.czas_startu = auto.czy_wynajety
            nowe_zamowienie.czy_obecnie_wynajety = True
            nowe_zamowienie.save()

            return redirect('/krotkoterminowy/'+car_type+'/'+auto_id+'/podliczanie')
        else:
            try:
                if(request.user.id == zamowienia.id_usera):
                    return redirect('/krotkoterminowy/'+car_type+'/'+auto_id+'/podliczanie')
                else:
                    messages.info(request, 'Wprowadzono niepoprawny kod lub auto jest już wynajęte! Spróbuj ponownie')
            except:
                messages.info(request, 'Wprowadzono niepoprawny kod lub auto jest już wynajęte! Spróbuj ponownie')
    
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
    
    now_dynamic = datetime.now()
    now_dynamic = make_aware(now_dynamic, timezone=None)
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

def krotkoterminowy_wynajety_zwrot(request,  car_type, auto_id):
    if request.POST:
        if(car_type == "hulajnoga"):
            auto = get_object_or_404(Hulajnoga, id=auto_id)
            rodzaj = "h"
            cena = auto.cena
        else:
            auto = get_object_or_404(Samochod, id=auto_id)
            rodzaj = "s"
            cena = auto.typ_auta.cena
        
        zamowienie = get_object_or_404(Zamowienia, id_pojazdu = auto.id, rodzaj_pojazdu = rodzaj, czy_obecnie_wynajety= True)

        if zamowienie.id_usera == request.user.id:
            zamowienie.czy_obecnie_wynajety = False
            now_dynamic = datetime.now()
            now_dynamic = make_aware(now_dynamic, timezone=None)
            zamowienie.czas_koniec = now_dynamic
            duration = (now_dynamic - auto.czy_wynajety)
            duration_in_s = int(duration.total_seconds())
            zamowienie.kwota = math.ceil(duration_in_s/60) * cena
            zamowienie.save()
            if rodzaj == "s":
                auto.zasieg = auto.zasieg - Decimal.from_float(round((0.08 * math.ceil(duration_in_s/60)), 3)) #8/100 * 60/60
                # zasięg może wyjść float a pole jest decimal
                if auto.zasieg < 11:
                    auto.service = True
            else:
                auto.zasieg = auto.zasieg - Decimal.from_float(round((0.073 *  math.ceil(duration_in_s/60)), 3)) # 70000/(16*60)
                if auto.zasieg < 2:
                    auto.service = True 
            auto.czy_wynajety = None
            auto.save()



    return redirect('/flota/')

def dlugoterminowy_przeglad(request, car_type):
    typ = get_object_or_404(TypAuta, slug=car_type)
    samochody =  Samochod.objects.filter(typ_auta = typ, typ_wynajmu = "d", service=False, czy_wynajety = None)
    miasta = Miasto.objects.all()
    return render(request, 'dlugoterminowy_przeglad.html', {'miasta': miasta,"samochody" : samochody, })

@login_required
def dlugoterminowy_wynajmij(request, car_type, auto_id):
    auto = get_object_or_404(Samochod, id=auto_id)
    typ = get_object_or_404(TypAuta, slug=car_type)
    try:
        user_m = User.objects.get(id= request.user.id)
        user_email_ = user_m.email
    except:
        pass
 
    if request.method == 'POST':
        message = "Imię i Nazwisko: " + request.POST['imie_nazwisko'] + " email: " + request.POST['email'] + " usernaname: " + request.POST['username'] + " Samochód: " + request.POST['samochod'] + " Od: " + request.POST['od'] + " Do: " + request.POST['do']
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
    

def error_404(request):
    return render(request, 'error_404.html')


