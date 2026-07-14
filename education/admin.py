from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Student)
#admin.site.register(VolunteerTrainer)
#admin.site.register(TrainingProgram)
#admin.site.register(Enrollment)
#admin.site.register(EventRegistration)
#admin.site.register(JobDrive)
#admin.site.register(JobDriveRegistration)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display=(
        'student',
        'program',
        'enrolled_at',
        'status',
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'user',
        'education',
        'college_name',
        'graduation_year',
        'interested_domain',
    )

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'description',
        'duration_weeks',
        'start_date',
        'end_date',
        'trainer',
        'is_active',
        'created_at',
    )


@admin.register(VolunteerTrainer)
class VolunteerTrainerAdmin(admin.ModelAdmin):
    list_display=(
        'user',
        'qualification',
        'expertise',
        'expertise_year',
        'teaching_mode',
        'status',
    )

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display=(
        'student',
        'event',
        'registered_at',
    )


@admin.register(JobDrive)
class JobDriveAdmin(admin.ModelAdmin):
    list_display=(
        'company_name',
        'job_role',
        'location',
        'package',
        'eligibility',
        'last_date',
        'description',
        'is_active',
    )
    
@admin.register(JobDriveRegistration)
class JobDriveRegistrationAdmin(admin.ModelAdmin):
    list_display=(
        'full_name',
        'job_drive',
        'email',
        'phone_number',
        'status',
        'applied_at'
    )
    list_filter=(
        'status',
        'job_drive'
    )
    search_fields=(
        'full_name',
        'email'
    )
    
