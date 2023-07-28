from rest_framework import serializers
from bangazonapi.models import Category, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    """json serializer for categories with related products"""
    
    class Meta:
        model = Product
        fields = ('id',
                  'title')


class CategorySerializer(serializers.ModelSerializer):
    """json serializer for categories"""
    products = ProductCategorySerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id',
                  'label',
                  'products',
                  'product_count')
    
    def get_product_count(self, obj):
        return obj.products.count()
