from django.shortcuts import render, redirect
from django.urls import path
from snackbar.modelo import *
# Create your views here.

def defaultIngrients():
    lettuce = Ingredient(0,"alface", 0.4, 0)
    bacon = Ingredient(1,"Bacon", 2, 0)
    burger = Ingredient(2,"Hambúrguer de carne", 3, 0)
    egg = Ingredient(3,"Ovo", 0.8, 0)
    cheese = Ingredient(4,"Queijo", 1.5, 0)
    ingredients = [lettuce, bacon, burger, egg, cheese]
    return ingredients

def add_default_amount_ingredient(snack, ids_ingredients):
    for ingredient in snack.ingredients_list:
        if ingredient.id in ids_ingredients:
            ingredient.amount = 1
    return snack

def getDefaultSnacks(ingredients):

    x_bacon = Snacks(1,"X-Bacon",  "xbacon-img.jpg" , defaultIngrients())
    x_bacon = add_default_amount_ingredient(x_bacon, [1,2,4])

    x_burger = Snacks(2,"X-Burger", "xburger-img.jpg", defaultIngrients())
    x_burger = add_default_amount_ingredient(x_burger, [2,4])

    x_egg = Snacks(3,"X-Egg","xegg-img.jpg",  defaultIngrients())
    x_egg = add_default_amount_ingredient(x_egg, [3,2,4])

    x_egg_bacon = Snacks(4,"X-Egg Bacon", "xegg-bacon-img.jpg", defaultIngrients())
    x_egg_bacon = add_default_amount_ingredient(x_egg_bacon, [3, 1, 2, 4])

    defaultSnacks = [x_bacon, x_burger, x_egg, x_egg_bacon]
    return defaultSnacks


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