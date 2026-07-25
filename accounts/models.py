from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
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


class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.user.username} - {self.otp}"
    