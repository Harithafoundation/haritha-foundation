from django.core.mail import EmailMessage
from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from donations.models import *
from education.models import *
from core.models import *
import os
from .utils import create_receipt
import razorpay
from django.conf import settings
User=get_user_model()
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')



def programs(request):
    programs=TrainingProgram.objects.filter(is_active=True)
    return render(request,'programs.html',{'programs':programs})


def events(request):
    events=Event.objects.filter(is_active=True)
    jobs=JobDrive.objects.filter(is_active=True)
    return render(request,'events.html',{'events':events,'jobs':jobs})

def gallery(request):
    galleries=Gallery.objects.prefetch_related('media').all()

    for gallery in galleries:
        gallery.first_image=None
        gallery.first_video=None
        for media in gallery.media.all():
            if media.image and not gallery.first_image:
                gallery.first_image=media.image.url
            if media.video and not gallery.first_video:
                gallery.first_video=media.video.url
    return render(request,'gallery.html',{'galleries':galleries})


def contact(request):
    if request.method=='POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),)
        return redirect('contact')
    return render(request,'contact.html')

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(
                request,
                "register.html",
                {"error": "Passwords do not match"}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register.html",
                {"error": "Username already exists"}
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        Student.objects.create(
            user=user,
            education="Not Provided",
            college_name="Not Provided",
            graduation_year=0,
            interested_domain="General"
        )

        return redirect("/login/")

    return render(request, "register.html")

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'Invalid Username or Password'})

    return render(request,'login.html')

def donate(request):
    projects=Project.objects.filter(is_active=True)
    client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        pan_number=request.POST.get('pan_number')
        message=request.POST.get('message')
        project=request.POST.get('project')
        amount=int(request.POST.get('amount'))
        request.session['name']=name
        request.session['email']=email
        request.session['phone']=phone
        request.session['address']=address
        request.session['pan_number']=pan_number
        request.session['message']=message
        request.session['project']=project
        request.session['amount']=amount
        payment=client.order.create({
            'amount':amount*100,
            'currency':'INR',
            'payment_capture':1})
        context={
            'projects':projects,
            'payment':payment,
            'order_id':payment['id'],
            'amount':amount,
            'razorpay_key':settings.RAZORPAY_KEY_ID,
            'name':name,
            'email':email,
            'phone':phone,
            'address':address,
            'pan_number':pan_number,
            'message':message,
            'project':project}
        return render(request,'donate.html',context)
    return render(request,'donate.html',{'projects':projects})

def payment_success(request):
    payment_id = request.GET.get("payment_id")
    order_id = request.GET.get("order_id")

    project = Project.objects.get(id=request.session["project"])

    donation = Donation.objects.create(
        name=request.session["name"],
        email=request.session["email"],
        phone=request.session["phone"],
        address=request.session["address"],
        pan_number=request.session["pan_number"],
        project=project,
        amount=request.session["amount"],
        razorpay_order_id=order_id,
        payment_id=payment_id,
        payment_status="SUCCESS"
    )
    subject='Donation Successful - Haritha Foundation'
    message=f"""
    Dear {donation.name}
    Thank you for supporting Haritha Foundation.
    Your donation has been received successfully.
    Donation Amount: ₹{donation.amount}
    Payment ID: {donation.payment_id}
    Order ID: {donation.razorpay_order_id}
    Regards,
    Haritha Foundation
        """
    email=EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [donation.email],
    )
    filename=f"receipt_{donation.id}.pdf"
    create_receipt(donation,filename)
    email.attach_file(filename)
    email.send(fail_silently=False)
    os.remove(filename)
    context = {
        "payment_id": donation.payment_id,
        "amount": donation.amount,
        "donation": donation,
    }

    return render(request, "payment_success.html", context)

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out Successfully')
    return redirect('home')
    

