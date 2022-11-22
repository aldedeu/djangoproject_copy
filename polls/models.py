from django.db import models
import datetime
from django.utils import timezone

class Product(models.Model):

    class EcoScore(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'

    class Category(models.TextChoices):
        Fruits = 'Fruits'
        Vegetables = 'Légumes'
        Starch = 'Féculents'
        Meat = 'Viande'
        Drinks = 'Boissons'
        ElseFood = 'Autres aliments'
        Others = 'Autres'


    reference = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0, null=False)
    productor_name = models.CharField(max_length=200, default='No data for the productor name')
    entitled = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, choices=Category.choices)
    eco_score = models.CharField(max_length=1, choices=EcoScore.choices)

    def __str__(self):
        return self.reference

    #coucou

class User(models.Model):
    ncli = models.IntegerField(null=False)
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=1000, null=False)
    email = models.CharField(max_length=200, default='No email')
    number = models.IntegerField(default=0)
    reference_product = models.ManyToManyField(Product)

    def __int__(self):
        return self.ncli

class Shop(models.Model):
    reference_shop = models.CharField(max_length=200, null=False)
    shop_name = models.CharField(max_length=1000, null=False)
    localisation = models.CharField(max_length=1000, null=False)
    category = models.CharField(max_length=1000, default='No category')
    description = models.CharField(max_length=1000, default='No description')
    opening = models.BooleanField()
    reference_product = models.ManyToManyField(Product)


    def __str__(self):
        return self.shop_name
