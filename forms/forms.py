from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class SignUpModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()


class LoginModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

