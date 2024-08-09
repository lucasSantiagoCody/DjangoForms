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


class SignUpWidgetForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

