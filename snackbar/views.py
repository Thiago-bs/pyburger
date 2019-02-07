from django.shortcuts import render, redirect
from django.urls import path
from snackbar.modelo import *
# Create your views here.

def defaultIngrients():
    lettuce = Ingredient(0,"alface", 0.4, 1)
    bacon = Ingredient(1,"Bacon", 2, 1)
    burger = Ingredient(2,"Hambúrguer de carne", 3, 1)
    egg = Ingredient(3,"Ovo", 0.8, 1)
    cheese = Ingredient(4,"Queijo", 1.5, 1)
    ingredients = [lettuce, bacon, burger, egg, cheese]
    return ingredients

def getDefaultSnacks(ingredients):
    bacon_ingrients = [bacon_ingrient for bacon_ingrient in ingredients if bacon_ingrient.id in [1,2,4] ]
    x_bacon = Snacks(1,"X-Bacon",  "xbacon-img.jpg" , bacon_ingrients)
    
    burger_ingrients = [burger_ingrient for burger_ingrient in ingredients if burger_ingrient.id in [2,4]]
    x_burger = Snacks(2,"X-Burger", "xburger-img.jpg", burger_ingrients )
    
    xegg_ingrients = [xegg_ingrient for xegg_ingrient in ingredients if xegg_ingrient.id in [3,2,4]]
    x_egg = Snacks(3,"X-Egg","xegg-img.jpg",  xegg_ingrients)

    xegg_bacon_ingrients = [xegg_bacon_ingrient for xegg_bacon_ingrient in ingredients if xegg_bacon_ingrient.id in [3,1, 2,4]]
    x_egg_bacon = Snacks(4,"X-Egg Bacon", "xegg-bacon-img.jpg", xegg_bacon_ingrients )
    defaultSnacks = [x_bacon, x_burger, x_egg, x_egg_bacon]

    return defaultSnacks

def count_ingredients(snack):
    dict_ingredients = {}

    return dict_ingredients

def get_snack(id):
    snacks = getDefaultSnacks(defaultIngrients())
    for snack in snacks:
        if snack.id == id:
            return snack
    return 0 

def index(request):
    print('index')
    return render(request, 'index.html')


def snacks(request):
    snacks = getDefaultSnacks(defaultIngrients())
    return render(request, 'snacks.html', {'snacks':snacks})

def add_ingredient(request, snack_id):
    snack = get_snack(snack_id)
    if snack == 0:
        return redirect('/snacks/')
    return render(request, 'add_ingredient_on_burger.html', {'snack': snack})