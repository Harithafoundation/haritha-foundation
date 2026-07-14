from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuditLog
        fields='__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields='__all__'