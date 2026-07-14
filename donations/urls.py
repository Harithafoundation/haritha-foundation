from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('donors',DonorViewSet)
router.register('projects',ProjectViewSet)
router.register('donations',DonationViewSet)
router.register('receipts',ReceiptViewSet)

urlpatterns=[
    path('',include(router.urls)),
]