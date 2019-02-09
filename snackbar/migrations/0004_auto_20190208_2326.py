# Generated by Django 2.1.5 on 2019-02-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackbar', '0003_soppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='soppingcart',
            name='price',
            field=models.FloatField(null=True, verbose_name='Valor do lanche'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='value',
            field=models.FloatField(null=True, verbose_name='Valor do Ingrediente'),
        ),
    ]
