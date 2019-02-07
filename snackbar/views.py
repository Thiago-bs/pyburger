from django.shortcuts import render, redirect
from django.urls import path
from snackbar.modelo import *
from django.views.decorators.csrf import csrf_exempt
from snackbar.default_snacks_helper import *
# Create your views here.



def index(request):
    print('index')
    return render(request, 'index.html')


def snacks(request):
    snacks = getDefaultSnacks(defaultIngrients())
    return render(request, 'snacks.html', {'snacks':snacks})

@csrf_exempt
def add_ingredient(request, snack_id):
    snack = get_snack(snack_id)
    if snack == 0:
        return redirect('/snacks/')
    if request.POST:
        add_snack = snack_from_request(request)

    return render(request, 'add_ingredient_on_burger.html', {'snack': snack})

def promotions(request):
    return render(request, 'promotions.html')