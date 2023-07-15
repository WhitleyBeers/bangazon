from django.db import models
from .product import Product
from .order import Order

class OrderProduct(models.Model):
  
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
