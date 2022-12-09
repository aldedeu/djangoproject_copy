from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

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


    price = models.FloatField(default=0, null=False)
    productor_name = models.CharField(max_length=200, default='No data for the productor name')
    entitled = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, choices=Category.choices)
    eco_score = models.CharField(max_length=1, choices=EcoScore.choices)

    def __str__(self):
        return self.entitled + ' - ' + str(self.id)

class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250)

    def __str__(self):
        return 'user ' + self.user.username + ' with location : ' + self.location

class Shop(models.Model):


    class Category(models.TextChoices):
        Fruits = 'Fruits'
        Vegetables = 'Légumes'
        Starch = 'Féculents'
        Meat = 'Viande'
        Drinks = 'Boissons'
        ElseFood = 'Autres aliments'
        Others = 'Autres'


    shop_name = models.CharField(max_length=1000, null=False)
    localisation = models.CharField(max_length=1000, null=False)
    category = models.CharField(max_length=100, choices=Category.choices)
    description = models.CharField(max_length=1000, default='No description')
    opening = models.BooleanField()
    reference_product = models.ManyToManyField(Product)
    creationDate = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='shop_images/')

    def __str__(self):
        return self.shop_name
