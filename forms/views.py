from .forms import (
    SignUpModelForm, 
    SignUpForm,
    SignUpWidgetForm,
   
    )
from django.shortcuts import render



def signup_view_model_form(request):
    context = {}
    context['form'] = SignUpModelForm
    return render(request, 'signup_model_form.html')


def signup_view_form(request):
    context = {}
    context['form'] = SignUpForm
    return render(request, 'signup_form.html', context)


def signup_view_widget_form(request):
    context = {}
    context['form'] = SignUpWidgetForm
    return render(request, 'signup_widget_form.html', context)

