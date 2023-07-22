from rest_framework import serializers
from bangazonapi.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """json serializer for products"""
    class Meta:
        model = Product
        fields = ('id',
                  'seller_id',
                  'title',
                  'description',
                  'quantity',
                  'price',
                  'category_id',
                  'date_added')
        depth = 1
