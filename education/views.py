from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]

class VolunteerTrainingViewSet(viewsets.ModelViewSet):
    queryset=VolunteerTrainer.objects.all()
    serializer_class=VolunteerTrainerSerializer

class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset=TrainingProgram.objects.all()
    serializer_class=TrainingProgramSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset=Enrollment.objects.all()
    serializer_class=EnrollmentSerializer
    permission_classes=[IsAuthenticated]

class EventRegistraionViewSet(viewsets.ModelViewSet):
    queryset=EventRegistration.objects.all()
    serializer_class=EventRegistrationSerializer

class JobDriveViewSet(viewsets.ModelViewSet):
    queryset=JobDrive.objects.all()
    serializer_class=JobDriveSerializer

class JobDriveRegistraionViewSet(viewsets.ModelViewSet):
    queryset=JobDriveRegistration.objects.all()
    serializer_class=JobDriveRegistrationSerializer

@login_required
def enroll_program(request,program_id):
    program=get_object_or_404(TrainingProgram,id=program_id)
    student,created=Student.objects.get_or_create(
        user=request.user,defaults={
            'education':'B-Tech',
            'college_name':'Not provided',
            'graduation_year':2026,
            'interested_domain':'General',
        }
    )
    Enrollment.objects.get_or_create(student=student,program=program)
    return redirect(f'/programs/?enrolled={program.id}')

@login_required
def register_event(request,event_id):
    event=get_object_or_404(Event,id=event_id)
    student,created=Student.objects.get_or_create(
        user=request.user,defaults={
            'education':'B-Tech',
            'college_name':'Not provided',
            'graduation_year':2026,
            'interested_domain':'General',
        }
    )
    EventRegistration.objects.get_or_create(student=student,event=event)
    return redirect(f'/events/?registered={event.id}')
 
@login_required
def apply_job(request,job_id):
    job=get_object_or_404(JobDrive,id=job_id)
    if request.method=='POST':
        student,created=Student.objects.get_or_create(
            user=request.user,
            defaults={
                'education':'Not Provided',
                'college_name':'Not Provided',
                'graduation_year':2026,
                'interested_domain':'General'
            }
        )
        JobDriveRegistration.objects.create(
            student=student,
            job_drive=job,
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            resume=request.FILES['resume']
        )
        return render(request,'job_application_form.html',{'job':job,'success':True})
    return render(request,'job_application_form.html',{'job':job})

 