from django.forms import ModelForm
from django import forms

from saidia_app.models import *

# make you forms here

class LoginForm(forms.Form):
    email = forms.EmailField()

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class AuthForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class OrphanageForm(ModelForm):
    class Meta:
        model = Orphanage
        fields = ['name','capacity','location', 'x_coordinate', 'y_coordinate']

class OphNeedsForm(ModelForm):
    class Meta:
        model = Orphanage
        fields = ['needs']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['message']
