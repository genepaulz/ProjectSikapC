from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from login.models import User
from login.models import Applicant
from .models import *
from django.template import *
from .import views
from datetime import *
from passlib.hash import pbkdf2_sha256


# Create your views here.


class RegisterViewA(View):
    def get(self,request):
        return render(request,'Applicant_Registration.html')

    def post(self,request):
        if 'applicant' in request.POST:
            email = request.POST.get("aemail")
            password = request.POST.get("apassword")
            firstname = request.POST.get("aname")
            lastname = request.POST.get("asurname")
            user_type = 0
            isVerified = 0
            isDeleted = 0
            industry = request.POST.get("aindustry")
            region = request.POST.get("aregion")
            province = request.POST.get("aprovince")
            city = request.POST.get("acity")
            age = request.POST.get("aage")

            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)
            User.registerApplicant(email,enc_password,firstname,lastname,user_type,isVerified,industry,region,province,city,isDeleted,age)
            
            return redirect('landing:landing_view')
        return HttpResponse("Fail")

class RegisterViewE(View):
    def get(self,request):
        return render(request,'Employer_Registration.html')

    def post(self,request):
        if 'employer' in request.POST:
            email = request.POST.get("eemail")
            password = request.POST.get("epassword")
            firstname = request.POST.get("ename")
            lastname = request.POST.get("esurname")
            user_type = 1
            isVerified = 0
            companyName = request.POST.get("ecompanyName")
            industry = request.POST.get("eindustry")
            region = ""
            province = ""
            city = ""
            isDeleted = 0

            #encrypt password

            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)
            User.registerEmployer(email,enc_password,firstname,lastname,user_type,isVerified,companyName,industry,region,province,city,isDeleted)

            return redirect('landing:landing_view')
        return HttpResponse("Fail")
