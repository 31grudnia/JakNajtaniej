from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os 

from apps.products.models import ProductCategory, ProductSubcategory, DataPopulationLog


@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):

    if DataPopulationLog.objects.filter(name="initial_population").exists():
        return

    categories = [
        {"name": "Electronics"},
        {"name": "Books"},
        {"name": "Home Appliances"},
        {"name": "Clothing"},
        {"name": "Sports Equipment"},
    ]

    subcategories = [
        {"name": "Smartphones", "category_name": "Electronics"},
        {"name": "Laptops", "category_name": "Electronics"},
        {"name": "Fiction", "category_name": "Books"},
        {"name": "Non-Fiction", "category_name": "Books"},
        {"name": "Kitchen Appliances", "category_name": "Home Appliances"},
        {"name": "Men's Wear", "category_name": "Clothing"},
        {"name": "Women's Wear", "category_name": "Clothing"},
        {"name": "Fitness Equipment", "category_name": "Sports Equipment"},
    ]

    for category_data in categories:
        ProductCategory.objects.get_or_create(name=category_data["name"])

    for subcategory_data in subcategories:
        try:
            category = ProductCategory.objects.get(name=subcategory_data["category_name"])
            ProductSubcategory.objects.get_or_create(name=subcategory_data["name"], category=category)
        except ProductCategory.DoesNotExist:
            print(f"Category '{subcategory_data['category_name']}' not found. Skipping subcategory '{subcategory_data['name']}'")

    DataPopulationLog.objects.create(name="initial_population")