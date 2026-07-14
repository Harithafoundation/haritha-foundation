from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.username
    
    