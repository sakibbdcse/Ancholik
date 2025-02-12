from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    product_img = models.ImageField(upload_to='product_image')
    new_price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    descriptions = models.TextField(max_length=250)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name