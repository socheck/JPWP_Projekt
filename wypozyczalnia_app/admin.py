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

admin.site.register(Oddzial)
admin.site.register(TypAuta)
admin.site.register(Samochod)
admin.site.register(Hulajnoga)

admin.site.register(Profil)
