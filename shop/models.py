from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=30)
    product_type = models.CharField(max_length=30)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images',default='')
    details = models.CharField(max_length=30000,default='') 
    
    def __str__(self):
        return self.product_name
    
