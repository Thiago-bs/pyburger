from django.test import TestCase
from snackbar.default_snacks_helper import * 
from snackbar.modelo import *
from snackbar.models import * 

# Create your tests here.
class TestSnacks(TestCase):
    def test_create_defaul_snack(self):
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)
        snacks = getDefaultSnacks(defaultIngrients())
        for snack in snacks:
            if snack.name_snack not in ['X-Bacon', 'X-Burger', 'X-Egg', 'X-Egg Bacon']:
                self.fail()


    def test_amount_ingredient_on_list(self):
        list_ingredients = ['Alface', 'Bacon', 
            'Hambúrguer de carne',
            'Ovo','Queijo', 'Bacon', 'Hambúrguer de carne', 'Hambúrguer de carne', 'Alface'] 
        ditc_amount_ingredient = get_amount_ingredient_in_list(list_ingredients)
        self.assertEqual(2, ditc_amount_ingredient['qtd_lettuce'])
        self.assertEqual(2, ditc_amount_ingredient['qtd_bacon'])
        self.assertEqual(3, ditc_amount_ingredient['qtd_burger'])
        self.assertEqual(1, ditc_amount_ingredient['qtd_egg'])
        self.assertEqual(1, ditc_amount_ingredient['qtd_cheese'])

    def test_price_of_snacks_promotion_light(self):
        # amount of ingredients 
        # Alface - 2, Hambúrguer - 3, Queijo - 1, Ovo - 1
        #total without promotion = (0.4 * 2 )+ (3 * 2) + (0.8 * 1 )+ (1.5 * 1) = 9.10
        #10% percent discount = 0.91
        #price result = 8.19
        list_ingredients_on_snack = ['Alface', 
            'Hambúrguer de carne', 'Ovo',
            'Queijo',
            'Hambúrguer de carne', 'Alface']
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)
        ditc_amount_ingredient = get_amount_ingredient_in_list(list_ingredients_on_snack)
        price = get_price_of_snack(ditc_amount_ingredient)
        self.assertEqual(8.19, round(price,2))

    def test_price_of_snacks_promotion_muita_carne(self):
        # amount of ingredient  
        # Alface - 2, Hambúrguer - 3, Bacon-6, Queijo - 1, Ovo - 1
        # total without promotion = (0.4 * 2) + (3 * 3) + (2 * 6) +  (1.5 * 1) + (0.8 * 1) = 24,10
        # beef discounts = 3 + 4 = 7 
        # price result = 17,1
        list_ingredients_on_snack = ['Alface', 
            'Hambúrguer de carne', 'Ovo',
            'Queijo','Hambúrguer de carne'
            'Bacon', 'Bacon', 'Bacon','Bacon',
            'Bacon','Bacon',
            'Hambúrguer de carne', 'Alface']
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)
        ditc_amount_ingredient = get_amount_ingredient_in_list(list_ingredients_on_snack)
        price = get_price_of_snack(ditc_amount_ingredient)
        self.assertEqual(17.10, round(price,2))

    def test_price_of_snacks_muito_queijo(self):
        # amount of ingredient 
        # Alface - 1, Hambúrguer - 1, Bacon-1, Queijo - 6, Ovo - 1
        # total without promotion = (0.4 * 1) + (3 * 1) + (2 * 1) +  (1.5 * 6) + (0.8 * 1) = 15,20
        # cheese discounts = 3
        # price result = 12,20
        list_ingredients_on_snack = ['Alface', 'Ovo','Queijo','Hambúrguer de carne', 
            'Bacon','Queijo', 'Queijo', 'Queijo', 'Queijo', 'Queijo']
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)
        ditc_amount_ingredient = get_amount_ingredient_in_list(list_ingredients_on_snack)
        price = get_price_of_snack(ditc_amount_ingredient)
        self.assertEqual(12.20, round(price,2))

    def test_price_of_snacks_all_disconts(self):
        # amount of ingredient 
        # Alface - 1, Hambúrguer - 9, Bacon-0, Queijo - 6, Ovo - 1
        # total without promotion = (0.4 * 1) + (3 * 9) +  (1.5 * 6) + (0.8 * 1) = 34,20
        # cheese discounts = 3
        # beef discounts = 6
        #10% percent discount = 2.52
        # price result = 22.68
        
        list_ingredients_on_snack = ['Alface', 'Ovo','Queijo','Hambúrguer de carne', 
            'Queijo', 'Queijo', 'Queijo', 'Queijo', 'Queijo', 'Hambúrguer de carne', 
            'Hambúrguer de carne', 'Hambúrguer de carne', 'Hambúrguer de carne', 'Hambúrguer de carne',
            'Hambúrguer de carne', 'Hambúrguer de carne', 'Hambúrguer de carne']

        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)
        ditc_amount_ingredient = get_amount_ingredient_in_list(list_ingredients_on_snack)
        price = get_price_of_snack(ditc_amount_ingredient)
        self.assertEqual(22.68, round(price,2))