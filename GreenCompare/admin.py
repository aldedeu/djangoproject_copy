from django.contrib import admin

# Register your models here.
from .models import Product
from .models import UserTable
from .models import Shop


admin.site.register(Product)
admin.site.register(UserTable)
admin.site.register(Shop)

