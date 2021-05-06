from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
    form = UserCreationForm()
    context = {'form':form}

    return render(request, 'rejestracja.html', context)