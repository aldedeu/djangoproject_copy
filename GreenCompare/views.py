import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, CreateUserForm


from .models import Product, UserTable, Shop

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
    print(request.user)
    template = loader.get_template("HomePage.html")
    context = {}
    return HttpResponse(template.render(context, request))

def Shops(request):
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

def loginPage(request):
    if request.method == 'GET':
        template = loader.get_template("accounts/login.html")
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                print('connecting')
                login(request, user)

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
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
