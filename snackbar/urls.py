from django.contrib import admin
from django.urls import path, include
from snackbar import views

urlpatterns = [
    path('' , views.index),
    path('snacks/', views.snacks)
]
