from django.urls import path, include
from . import views

#app_name = 'nigtech'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('team/', views.team, name='team'),
    path('request-a-quote/', views.contact, name='contact'),
    path('digital-markerter-sign-up/', views.DMSignUpView, name='dm_sign_up'),
    ]