from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    bio= models.TextField(max_length=250,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
   
    class StatusChoices(models.TextChoices):
        DRIVER = 'Driver', 'Driver'
        RIDER = 'Rider', 'Rider'

    status = models.CharField(max_length=10,choices=StatusChoices.choices, default=StatusChoices.RIDER)

    def __str__(self):
        return self.username



class Room(models.Model):
    name= models.TextField(max_length=100,unique=True)
    def __str__(self):
        return self.name
    
class UserMessages(models.Model):
    room= models.ForeignKey(Room,on_delete=models.CASCADE,default=3)
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    text= models.TextField(max_length=500,null=False,blank=False)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message from {self.user.username} in {self.room.name}: {self.text}"

class UserListing(models.Model):
    class TypeChoices(models.TextChoices):
        PAID = 'Paid', 'Paid'
        HITCHHIKE = 'Hitchhike', 'Hitchhike'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=False, blank=False)
    ride_type = models.CharField(max_length=15, choices=TypeChoices.choices, default=TypeChoices.HITCHHIKE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Listing by {self.user.username}: {self.text} ({self.ride_type})"
