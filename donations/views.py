from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.
class DonorViewSet(viewsets.ModelViewSet):
    queryset=Donor.objects.all()
    serializer_class=DonorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset=Donation.objects.all()
    serializer_class=DonationSerializer
    permission_classes=[IsAuthenticated]

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Receipt.objects.all()
    serializer_class=ReceiptSerializer