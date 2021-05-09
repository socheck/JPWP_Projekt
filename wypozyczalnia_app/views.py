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

from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cena(request):
    return render(request, 'cena.html')

def flota(request):
    return render(request, 'flota.html')

def kontakt(request):
    return render(request, 'kontakt.html')

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

def dlugoterminowyform(request):
    return render(request, 'dlugoterminowyform.html')

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

# @login_required
# def uzupelnijprofil(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfilForm(request.POST, request.FILES, instance=request.user.profile)

#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, 'Informacje zostały zaaktualizowane')
#             return redirect('uzupelnijprofil')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfilForm(instance=request.user.profile)

#     context = {
#         'u_form' : u_form,
#         'p_form' : p_form
#     }
#     return render(request, 'uzupelnijprofil.html', context)


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