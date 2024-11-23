from django.contrib import admin

from .models import ProductComment, OpportunityComment


admin.site.register([ProductComment, OpportunityComment])

