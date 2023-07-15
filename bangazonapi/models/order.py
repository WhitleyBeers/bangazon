from django.db import models
from .user import User

class Order(models.Model):
  
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)
    shipped = models.BooleanField(default=False)
