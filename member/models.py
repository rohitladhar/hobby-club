from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse,get_object_or_404
abcstring = RegexValidator(r'^[A-Za-z ]*$', 'Only characters are allowed.')
# Create your models here.
class Application(models.Model):
    objects = models.Manager()
    object=models.Manager()
    username=models.CharField(max_length=25)
    name= models.CharField(max_length=50, validators=[abcstring])
    group=models.CharField(max_length=30,default='club')
    slot=models.CharField(max_length=30,default='club')
    date=models.CharField(max_length=15,default='club')
    phone=models.FloatField()
    status=models.CharField(max_length=15,default='club')

class UserLogin(models.Model):
    objects = models.Manager()
    object=models.Manager()
    username=models.CharField(max_length=25,unique=True)
    password= models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics',default='pics')

class Contactus(models.Model):
    objects = models.Manager()
    object=models.Manager()
    fname=models.CharField(max_length=30,default='club')
    lname=models.CharField(max_length=30,default='club')
    group=models.CharField(max_length=30,default='club')
    email=models.CharField(max_length=30,default='club')
    desc=models.CharField(max_length=1500,default='club')
    phone=models.FloatField()
    
