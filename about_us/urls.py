from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutUs, name='about-us'),
]