from django.contrib.auth.models import User
from django.db import models


class Deal(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    link = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    discount_code = models.CharField(max_length=128, blank=True, null=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)