from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Donor)
#admin.site.register(Project)
#admin.site.register(Donation)
admin.site.register(Receipt)




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'description',
        'target_amount',
        'collected_amount',
        'is_active',
    )

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display=(
        'user',
        'pan_number',
        'donor_type',
    )

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display=(
        'donor',
        'name',
        'email',
        'phone',
        'address',
        'pan_number',
        'project',
        'amount',
        'razorpay_order_id',
        'payment_id',
        'payment_status',
        'donated_at',
    )


