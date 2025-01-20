from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("", views.home, name='home'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog')
]

