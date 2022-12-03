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


class UserTable(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    date_joined = models.DateTimeField('date_joined')
    email = models.CharField(max_length=200, default='No email')
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username

class Shop(models.Model):


    class Category(models.TextChoices):
        Fruits = 'Fruits'
        Vegetables = 'Légumes'
        Starch = 'Féculents'
        Meat = 'Viande'
        Drinks = 'Boissons'
        ElseFood = 'Autres aliments'
        Others = 'Autres'


    reference_shop = models.CharField(max_length=200, null=False)
    shop_name = models.CharField(max_length=1000, null=False)
    localisation = models.CharField(max_length=1000, null=False)
    category = models.CharField(max_length=100, choices=Category.choices)
    description = models.CharField(max_length=1000, default='No description')
    opening = models.BooleanField()
    reference_product = models.ManyToManyField(Product)


    def __str__(self):
        return self.shop_name
