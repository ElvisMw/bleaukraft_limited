""" branding urls """
from django.urls import path
from . import views

app_name = 'branding'

urlpatterns = [
    path('', views.home, name='home'),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('landingpage1/', views.landingpage1, name='landingpage1'),

]