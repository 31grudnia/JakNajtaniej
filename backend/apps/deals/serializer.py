from rest_framework import serializers

from .models import Deal


class DealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deal
        fields = ['id', 'title', 'description', 'link', 'created_at', 'discount_code']