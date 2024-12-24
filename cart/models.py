from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
   username = models.ForeignKey(User,on_delete=models.CASCADE)
   product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
   product_price = models.IntegerField(default=0)
   product_desc = models.CharField(max_length=200,default='')
   product_image = models.ImageField(upload_to='shop',default='')
   quantity = models.IntegerField(default=1)
   total_price = models.IntegerField(default=0)

   def __str__(self):
      return str(self.username)



    