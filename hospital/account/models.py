from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user           = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    patient_name   = models.CharField(max_length=255,verbose_name='Patient Name')
    patient_phone  = models.CharField(max_length=10,verbose_name='Patient Phone')
    patient_email  = models.EmailField(verbose_name='Patient Email')
    doctor         = models.CharField(max_length=255,verbose_name='Doctor')
    booking_date   = models.DateField(verbose_name='Booking Date')
    booked_on      = models.DateField(auto_now=True)

class Bookings(models.Model):
    user           = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    patient_name   = models.CharField(max_length=255,verbose_name='Patient Name')
    patient_phone  = models.CharField(max_length=10,verbose_name='Patient Phone')
    patient_email  = models.EmailField(verbose_name='Patient Email')
    doctor         = models.CharField(max_length=255,verbose_name='Doctor')
    booking_date   = models.DateField(verbose_name='Booking Date')
    booked_on      = models.DateField(auto_now=True)
    
class Department(models.Model):
    department_name        = models.CharField(max_length=100)
    department_description = models.TextField()

    def __str__(self):
        return self.department_name
    
class Doctor(models.Model):
    doctor_name           = models.CharField(max_length=255)
    doctor_specialization = models.CharField(max_length=255)
    department_name       = models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor_image          = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.'+self.doctor_name + '-('+self.doctor_specialization+')'
    

class Bookingss(models.Model):
    user           = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    patient_name   = models.CharField(max_length=255,verbose_name='Patient Name')
    patient_phone  = models.CharField(max_length=10,verbose_name='Patient Phone')
    patient_email  = models.EmailField(verbose_name='Patient Email')
    doctor_name    = models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Doctor Name')
    booking_date   = models.DateField(verbose_name='Booking Date')
    booked_on      = models.DateField(auto_now=True)
    
