from django.core.mail import EmailMessage
from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from donations.models import *
from education.models import *
from random import randint
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from accounts.models import *
from core.models import *
import os,random
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
            return render(request, "register.html", {
                "error": "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already exists"
            })

        otp = str(random.randint(100000, 999999))

        request.session["username"] = username
        request.session["email"] = email
        request.session["password"] = password1
        request.session["otp"] = otp

        send_mail(
            subject="Haritha Foundation OTP Verification",
            message=f"Your OTP is {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect("register_otp")

    return render(request, "register.html")

def register_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        if entered_otp == request.session.get("otp"):

            username = request.session.get("username")
            email = request.session.get("email")
            password = request.session.get("password")

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            Student.objects.create(
                user=user,
                education="Not Provided",
                college_name="Not Provided",
                graduation_year=0,
                interested_domain="General"
            )

            request.session.flush()

            return redirect("/login/")

        return render(request, "register_otp.html", {
            "error": "Invalid OTP"
        })

    return render(request, "register_otp.html")

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


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(email=email)

            # Delete previous OTPs
            PasswordResetOTP.objects.filter(user=user).delete()

            # Generate new OTP
            otp = str(randint(100000, 999999))

            PasswordResetOTP.objects.create(
                user=user,
                otp=otp
            )

            # Send email
            subject = "Haritha Foundation - Password Reset OTP"

            message = f"""
Hello {user.first_name or user.username},

Your OTP for resetting your password is:

{otp}

This OTP is valid for 10 minutes.

If you did not request a password reset, please ignore this email.

Regards,
Haritha Foundation
"""

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            request.session["reset_email"] = email

            messages.success(request, "OTP has been sent to your email.")

            return redirect("verify_otp")

        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")

        except Exception as e:
            messages.error(request, f"Email Error: {str(e)}")

    return render(request, "forgot_password.html")

def verify_otp(request):
    email = request.session.get("reset_email")

    if not email:
        messages.error(request, "Password reset session expired.")
        return redirect("forgot_password")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("forgot_password")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        try:
            otp_obj = PasswordResetOTP.objects.get(
                user=user,
                otp=entered_otp
            )

            if timezone.now() > otp_obj.expires_at:
                otp_obj.delete()
                messages.error(request, "OTP has expired.")
                return redirect("forgot_password")

            otp_obj.is_verified = True
            otp_obj.save()

            return redirect("reset_password")

        except PasswordResetOTP.DoesNotExist:
            messages.error(request, "Invalid OTP.")

    return render(request, "verify_otp.html")


def reset_password(request):
    email = request.session.get("reset_email")

    if not email:
        messages.error(request, "Password reset session expired.")
        return redirect("forgot_password")

    try:
        user = User.objects.get(email=email)

        otp_obj = PasswordResetOTP.objects.filter(
            user=user,
            is_verified=True
        ).last()

        if not otp_obj:
            messages.error(request, "Please verify your OTP first.")
            return redirect("verify_otp")

    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect("forgot_password")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "reset_password.html")

        user.set_password(password)
        user.save()

        PasswordResetOTP.objects.filter(user=user).delete()

        request.session.pop("reset_email", None)

        messages.success(request, "Password reset successful. Please login.")
        return redirect("login")

    return render(request, "reset_password.html")