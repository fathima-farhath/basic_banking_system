from django.db import models

# Create your models here.
class customers(models.Model):
    name=models.CharField( max_length=500)
    email=models.EmailField(max_length=254)
    balance=models.IntegerField()