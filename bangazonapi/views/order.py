from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.serializers import OrderSerializer
from bangazonapi.models import Order


class OrderView(ViewSet):
    """Bangazon Orders"""
    def retrieve(self, request, pk):
        """GET request for a single order"""
        pass
    
    def list(self, request):
        """GET request for a list of orders"""
        orders = Order.objects.all()
        user = request.META["HTTP_AUTHORIZATION"]
        orders = orders.filter(customer_id = user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """POST request to create an order"""
        pass
      
    def update(self, request, pk):
        """PUT request to update an order"""
        pass
      
    def destroy(self, request, pk):
        """DELETE request to destroy an order"""
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'message': 'Order deleted'}, status=status.HTTP_204_NO_CONTENT)
