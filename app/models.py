from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=100, unique=True)

class Item(models.Model):
    prod_name =models.CharField(max_length=100)
    prod_description = models.CharField(max_length=100)
    #photo = models.CharField(max_length=100)
    min_bid_price =models.CharField(max_length=10)
    end_date_time = models.CharField(max_length=20)