from django.shortcuts import render, redirect
from django.urls import path
from snackbar.modelo import *
from django.views.decorators.csrf import csrf_exempt
from snackbar.default_snacks_helper import *
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json

@api_view(['POST'])
def get_snack_detail(snack_id):
    json_snack = json.loads(snack_id.body)
    """sopping_cart = SoppingCart.objects.get(id=int(json_snack['id']))
    snack_dict = {
        "name": sopping_cart.name,
        "qtd_lettuce": sopping_cart.amount_lettuce,
        "qtd_bacon":sopping_cart.amount_bacon,
        "qtd_burger": sopping_cart.amount_burger,
        "qtd_egg": sopping_cart.amount_egg,
        "qtd_cheese": sopping_cart.amount_cheese,
        "price": sopping_cart.price
    }"""
    return Response(snack_dict,safe=False)

@api_view(['POST'])
def exclude_snack(snack_id):
    try:
        json_snack = json.loads(snack_id.body)
        sopping_cart = SoppingCart.objects.get(id=int(json_snack['id'])).delete()
        return JsonResponse(True,safe=False)
    except Exception as e:
        return JsonResponse(False,safe=False)

@api_view(["POST"])
def add_to_cart(snack_object):
    json_snack = json.loads(snack_object.body)
    amount_of_ingredients = get_amount_ingredient_in_list(json.loads(json_snack['ingredients']))
    price = get_price_of_snack(amount_of_ingredients)
    try:
        sopping_cart = SoppingCart.objects.create(name_snack= json_snack['snackName'],
            img_snack=json_snack['snackImg'],
            amount_lettuce=amount_of_ingredients['qtd_lettuce'],
            amount_bacon=amount_of_ingredients['qtd_bacon'],
            amount_burger=amount_of_ingredients['qtd_burger'],
            amount_egg=amount_of_ingredients['qtd_egg'],
            amount_cheese=amount_of_ingredients['qtd_cheese'],
            price=price), 
        return JsonResponse(True,safe=False)
    except Exception as e:
        return JsonResponse(False,safe=False)
    
def snacks(request):
    snacks = getDefaultSnacks(defaultIngrients())
    sopping_cart = SoppingCart.objects.all()
    for snack in snacks:
        for ingredient in snack.ingredients_list:
            if ingredient.amount > 0:
                snack.price += ingredient.amount * ingredient.value

    return render(request, 'snacks.html', {'snacks':snacks, 'sopping_cart':sopping_cart})

@csrf_exempt
def add_ingredient(request, snack_id):
    snack = get_snack(snack_id)
    ingredients = Ingredient.objects.all()
    sopping_cart = SoppingCart.objects.all()
    if snack == 0:
        return redirect('/snacks/')
    if request.POST:
        add_snack = snack_from_request(request)

    return render(request, 'add_ingredient_on_burger.html', {'snack': snack, 'ingredients':ingredients})

def promotions(request):
    sopping_cart = SoppingCart.objects.all()
    return render(request, 'promotions.html', {'sopping_cart':sopping_cart})

@csrf_exempt
def ingredients(request):
    sopping_cart = SoppingCart.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients':ingredients, 'sopping_cart':sopping_cart})

def shopping_car(request):
    sopping_cart = SoppingCart.objects.all()
    return render(request, 'shopping_car.html', {'sopping_cart':sopping_cart})