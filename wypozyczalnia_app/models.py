from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import datetime
# Create your models here.

# funkcja do pobierania obrazku
def path_typ_auta_ilustracja(instance, filename):
    upload_to = 'static/images/typ_auta'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_hulajnogi_img(instance, filename):
    upload_to = 'static/images/hulajnogi_img'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_auta_img(instance, filename):
    upload_to = 'static/images/auta_img'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_hulajnogi_ilustracja(instance, filename):
    upload_to = 'static/images/ilustracja_hulajnogi'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_kodQR_auto(instance, filename):
    upload_to = 'static/images/kodyQR_auta'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_kodQR_hulajnogi(instance, filename):
    upload_to = 'static/images/kodyQR_hulajnogi'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_prawa_jazdy(instance, filename):
    upload_to = 'static/images/prawa_jazdy'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Miasto(models.Model):
    nazwa = models.CharField(max_length=50)
    pozycja = models.JSONField(blank = False, null = False)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name_plural = "Miasta"
        verbose_name = "Miasto"

rodzaje_stref = [
    ('h', 'hulajnogowa'),
    ('s', 'samochodowa'),
]
class Strefa(models.Model):
    rodzaj = models.CharField(max_length=50, choices=rodzaje_stref, default="h")
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)
    lista_pozycji = models.JSONField(blank = False, null = False, default= {})

    def __str__(self):
        return str(self.miasto) + " strefa: " + self.rodzaj
        
    class Meta:
        verbose_name_plural = "Strefy"
        verbose_name = "Strefa"

class Oddzial(models.Model):
    pozycja = models.JSONField(blank = False, null = False)
    adres = models.CharField(max_length=100, blank = False, null = False)
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.adres)
        
    class Meta:
        verbose_name_plural = "Oddziały"
        verbose_name = "Oddział"

class TypAuta(models.Model):
    nazwa = models.CharField(max_length=100, blank = False, null = False)
    grafika = models.ImageField(upload_to=path_typ_auta_ilustracja, max_length=100, null=False, blank=False)
    cena = models.DecimalField( max_digits=8, decimal_places=2,  null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=100, null = True)

    def __str__(self):
        return self.nazwa
        
    class Meta:
        verbose_name_plural = "Typy samochodów"
        verbose_name = "Typ samochodu"

rodzaje_paliwa = [
    ('b', 'benzyna'),
    ('d', 'diesel'),
    ('e', 'elektryczny'),
    ('h', 'hybryda'),
    ('g', 'LPG'),
]
rodzaj_skrzyni = [
    ('a', 'automatyczna'),
    ('m', 'manualna'),
]
rodzaj_wynamu = [
    ('d', 'długoterminowy'),
    ('k', 'krótkoterminowy'),
]
class Samochod(models.Model):
    pozycja = models.JSONField(blank = False, null = False)
    kolor = models.CharField(max_length=40)
    marka = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    moc = models.DecimalField( max_digits=8, decimal_places=1,  null=False, blank=False)
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)
    nr_rejestracyjny = models.CharField(max_length=8, blank = False, null = False)
    paliwo = models.CharField(max_length=50, choices=rodzaje_paliwa, default="b")
    typ_auta = models.ForeignKey(TypAuta, on_delete=models.CASCADE)
    wyposazenie = models.CharField(max_length=200, blank= True, null = True)
    skrzynia_biegow = models.CharField(max_length=30, choices=rodzaj_skrzyni, default="m")
    opis = models.CharField(max_length=500, blank= True, null = True)
    image = models.ImageField(upload_to=path_auta_img, max_length=100, null=False, blank=False)
    typ_wynajmu = models.CharField(max_length=30, choices=rodzaj_wynamu, default="d")  
    czy_wynajety = models.DateTimeField(auto_now=False, auto_now_add=False, default= None, null = True, blank = True) 
    zasieg = models.DecimalField( max_digits=8, decimal_places=3,  null=False, blank=False) 
    service = models.BooleanField(default = False)
    kodQR = models.ImageField(upload_to=path_kodQR_auto, max_length=100, null=False, blank=False)
    kod = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nr_rejestracyjny + " " + self.marka + " " + self.model

    class Meta:
        verbose_name_plural = "Samochody"
        verbose_name = "Samochód"

class Hulajnoga(models.Model):
    pozycja = models.JSONField(blank = False, null = False)
    miasto = models.ForeignKey(Miasto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_hulajnogi_img, max_length=100, null=False, blank=False)
    cena = models.DecimalField( max_digits=8, decimal_places=2,  null=False, blank=False)
    nr_identyfikacyjny = models.DecimalField( max_digits=8, decimal_places=0,  null=False, blank=False)
    czy_wynajety = models.DateTimeField(auto_now=False, auto_now_add=False, default= None, null = True, blank = True) #może się wywalić tutaj
    zasieg = models.DecimalField( max_digits=6, decimal_places=3,  null=False, blank=False) #obliczany na podstawie przejechanych minut razy mnożnik zużycia (odejmujemy od poprzedniego stanu)
    service = models.BooleanField(default = False) #zmieniany gdy za mało paliwa[zasięg jest odpowiednio niski] (trzeba to ukryć)
    kodQR = models.ImageField(upload_to=path_kodQR_hulajnogi, max_length=100, null=False, blank=False)
    kod = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return  "Hulajnoga TX300 " + str(self.nr_identyfikacyjny)

    class Meta:
        verbose_name_plural = "Hulajnogi"
        verbose_name = "Hulajnoga"

rodzaj_pojazdu = [
    ('h', 'hulajnoga'),
    ('s', 'samochód'),
]
class Zamowienia(models.Model):

    id_usera = models.IntegerField(null = False, blank = False)
    kwota = models.DecimalField( max_digits=8, decimal_places=2,  null=True, blank=True, default= None)
    nr_karty = models.CharField(max_length=16, blank=True, null = True)
    rodzaj_pojazdu = models.CharField(max_length=30, choices=rodzaj_pojazdu, default="s")
    # robimy tylko krótkoterminowy więc chyba nie trzeba dodatkowego pola
    typ_wynajmu = models.CharField(max_length=30, choices=rodzaj_wynamu, default="k")
    id_pojazdu = models.IntegerField(null = False, blank = False)
    czas_startu = models.DateTimeField(auto_now=False, auto_now_add=False, default= None, null = False, blank = False)
    czas_koniec = models.DateTimeField(auto_now=False, auto_now_add=False, default= None, null = True, blank = True)
    czy_obecnie_wynajety =  models.BooleanField(default = True)


    def __str__(self):
        return  "Zamowienie: " + str(self.id) 

    class Meta:
        verbose_name_plural = "Zamówienia"
        verbose_name = "Zamówienie"




class Profil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    telefon = models.CharField(max_length=9, blank=True, null = True)
    karta = models.CharField(max_length=40, blank=True, null = True)
    pj_img =  models.ImageField(upload_to=path_prawa_jazdy, max_length=100, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        if created:
            Profil.objects.create(user=instance)
    except:
        pass

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profil.save()
    except:
        pass
