from django.db import models


class OpportunityComment(models.Model):
    class Meta:
        verbose_name = 'Opportunity Comment'
        verbose_name_plural = 'Opportunities Comments'

    text = models.CharField(max_length=256)
    opportunity = models.ForeignKey('deals.Deal', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Opportunity Comment #{self.id}"


class ProductComment(models.Model):
    class Meta:
        verbose_name = 'Product Comment'
        verbose_name_plural = 'Products Comments'

    text = models.CharField(max_length=256)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return  f"Product Comment #{self.id}"