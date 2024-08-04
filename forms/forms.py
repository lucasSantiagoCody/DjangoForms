from django.forms import forms
from django.contrib.auth.models import User



class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

