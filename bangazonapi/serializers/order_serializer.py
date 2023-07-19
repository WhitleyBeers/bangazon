from rest_framework import serializers
from  bangazonapi.models import Order

class OrderSerializer(serializers.ModelSerializer):
    """json serializer for orders"""
    class Meta:
        model = Order
        fields = ('id',
                  'customer_id',
                  'completed',
                  'payment_method',
                  'shipped')
