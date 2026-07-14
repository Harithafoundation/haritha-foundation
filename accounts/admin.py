from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Role)
#admin.site.register(User)





@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'phone_number',
        'role',
        'is_staff',
    )






