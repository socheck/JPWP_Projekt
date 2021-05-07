from django.contrib import admin

# Register your models here.

from .models import Miasto
from .models import Strefa

admin.site.register(Strefa)
admin.site.register(Miasto)