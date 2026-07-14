from rest_framework import serializers
from .models import *

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donation
        fields='__all__'
    def validate_amount(self,value):
        if value <= 0:
            raise serializers.ValidationError('Donation amount must be greater than zero ')
        return value
    def validate_payment_id(self,value):
        if len(value)<5:
            raise serializers.ValidationError('Payment ID is too short')
        return value

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields='__all__'