from django.contrib import admin

from .models import Bookingss,Department,Doctor
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'patient_name', 'patient_phone', 'patient_email','booking_date', 'booked_on' )

admin.site.register(Bookingss, BookingAdmin)
admin.site.register(Department)
admin.site.register(Doctor)
