from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=20,default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=15000)
    amount_paid = models.IntegerField(default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    date_shipped = models.DateTimeField(blank=True,null=True)
    placed = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'Order - {str(self.order_id)}'
    

class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE , null=True ,blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'Order_item - {str(self.id)}'