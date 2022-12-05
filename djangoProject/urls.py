"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Images, name='Images')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='Images')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

import GreenCompare.views

urlpatterns = [
    path('', GreenCompare.views.HomePage),
    path('shop/<int:shop_reference>', GreenCompare.views.detailShop),
    path('shop/', GreenCompare.views.Shops),
    path('products/<int:shop_reference>', GreenCompare.views.Products),
    path('product/<str:product_reference>', GreenCompare.views.ProductDetails),
    path('admin/', admin.site.urls),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', GreenCompare.views.registerPage, name='register')
]
