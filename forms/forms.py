from django.forms import ModelForm
from django.contrib.auth.models import User



class SignUpModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']