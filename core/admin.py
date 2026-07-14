from django.contrib import admin
from .models import *

#admin.site.register(Event)
admin.site.register(Report)
admin.site.register(AuditLog)
#admin.site.register(Gallery)
#admin.site.register(GalleryMedia)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'subject',
        'created_at',
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'event_type',
        'description',
        'event_date',
        'location',
        'image',
        'is_active',
        'created_at',
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'uploaded_at',
    )



@admin.register(GalleryMedia)
class GalleryMediaAdmin(admin.ModelAdmin):
    list_display = (
        'gallery',
        'image',
        'video',
    )





