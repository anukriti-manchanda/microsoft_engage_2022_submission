from django.db import models

# Create your models here.
class loginDetails(models.Model):
    carNumber=models.CharField(max_length=20)
    phoneNumber=models.CharField(max_length=20)
    def __str__(self):
        return self.carNumber
class location(models.Model):
    latlong=models.CharField(max_length=100,default='Location Not Found')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    time=models.CharField(max_length=30,default='00:00:00')
    
    
