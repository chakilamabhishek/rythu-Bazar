import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class farmer(models.Model):
    farmername=models.ForeignKey(User, related_name='farmer_name',on_delete=models.CASCADE)
    cropimage=models.ImageField(blank=True,upload_to = STATIC_DIR,default="")
    cropname=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description = models.TextField()
    Address = models.TextField()
    contactnumb=models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.now)


class inventory(models.Model):
    pass
class reviewfarmer(models.Model):
    created_by = models.ForeignKey(User, related_name='review_farmer',on_delete=models.CASCADE)
    review=models.TextField()
    added_at = models.DateTimeField(default=datetime.datetime.now)

