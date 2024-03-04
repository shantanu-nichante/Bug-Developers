"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
   
from .views import base,Signup,Login,home,index,about,service,contact,medicine,Image,arthritis,Asthma,Diabetes,Hypertension,Digestive,info,Anxiet,Skin,Insomnia,Obesity,Allergies


urlpatterns = [
    path('',base,name='base'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('home',home, name='home'),
    path('index',index, name='index'),
    path('about',about, name='about'),
    path('service',service, name='service'),
    path('contact',contact, name='contact'),
    path('arthritis',arthritis,name='arthritis'),
    path('Asthma',Asthma,name='Asthma'),
     path('Anxiet',Anxiet,name='Anxiet'),
    path('Diabetes',Diabetes,name='Diabetes'),
    path('Hypertension',Hypertension,name='Hypertension'),
    path('Digestive',Digestive,name='Digestive'),
    path('Image',Image,name='Image'),
    
    path('Skin',Skin,name='Skin'),
    path('Insomnia',Insomnia,name='Insomnia'),
    path('Obesity',Obesity,name='Obesity'),
    path('Allergies',Allergies,name='Allergies'),
    path('medicine',medicine,name='medicine'),
    path('info',info,name='info'),

]
