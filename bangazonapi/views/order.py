from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.serializers import OrderSerializer, UserSerializer
from bangazonapi.models import Order, User
from rest_framework.decorators import action, api_view
from django.db.models import Q

class OrderView(ViewSet):
    """Bangazon Orders"""
    def retrieve(self, request, pk):
        """GET request for a single order"""
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """GET request for a list of orders"""
        orders = Order.objects.all()
        user = request.META["HTTP_AUTHORIZATION"]
        orders = orders.filter(customer_id = user, completed=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """POST request to create an order"""
        user = User.objects.get(id=request.META["HTTP_AUTHORIZATION"])
        order = Order.objects.create(
            customer_id = user,
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """PUT request to update an order"""
        order = Order.objects.get(pk=pk)
        order.completed = True
        order.payment_method = request.data['paymentMethod']
        order.shipped = True
        order.save()
        return Response({'message': 'Order updated'}, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        """DELETE request to destroy an order"""
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'message': 'Order deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @api_view(['GET'])
    def seller_order_history(request):
        target_seller_id = request.META["HTTP_AUTHORIZATION"]
        orders_with_products_from_seller = Order.objects.filter(
            order_products__product_id__seller_id = target_seller_id
        ).distinct()
        serializer = OrderSerializer(orders_with_products_from_seller, many=True)
        return Response(serializer.data)
