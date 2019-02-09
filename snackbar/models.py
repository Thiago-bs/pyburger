from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="Nome do Ingrediente")
    value =  models.FloatField(null=True, verbose_name="Valor do Ingrediente")
    category = models.IntegerField(null=True, verbose_name="Categoria do ingrediente 1-Alface | 2-Bacon | 3-Hambúrguer de carne | 4-Ovo | 5-Queijo")
   

class SoppingCart(models.Model):
    name_snack = models.CharField(max_length=255, null=False, verbose_name="Nome do Ingrediente")
    img_snack = models.CharField(max_length=255, null=False, verbose_name="foto do lanche")
    amount_lettuce = models.IntegerField(null=False, verbose_name="Quantidade de alface")
    amount_bacon = models.IntegerField(null=False, verbose_name="Quantidade de Bacon")
    amount_burger = models.IntegerField(null=False, verbose_name="Quantidade de Hambúguer de carne")
    amount_egg = models.IntegerField(null=False, verbose_name="Quantidade de ovo")
    amount_cheese = models.IntegerField(null=False, verbose_name="Quantidade de queijo")
    price = models.FloatField(null=True, verbose_name="Valor do lanche")
