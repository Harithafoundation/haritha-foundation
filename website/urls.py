from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
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
    path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ),
    name='password_reset'),

    path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),
    name='password_reset_done'),

    path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),
    name='password_reset_confirm'),

    path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),
    name='password_reset_complete'),
    path('logout/',logout_view,name='logout'),
    path('gallery/',gallery,name='gallery'),
    path('payment-success/',payment_success,name='payment_success')
    
]