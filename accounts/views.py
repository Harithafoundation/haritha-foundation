from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializers import *
# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset=Role.objects.all()
    serializer_class=RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[filters.SearchFilter,filters.OrderingFilter]
    search_fields=['username','email']
    ordering_fields=['username','email','id']


