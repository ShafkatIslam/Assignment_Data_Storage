from django.contrib.auth.models import Permission, User
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    belong_to = models.CharField(max_length=50,blank=True)
    street = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50,blank=True)
    zip = models.IntegerField(max_length=50,default=0,blank=True)

    def __str__(self):
        return self.first_name
