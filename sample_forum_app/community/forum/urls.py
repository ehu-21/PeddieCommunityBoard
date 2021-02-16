from django.contrib import admin
from django.urls import path
from . import views

app_name = "forum"

urlpatterns = [
    path('',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('termsConditions', views.termsAndConditions, name="termsConditions"),
   
    
]
