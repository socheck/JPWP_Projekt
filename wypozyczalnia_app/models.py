from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

import datetime
# Create your models here.

# funkcja do podierania obrazku
def path_rodzaj_auta_ilustracja(instance, filename):
    upload_to = 'static/images/rodzaj_auta'
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


class Miasto(models.Model):
    nazwa = models.CharField(max_length=50)
    # pozycja = models.JSONField(default = {})

    def __str__(self):
        return self.nazwa

