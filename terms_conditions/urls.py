from django.urls import path
from . import views

urlpatterns = [
    path('', views.TermsConditions, name='terms-conditions'),
]
