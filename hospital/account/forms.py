from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Bookingss

class RegForm(UserCreationForm):
    error_messages = {
        'password_mismatch':("The two password fields didn't match"),
    }
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    )
    
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
        strip=False,
        
    )
    class Meta:
        model  = User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
            'email'     : forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            'username'  : forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),
        }
        
class LogForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookingss
        fields = ['patient_name','patient_phone','patient_email','doctor_name','booking_date']

        widgets = {
            'patient_name'  : forms.TextInput(attrs={"placeholder":"Patient Name","class":"form-control"}),
            'patient_phone' : forms.NumberInput(attrs={"placeholder":"Patient Phone Number","class":"form-control"}),
            'patient_email' : forms.EmailInput(attrs={"placeholder":"Patient Email","class":"form-control"}),
            'doctor_name'   : forms.Select(attrs={'class':'form-control'}),
            'booking_date'  : DateInput(attrs={'type': 'date',"class":'form-control'})
            
        }
