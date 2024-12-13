from django.urls import path , include
from profiles_api import views
from django.shortcuts import render
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('userapi', views.UserProfileViewSet, basename='UserProfileViewSet')


urlpatterns = [
    
    path('hello' , views.Hello_Api.as_view()),
    path('', include(router.urls))




]
