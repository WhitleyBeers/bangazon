from django.db import models
from .user import User
from .category import Category

class Product(models.Model):
  
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=280)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category_id = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="None", related_name='products')
    date_added = models.DateField(auto_now_add=True)
