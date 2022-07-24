from django.urls import path
from . import views

#This file was created manually to map view functions from this app ("Playground") to the main project folder (project_v). 
#The first string is the url path followed by the function being called when that url is accessed. 

urlpatterns = { 
    path('', views.playground_home),
    path('hello/', views.say_hello),
}