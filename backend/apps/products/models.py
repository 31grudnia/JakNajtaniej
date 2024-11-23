from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f"Product Category #{self.id} - {self.name}"
    

class ProductSubcategory(models.Model):
    class Meta:
        verbose_name = 'Product Subcategory'
        verbose_name_plural = 'Product Subcategories'

    name = models.CharField(max_length=45, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"Product Subcategory #{self.id} - {self.name}"
    

class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=250, unique=True)
    rating = models.IntegerField()
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"Product #{self.id} - {self.name}"
