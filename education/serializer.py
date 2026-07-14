from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class VolunteerTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=VolunteerTrainer
        fields='__all__'

class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model=TrainingProgram
        fields='__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields='__all__'

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventRegistration
        fields='__all__'

class JobDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobDrive
        fields='__all__'

class JobDriveRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobDriveRegistration
        fields='__all__'