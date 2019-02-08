from django.shortcuts import render, redirect
from django.urls import path
from snackbar.modelo import *
from django.views.decorators.csrf import csrf_exempt
from snackbar.default_snacks_helper import *
from django.contrib import messages


def snacks(request):
    snacks = getDefaultSnacks(defaultIngrients())
    for snack in snacks:
        for ingredient in snack.ingredients_list:
            if ingredient.amount > 0:
                snack.price += ingredient.amount * ingredient.value

    return render(request, 'snacks.html', {'snacks':snacks})

@csrf_exempt
def add_ingredient(request, snack_id):
    snack = get_snack(snack_id)
    if snack == 0:
        return redirect('/snacks/')
    if request.POST:
        add_snack = snack_from_request(request)

    ingredients = Ingredient.objects.all()

    return render(request, 'add_ingredient_on_burger.html', {'snack': snack, 'ingredients':ingredients})

def promotions(request):
    return render(request, 'promotions.html')

@csrf_exempt
def ingredients(request):
    ingredients = Ingredient.objects.all()
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

        cheese = Ingredient.objects.get(id=1)
        cheese.value = float(price_cheese)
        cheese.save()
        messages.success(request, 'Alterações realizadas com sucesso!')
    return render(request, 'ingredients.html', {'ingredients':ingredients})