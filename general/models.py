from django.db import models

# Create your models here.
class SigninModel(models.Model):
    aid=models.CharField(max_length=120)
    passwd=models.CharField(max_length=80)

class contactModel(models.Model):
    name=models.CharField(max_length=80)
    mob=models.CharField(max_length=40)
    email=models.EmailField(max_length=120)
    msg=models.CharField(max_length=400)


class myregModel(models.Model):
     name=models.CharField(max_length=70)
     course=models.CharField(max_length=70)
     gender= models.CharField(max_length=60)
     mob=models.CharField(max_length=50)
     email=models.CharField(max_length=120)
     passwd=models.CharField(max_length=80)
     add=models.CharField(max_length=120)
     city=models.CharField(max_length=120)




