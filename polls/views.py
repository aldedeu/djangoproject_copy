from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Product, User, Shop

def index(request):
    display_products = Product.objects.all()
    template = loader.get_template('Display_products.html')
    context = {'display_products': display_products}
    return HttpResponse(template.render(context, request))
