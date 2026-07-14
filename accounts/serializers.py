from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','phone_number','address','role']

    def validate_phone_number(self,value):
        if len(value) !=10:
            raise serializers.ValidationError('Phone number must contain 10 digits')
        return value
    def validate_email(self,value):
        if '@gmail.com' not in value:
            raise serializers.ValidationError('Enter Valid Gmail address')
        return value
