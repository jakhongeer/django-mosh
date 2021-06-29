from django.urls import path
from django.contrib import admin
from .views import basic


urlpatterns = [
    path('', basic),
]
