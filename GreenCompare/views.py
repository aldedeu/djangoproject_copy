import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import redirect
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from .models import Product, Shop, UserLocation

def Products(request, shop_reference):
    display_products = []
    for products in Shop.objects.get(id=shop_reference).reference_product.all():
        display_products.append(products)

    template = loader.get_template('Display_products.html')
    context = {'display_products': display_products, 'shop_reference': shop_reference}
    return HttpResponse(template.render(context, request))

def ProductDetails(request, product_reference):
    details = Product.objects.get(id=product_reference)

    template = loader.get_template('Product_details.html')
    context = {'details': details}
    return HttpResponse(template.render(context, request))

def HomePage(request):
    template = loader.get_template("HomePage.html")
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login')
def Shops(request):
    ##Si un utilisateur est connecté et qu'il a une localisation, affiche en premier les magasins qu'il y a à la même localisation
    if request.user is not None and request.user.is_authenticated and hasattr(request.user, 'userlocation'):
        display_shops = []
        shops = Shop.objects.filter(localisation__iexact=request.user.userlocation.location)
        for shop in shops:
            display_shops.append(shop)
        ##Le ~Q (de django.db.models) permet d'inverser une condition de filtrage
        to_append = Shop.objects.filter(~Q(localisation__iexact=request.user.userlocation.location))
        for shop in to_append:
            display_shops.append(shop)
    else:
        display_shops = Shop.objects.all()
    template = loader.get_template("Display_shops.html")
    context = {'display_shops': display_shops}

    return HttpResponse(template.render(context, request))


def detailShop(request, shop_reference):
    details = Shop.objects.get(id=shop_reference)
    print(details.reference_product.count())
    if details.reference_product.count() <= 0:
        products_in_shop = None
    else:
        products_in_shop = 'f'

    template = loader.get_template("Detail_shop.html")
    context = {'details': details, 'products_in_shop': products_in_shop}
    return HttpResponse(template.render(context, request))

def registerPage(request):
    context = {}
    if request.method == 'GET':
        template = loader.get_template("accounts/register.html")
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        post = request.POST.copy()
        post['date_joined'] = datetime.date.today()
        request.POST = post
        form = CreateUserForm(request.POST)
        print(form.fields)
        if form.is_valid():
            location = form.cleaned_data['location']
            user = form.save()
            UserLocation.objects.create(user=user, location=location)
            login(request, user)
            return redirect('/')
