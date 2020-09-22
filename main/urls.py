from django.urls import path, include
from . import views

#app_name = 'nigtech'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('request-a-quote/', views.contact, name='contact'),

    ]