from django.db import models

# Create your models here.
class HeroSlider(models.Model):
    offer_name = models.CharField(max_length=300)
    offer_title = models.TextField()  
    offer_price = models.CharField(max_length=100)
    offer_product_link = models.TextField()  
    offer_image = models.FileField(upload_to="media/sliderImage/") 

    def __str__(self):
        return self.offer_title
