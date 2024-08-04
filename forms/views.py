from django.shortcuts import render
from .forms import LoginModelForm


# login view for LoginModelForm
def login_view_model_form(request):
    context = {}
    context['form'] = LoginModelForm
    return render(request, 'login.html', context)

