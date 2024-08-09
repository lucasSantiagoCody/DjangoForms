from .forms import (
    SignUpModelForm, 
    LoginModelForm, 
    SignUpForm,
    LoginForm
    )
from django.shortcuts import render


# login view for LoginModelForm
def login_view_model_form(request):
    context = {}
    context['form'] = LoginModelForm
    return render(request, 'login_model_form.html', context)


def signup_view_model_form(request):
    context = {}
    context['form'] = SignUpModelForm
    return render(request, 'signup_model_form.html')


def signup_view_form(request):
    context = {}
    context['form'] = SignUpForm
    return render(request, 'signup_form.html', context)

