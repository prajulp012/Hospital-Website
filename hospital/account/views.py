from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView,ListView
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from .models import *
from django.views.decorators.cache import never_cache


def signin_required(fun):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.error(request,"Unsuccessful...!Login Required")
            return redirect('signin')
    return inner

doc = [signin_required,never_cache]

# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    
class RegView(View):
    def get(self,request):
        form = RegForm()
        return render(request,'contact.html',{'form':form})
    def post(self,request):
        form_data = RegForm(data=request.POST)
        if form_data.is_valid():
            messages.success(request,'Successful...!')
            form_data.save()
            return redirect('home')
        else:
            messages.error(request,'Unsuccessful...!')
            return render(request,'contact.html',{'form':form_data})
        
class LogView(FormView):                
    template_name='login.html'
    form_class = LogForm
    def post(self,request):
        form_data = LogForm(data=request.POST)
        if form_data.is_valid():
            usrname = form_data.cleaned_data.get('username')            #data taken from the forms.py
            pswd = form_data.cleaned_data.get('password')
            user = authenticate(request,username=usrname,password=pswd) #this method just checks the database username & password with user provided username & password
            if user:
                login(request,user)
                return redirect('homes')
            else:
                return render(request,'login.html',{'form':form_data})
            

class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
    
@method_decorator(doc,name='dispatch')   
class Booking(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = BookingForm()
            return render(request,'booking.html',{'form':form})
        else:
            return render(request,'booking.html')
    def post(self,request):
        if request.user.is_authenticated:
            user=request.user
            form_data = BookingForm(data=request.POST)
            if form_data.is_valid():
                doc=form_data.save(commit=False)
                doc.user=user
                doc.save()
                return redirect('homes')
            else:
                 return render(request,'booking.html',{'form':form_data})
             
             
@method_decorator(doc,name='dispatch')               
class Details(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:                                   
            user = request.user                                             
            details = Bookingss.objects.filter(user=user)                    
            return render(request,'details.html',{'details':details})       
        else:                                                                
             return render(request,'details.html')
         

class PatientDelete(View):
    def get(self,request,*args,**kwargs):
        patdel = kwargs.get('patdel')
        pat    = Bookingss.objects.get(id=patdel)
        pat.delete()
        # messages.success(request,"Employee Deleted Successfully...!")
        return redirect('details')

  
class About(TemplateView):
    template_name = 'about.html'

    
class DepartmentView(ListView):
    template_name = 'department.html'
    model         = Department
    context_object_name = 'department'

    
class DoctorView(ListView):
    template_name = 'doctor.html'
    model         = Doctor
    context_object_name = 'doctor'

     
class Contacts(TemplateView):
    template_name = 'contacts.html'

  
class Homes(View):
    def get(self,request):
        return render(request,'homepages.html')

