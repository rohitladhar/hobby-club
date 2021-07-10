from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse,get_object_or_404
abcstring = RegexValidator(r'^[A-Za-z ]*$', 'Only characters are allowed.')
emailstring= RegexValidator(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$','Invalid Email Format')
# Create your models here.

class Records(models.Model):
    objects = models.Manager()
    object=models.Manager()
    username=models.CharField(max_length=25,unique=True)
    password=models.CharField(max_length=50, default='clubs')
    name= models.CharField(max_length=50, validators=[abcstring])
    phone=models.FloatField()
    email=models.CharField(max_length=50, validators=[emailstring])
    date=models.CharField(max_length=25, default='clubs')
    status=models.CharField(max_length=25, default='clubs')
    group=models.CharField(max_length=25, default='clubs')
    slot=models.CharField(max_length=25, default='clubs')
    fees=models.FloatField()
    month=models.CharField(max_length=25, default='jan')
    address=models.CharField(max_length=250, default='clubs')
    
    
class StaffRecords(models.Model):
    objects = models.Manager()
    object=models.Manager()
    username=models.CharField(max_length=25,unique=True)
    name= models.CharField(max_length=50, validators=[abcstring])
    phone=models.FloatField()
    email=models.CharField(max_length=50, validators=[emailstring])
    image=models.ImageField(upload_to='pics')
    joining_date=models.DateField()

class Content(models.Model):
    objects = models.Manager()
    object=models.Manager()
    article=models.CharField(max_length=30,default='club')
    heading=models.CharField(max_length=100,default='club')
    date=models.CharField(max_length=15,default='club')
    group=models.CharField(max_length=30,default='club')
    desc=models.CharField(max_length=2000,default='club')

class Booking(models.Model):
    objects = models.Manager()
    object=models.Manager()
    group=models.CharField(max_length=30)
    booked=models.IntegerField()
    available= models.IntegerField()    
    slot=models.CharField(max_length=25, default='clubs')
    theme=models.CharField(max_length=100, default='clubs')
    date=models.CharField(max_length=15,default='club')