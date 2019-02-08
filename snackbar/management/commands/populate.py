from django.core.management.base import BaseCommand, CommandError
from snackbar.models import *

class Command(BaseCommand):
    help = 'Populate initial snacks'

    
    def create_ingredient(snack):
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4)
        
    
    def handle(self, *args, **options):
        ingredient_lettuce = Ingredient.objects.create(name="Alface", value=0.4, category=1)
        ingredient_bacon = Ingredient.objects.create(name="Bacon", value=2, category=2)
        ingredient_burger = Ingredient.objects.create(name="Hambúrguer de carne", value=3, category=3)
        ingredient_egg = Ingredient.objects.create(name="Ovo", value=0.8, category=4)
        ingredient_cheese = Ingredient.objects.create(name="Queijo", value=1.5, category=5)