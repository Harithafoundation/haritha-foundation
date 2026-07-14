from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('students',StudentViewSet)
router.register('trainers',VolunteerTrainingViewSet)
router.register('programs',TrainingProgramViewSet)
router.register('enrollments',EnrollmentViewSet)
router.register('event-registrations',EventRegistraionViewSet)
router.register('job-drives',JobDriveViewSet)
router.register('job-applications',JobDriveRegistraionViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('enroll/<int:program_id>/',enroll_program,name='enroll_program'),
    path('register-event/<int:event_id>/',register_event,name='register_event'),
    path('apply-job/<int:job_id>/',apply_job,name='apply_job'),
]