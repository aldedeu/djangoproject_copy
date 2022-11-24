from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

from .models import Product, User, Shop

def Products(request):
    display_products = Product.objects.all()
    template = loader.get_template('Display_products.html')
    context = {'display_products': display_products}
    print(context)
    return HttpResponse(template.render(context, request))


def HomePage(request):
    template = loader.get_template("HomePage.html")
    context = {}
    print(context)
    return HttpResponse(template.render(context, request))

def Shops(request):
    display_shops = Shop.objects.all()
    template = loader.get_template("Display_shops.html")
    context = {'display_shops': display_shops}
    print(context)
    return HttpResponse(template.render(context, request))

def LogIn(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

    else:
        print("Invalid login, please try again")
