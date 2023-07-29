from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.serializers import ProductSerializer
from bangazonapi.models import Product, Order, OrderProduct
from rest_framework.decorators import action


class ProductView(ViewSet):
    """Bangazon Products"""
    def retrieve(self, request, pk):
        """GET request for a single product"""
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def list(self, request):
        """GET request for a list of products"""
        products = Product.objects.all()
        seller = request.query_params.get('seller', None)
        if seller is not None:
            products = products.filter(seller_id = seller)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def addtocart(self, request, pk):
        """post request to add item to cart"""
        
        order = Order.objects.get(id = request.data["orderId"])
        product = Product.objects.get(pk=pk)
        order_product = OrderProduct.objects.create(
            order_id = order,
            product_id = product
        )
        return Response({'message': 'Added to cart'}, status=status.HTTP_201_CREATED)
