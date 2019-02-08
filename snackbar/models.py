from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="Nome do Ingrediente")
    value =  models.FloatField(null=True, verbose_name="Valor do lanche")
    category = models.IntegerField(null=True, verbose_name="Categoria do ingrediente 1-Alface | 2-Bacon | 3-Hambúrguer de carne | 4-Ovo | 5-Queijo")
   