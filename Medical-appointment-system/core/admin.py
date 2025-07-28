from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Doctor, TimeSlot, Appointment

class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False
    verbose_name_plural = 'doctor'

class UserAdmin(BaseUserAdmin):
    inlines = [DoctorInline]
    list_display = BaseUserAdmin.list_display + ('role',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(TimeSlot)
admin.site.register(Appointment) 