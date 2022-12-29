from django.urls import path
from . import views

urlpatterns = [
    path('', views.CookiePolicy, name='cookie-policy'),
]
