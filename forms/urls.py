from django.urls import path
from . import views

urlpatterns = [
    path('login-model-form/', views.login_view_model_form, name='login_model_form_url'),
    path('login-form/', views.login_view_form, name='login_form_url'),
    path('signup-model-form/', views.signup_view_model_form, name='singup_model_form_url'),
    path('signup-form/', views.signup_view_form, name='signup_form_url'),
    path('signup-widget-form/', views.signup_view_widget_form, name='signup_widget_form_url'),


]