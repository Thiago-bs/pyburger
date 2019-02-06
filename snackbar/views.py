from django.shortcuts import render
from django.urls import path
# Create your views here.

def index(request):
    print('index')
    return render(request, 'index.html')

def snacks(request):
    return render(request, 'snacks.html')