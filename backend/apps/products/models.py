from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=45)

class ProductSubcategory(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='subcategories')

class Product(models.Model):
    name = models.TextField()
    rating = models.IntegerField()
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE, related_name='products')
