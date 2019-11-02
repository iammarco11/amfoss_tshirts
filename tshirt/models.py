from django.db import models
from django.contrib.auth.models import User


class Tshirt(models.Model):
    name = models.CharField(max_length=255,default='amfoss')
    slug = models.CharField(max_length=255, default='amfoss')
    image = models.FileField(null=True,blank=True)
    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user

class Cart(models.Model):
    product = models.OneToOneField(Tshirt, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.FloatField()
    gender = models.CharField(max_length=2)
    size = models.CharField(max_length=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name + str(self.quantity)


