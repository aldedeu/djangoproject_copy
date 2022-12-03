from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, CreateUserForm


from .models import Product, UserTable, Shop

def Products(request, shop_reference, product_reference):
    display_products = []
    for products in Shop.product_reference:
        display_products.append(products)

    template = loader.get_template('Display_products.html')
    context = {'display_products': display_products, 'shop_reference': shop_reference, 'product_reference': product_reference}
    return HttpResponse(template.render(context, request))

def HomePage(request):
    template = loader.get_template("HomePage.html")
    context = {}
    return HttpResponse(template.render(context, request))

def Shops(request):
    display_shops = Shop.objects.all()
    template = loader.get_template("Display_shops.html")
    context = {'display_shops': display_shops}

    return HttpResponse(template.render(context, request))

def detailShop(request, shop_reference):
    details = Shop.objects.get(reference_shop=shop_reference)

    if details.reference_product == "GreenCompare.Product.None":
        products_in_shop = None
    else:
        products_in_shop = 'f'

    template = loader.get_template("Detail_shop.html")
    context = {'details': details, 'products_in_shop': products_in_shop}
    return HttpResponse(template.render(context, request))

def loginPage(request):

    template = loader.get_template("accounts/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    template = loader.get_template("accounts/register.html")
    context = {'form': form}
    return HttpResponse(template.render(context, request))
