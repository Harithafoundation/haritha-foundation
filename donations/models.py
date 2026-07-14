from django.db import models
from accounts.models import User
# Create your models here.

class Donor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pan_number=models.CharField(max_length=20,blank=True)
    donor_type=models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
    
class Project(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    target_amount=models.DecimalField(max_digits=12,decimal_places=2)
    collected_amount=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Donation(models.Model):
    donor=models.ForeignKey(Donor,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.TextField()
    pan_number=models.CharField(max_length=20,blank=True,null=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    razorpay_order_id=models.CharField(max_length=255,blank=True,null=True)
    payment_id=models.CharField(max_length=255,unique=True,blank=True,null=True)
    payment_status=models.CharField(max_length=50,default='PENDING')
    donated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
class Receipt(models.Model):
    donation=models.OneToOneField(Donation,on_delete=models.CASCADE)
    receipt_number=models.CharField(max_length=100,unique=True)
    pdf_file=models.FileField(upload_to='receipts/')
    generated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receipt_number