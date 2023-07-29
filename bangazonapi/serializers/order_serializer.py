from rest_framework import serializers
from  bangazonapi.models import Order, OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    """json serializer for products in orders"""
    class Meta:
        model = OrderProduct
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    """json serializer for orders"""
    products = OrderProductSerializer(many=True, read_only=True, source="order_products")
    class Meta:
        model = Order
        fields = ('id',
                  'customer_id',
                  'completed',
                  'payment_method',
                  'shipped',
                  'products')
