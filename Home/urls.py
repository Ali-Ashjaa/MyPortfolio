from django.urls import path
from Home import views

urlpatterns = [
     path('', views.index, name='home'),
     path('projects', views.projects, name='projects'),
     path('about', views.about, name='about'),
     # path('services', views.services, name='services'),
     # path('contact', views.contact, name='contact'),

     
]