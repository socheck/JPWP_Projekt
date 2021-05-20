from django.contrib import admin

# Register your models here.
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Miasto
from .models import Strefa
from .models import Oddzial
from .models import TypAuta
from .models import Samochod
from .models import Hulajnoga
from .models import Profil
from .models import Zamowienia



@admin.register(Miasto)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Strefa)
class YourModelAdmin1(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Oddzial)
class YourModelAdmin1(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Samochod)
class YourModelAdmin1(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Hulajnoga)
class YourModelAdmin1(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

admin.site.register(TypAuta)
admin.site.register(Profil)
admin.site.register(Zamowienia)
