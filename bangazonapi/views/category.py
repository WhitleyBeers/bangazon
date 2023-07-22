from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.serializers import CategorySerializer
from bangazonapi.models import Category


class CategoryView(ViewSet):
    """Categories"""
    def retrieve(self, request, pk):
        """GET request for a single category"""
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
      
    def list(self, request):
        """GET request for a list of categories"""
        pass
