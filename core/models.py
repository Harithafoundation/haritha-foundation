from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    EVENT_TYPES=[
        ('Workshop','Workshop'),
        ('Training','Training'),
        ('Seminar','Seminar'),
        ('Career Guidance','Career Guidance'),
        ('Awareness Program','Awareness Program'),
        
    ]
    title = models.CharField(max_length=255)
    event_type=models.CharField(max_length=50,choices=EVENT_TYPES)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=255)
    image=models.ImageField(upload_to='events/',blank=True,null=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
    
class Gallery(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True,null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryMedia(models.Model):

    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE,related_name='media')
    
    image = models.ImageField(upload_to='gallery/images/',blank=True,null=True)

    video = models.FileField(upload_to='gallery/videos/',blank=True,null=True)

    def __str__(self):
        if self.image:
            return f'{self.gallery.title} - Image'
        if self.video:
            return f'{self.gallery.title} - Video'
        return  self.gallery.title