from django.contrib import admin

from .models import Product, ProductCategory, ProductSubcategory


admin.site.register([Product, ProductCategory, ProductSubcategory])
