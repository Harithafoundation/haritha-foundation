from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('programs/',programs,name='programs'),
    path('events/',events,name='events'),
    path('gallery/',gallery,name='gallery'),
    path('donate/',donate,name='donate'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/', login_view,name='login'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('verify-otp/',verify_otp,name='verify_otp'),
    path('reset-password/',reset_password,name='reset_password'),
    path('logout/',logout_view,name='logout'),
    path('gallery/',gallery,name='gallery'),
    path('register-otp/',register_otp,name='register_otp'),
    path('payment-success/',payment_success,name='payment_success')
    
]