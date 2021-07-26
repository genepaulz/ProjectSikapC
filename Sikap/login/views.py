from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import *
from .import views
from datetime import *



# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("pass")
        q = User.objects.get(email=email)    
        
        if(User.login(email,password) == 1):
            #IMPLEMENT CONTEXT HERE
            request.session['email'] = q.email   
            e = Employer.objects.get(employerUser_id = q.id)    
            request.session['companyName'] = e.companyName
            request.session['hasSearched'] = 0
            request.session['searchResults'] = "nothing"
            return redirect('viewas:viewase_view')
        else:    
            #IMPLEMENT CONTEXT HERE
            request.session['email'] = q.email
            request.session['firstname'] = q.firstname
            request.session['lastname'] = q.lastname
            request.session['industry'] = q.industry
            request.session['region'] = q.region
            request.session['province'] = q.province
            request.session['city'] = q.city
            a = Applicant.objects.get(applicantUser_id = q.id)
            request.session['age'] = a.age
            return redirect('viewas:viewasa_view')
            # return render(request,'applicant.html',context)        
        #else:
            #return HttpResponse("User does not EXIST!")


