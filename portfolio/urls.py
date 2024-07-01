from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('experience', views.experience, name='experience'),
    path('contact', views.contact, name='contact')
]