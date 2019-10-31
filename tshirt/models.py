from django.db import models
from django.contrib.auth.models import User


class Tshirt(models.Model):
    size = models.CharField(max_length=10)
    image = models.ImageField()
    gender = models.CharField(max_length=10) 

    def __str__(self):
        return self.size

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user
