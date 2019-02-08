from snackbar.modelo import *
from snackbar.models import * 
def defaultIngrients():
    lettuce = Ingredient.objects.get(category=1)
    bacon = Ingredient.objects.get(category=2)
    burger = Ingredient.objects.get(category=3)
    egg = Ingredient.objects.get(category=4)
    cheese = Ingredient.objects.get(category=5)

    lettuce = Ingredient(0,"alface", lettuce.value, 0)
    bacon = Ingredient(1,"Bacon", bacon.value, 0)
    burger = Ingredient(2,"Hambúrguer de carne", burger.value, 0)
    egg = Ingredient(3,"Ovo", egg.value, 0)
    cheese = Ingredient(4,"Queijo", cheese.value, 0)
    ingredients = [lettuce, bacon, burger, egg, cheese]

    return ingredients

def add_default_amount_ingredient(snack, ids_ingredients):
    for ingredient in snack.ingredients_list:
        if ingredient.id in ids_ingredients:
            ingredient.amount = 1
        else:
            ingredient.amount = 0
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

def snack_from_request(request):
    snack_id = request.POST.get('input_id', '')
    snack_name = request.POST.get('input_name', '')
    snack_img = request.POST.get('input_img', '')
    qtd_letture = request.POST.get('input_0', '')
    qtd_bacon = request.POST.get('input_1', '')
    qtd_burger = request.POST.get('input_2', '')
    qtd_egg = request.POST.get('input_3', '')
    qtd_cheese = request.POST.get('input_4', '')

    lettuce = Ingredient(0,"alface", 0.4, int(qtd_letture))
    bacon = Ingredient(1,"Bacon", 2, int(qtd_bacon))
    burger = Ingredient(2,"Hambúrguer de carne", 3, int(qtd_burger))
    egg = Ingredient(3,"Ovo", 0.8, int(qtd_egg))
    cheese = Ingredient(4,"Queijo", 1.5, int(qtd_cheese))
    ingredients = [lettuce, bacon, burger, egg, cheese]

    snack = Snacks(snack_id, snack_name, snack_img, ingredients)
    
    return snack