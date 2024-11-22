from django.db import models


class OpportunityComment(models.Model):
    text = models.CharField(max_length=256)
    opportunity = models.ForeignKey('opportunities.Opportunity', on_delete=models.CASCADE, related_name='comments')

class ProductComment(models.Model):
    text = models.CharField(max_length=256)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='comments')
