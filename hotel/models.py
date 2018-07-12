from django.db import models

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    location_description=models.CharField(max_length=250)
    quality=models.CharField(max_length=25)
    wifi=models.BooleanField(default=True)
    price= models.IntegerField(blank=True,null=True)
    hotel_website_price=models.IntegerField(blank=True,null=True)
    makemytrip_price=models.IntegerField(blank=True,null=True)
    reviews = models.IntegerField(blank=True,null=True)
    others_price=models.IntegerField(blank=True,null=True)
    num_stars = models.IntegerField(blank=True,null=True)
    image= models.ImageField(upload_to='hotel_image',blank=True)

    def __str__(self):
        return self.name
