"""
URL configuration for djcalculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.AdditionView.as_view()),
    path('subtraction/', views.Subtraction.as_view()),
    path('Multiplication/', views.Multiplication.as_view()),
    path('Division/', views.Division.as_view()),
    path('Modulus/', views.Modulus.as_view()),
    path('BMI/', views.BMI.as_view()),
    path('age/', views.Age.as_view()),
    path('percentage/', views.PercentageView.as_view()),
    path('area/', views.AreaView.as_view()),
    path('SI/', views.SimpleInterest.as_view())
]
