from rest_framework import serializers
from bangazonapi.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """json serializer for categories"""
    class Meta:
        model = Category
        fields = ('id',
                  'label')
