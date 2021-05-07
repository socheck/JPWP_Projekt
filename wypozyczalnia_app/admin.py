from django.contrib import admin

# Register your models here.
# from django.contrib.postgres import fields # if django < 3.1
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Miasto
from .models import Strefa


@admin.register(Miasto)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

# admin.site.register(Strefa)
@admin.register(Strefa)
class YourModelAdmin1(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }