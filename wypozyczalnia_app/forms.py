from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django_json_widget.widgets import JSONEditorWidget
from .models import Miasto
from .models import Strefa



class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required
    email = forms.EmailField(max_length=50) # Required
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']

class YourForm(forms.ModelForm):
    class Meta:
        model = Strefa

        fields = ('lista_pozycji',)

        widgets = {
            'lista_pozycji': JSONEditorWidget
        }

class YourForm(forms.ModelForm):
    class Meta:
        model = Miasto

        fields = ('pozycja',)

        widgets = {
            'pozycja': JSONEditorWidget
        }