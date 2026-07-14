from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render,redirect
from accounts.permissions import IsAdminRole
from .models import *
from .serializer import *
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    permission_classes=[IsAdminRole]

class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset=AuditLog.objects.all()
    serializer_class=AuditLogSerializer
    permission_classes=[IsAdminRole]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer



