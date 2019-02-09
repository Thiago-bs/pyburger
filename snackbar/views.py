#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


@api_view(['POST'])
def buy_snack(snack_id):
    json_snack = json.loads(snack_id.body)
    try:
        sopping_cart = SoppingCart.objects.get(id=int(json_snack['id']))
        sopping_cart.is_buy = True
        sopping_cart.save()
        return JsonResponse(True,safe=False)
    except Exception as e:
        return JsonResponse(False, safe=False)

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
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    for snack in snacks:
        for ingredient in snack.ingredients_list:
            if ingredient.amount > 0:
                snack.price += ingredient.amount * ingredient.value

    return render(request, 'snacks.html', {'snacks':snacks, 'sopping_cart':sopping_cart})

@csrf_exempt
def add_ingredient(request, snack_id):
    snack = get_snack(snack_id)
    ingredients = Ingredient.objects.all()
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    if snack == 0:
        return redirect('/snacks/')
    if request.POST:
        add_snack = snack_from_request(request)

    return render(request, 'add_ingredient_on_burger.html', {'snack': snack, 'ingredients':ingredients})

def promotions(request):
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    return render(request, 'promotions.html', {'sopping_cart':sopping_cart})

@csrf_exempt
def ingredients(request):
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    if request.POST:
        price_lettuce = request.POST.get('input_1', '')
        price_bacon = request.POST.get('input_2', '')
        price_burger = request.POST.get('input_3', '')
        price_egg = request.POST.get('input_4', '')
        price_cheese = request.POST.get('input_5', '')

        lettuce = Ingredient.objects.get(id=1)
        lettuce.value = float(price_lettuce)
        lettuce.save()

        bacon = Ingredient.objects.get(id=2)
        bacon.value = float(price_bacon)
        bacon.save()

        burger = Ingredient.objects.get(id=3)
        burger.value = float(price_burger)
        burger.save()

        egg = Ingredient.objects.get(id=4)
        egg.value = float(price_egg)
        egg.save()

        cheese = Ingredient.objects.get(id=5)
        cheese.value = float(price_cheese)
        cheese.save()
        messages.success(request, 'Alterações realizadas com sucesso!')

    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients':ingredients, 'sopping_cart':sopping_cart})

def shopping_car(request):
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    return render(request, 'shopping_car.html', {'sopping_cart':sopping_cart})

def snack_controll(request):
    sopping_cart = SoppingCart.objects.filter(is_buy=False)
    buy_snacks = SoppingCart.objects.filter(is_buy=True)
    paginator = Paginator(buy_snacks, 10)
    page = request.GET.get('page')
    try:
        buy_snacks = paginator.page(page)
    except PageNotAnInteger:
        buy_snacks = paginator.page(1)
    except EmptyPage:
        buy_snacks = paginator.page(paginator.num_pages)

    return render(request, 'snack_controll.html', {'sopping_cart':sopping_cart, 'buy_snacks': buy_snacks})