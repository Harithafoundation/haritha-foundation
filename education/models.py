from django.db import models
from accounts.models import User
from core.models import *
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    education=models.CharField(max_length=200)
    college_name=models.CharField(max_length=200)
    graduation_year=models.IntegerField()
    interested_domain=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class VolunteerTrainer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=255)
    expertise=models.CharField(max_length=255)
    expertise_year=models.IntegerField(default=0)
    teaching_mode=models.CharField(max_length=50)
    status=models.CharField(max_length=20,default='Pending')

    def __str__(self):
        return self.user.username

class TrainingProgram(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    duration_weeks=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    trainer=models.ForeignKey(VolunteerTrainer,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    program=models.ForeignKey(TrainingProgram,on_delete=models.CASCADE)
    enrolled_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='Active')

    def __str__(self):
        return f"{self.student} - {self.program}"

class EventRegistration(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.event.title}"
    
class JobDrive(models.Model):
    company_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    package = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=255)
    last_date = models.DateField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"
    
class JobDriveRegistration(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    job_drive = models.ForeignKey(JobDrive,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    resume=models.FileField(upload_to='resumes/',null=True,blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES=[('Applied','Applied'),('Selected','Selected'),('Rejected','Rejected')]
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='Applied')

    def __str__(self):
        return f"{self.full_name} - {self.job_drive.company_name}"