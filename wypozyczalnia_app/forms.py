from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django_json_widget.widgets import JSONEditorWidget
from .models import Miasto
from .models import Strefa
from .models import Oddzial
from .models import Samochod
from .models import Hulajnoga
from .models import Profil
from django import forms



class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50 ) # Required
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

class YourForm(forms.ModelForm):
    class Meta:
        model = Oddzial

        fields = ('pozycja',)

        widgets = {
            'pozycja': JSONEditorWidget
        }

class YourForm(forms.ModelForm):
    class Meta:
        model = Samochod

        fields = ('pozycja',)

        widgets = {
            'pozycja': JSONEditorWidget
        }

class YourForm(forms.ModelForm):
    class Meta:
        model = Hulajnoga

        fields = ('pozycja',)

        widgets = {
            'pozycja': JSONEditorWidget
        }


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class UserUpdateForm(UserChangeForm):
    email = forms.EmailField() # Required


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    # def save(self, commit=True):
    #     user = super(UserUpdateForm, self).save(commit=False)
    #     password = self.cleaned_data["password"]
    #     if password:
    #         user.set_password(password)
    #     if commit:
    #         user.save()
    #     return user

class ProfilForm(forms.ModelForm):

    class Meta:
        model = Profil
        fields = ['telefon', 'karta', 'pj_img']