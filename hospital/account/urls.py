from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('signup/',RegView.as_view(),name='signup'),
    path('signin/',LogView.as_view(),name='signin'),
    path('signout/',SignOut.as_view(),name='signout'),
    path('about/',About.as_view(),name = 'about'),
    path('booking/',Booking.as_view(),name='booking'),
    path('details/',Details.as_view(),name='details'),
    path('department/',DepartmentView.as_view(),name='department'),
    path('doctor/',DoctorView.as_view(),name='doctor'),
    path('contact/',Contacts.as_view(),name='contact'),
    path('patientdelete<int:patdel>',PatientDelete.as_view(),name='patientdelete'),
    path('home',Homes.as_view(),name='homes'),
]