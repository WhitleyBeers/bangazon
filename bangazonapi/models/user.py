from django.db import models

class User(models.Model):
  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    uid = models.CharField(max_length=50)
    registered_on = models.DateField(auto_now_add=True)
    profile_image_url = models.CharField(max_length=260)
    username = models.CharField(max_length=50)
