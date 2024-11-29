from django.urls import path
from profiles_api import views
from django.shortcuts import render


urlpatterns = [
    
    path('hello' , views.Hello_Api.as_view()),
    path('calculator/', views.calculator, name='calculator'),
    path('test/', lambda request: render(request, 'test.html')),



]
