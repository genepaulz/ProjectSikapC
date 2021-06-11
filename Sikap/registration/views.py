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
            companyName=""
            isDeleted = 0
            industry = request.POST.get("aindustry")
            region = request.POST.get("aregion")
            province = request.POST.get("aprovince")
            city = request.POST.get("acity")
            age = request.POST.get("aage")

            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)

            User.register(email,enc_password,firstname,lastname,user_type,isVerified,companyName,industry,region,province,city,isDeleted,age)
            
            return redirect('landing:landing_view')
        return HttpResponse("Fail")

class RegisterViewE(View):
    def get(self,request):
        return render(request,'Employer_Registration.html')

    def post(self,request):
        if 'employer' in request.POST:
            email = request.POST.get("eemail")
            password = request.POST.get("epassword")
            name = request.POST.get("ename")
            surname = request.POST.get("esurname")
            user_type = 1
            isVerified = 0
            companyName = request.POST.get("ecompanyName")
            industry = request.POST.get("eindustry")

            #encrypt password
            enc_password = pbkdf2_sha256.encrypt(password, rounds=10,salt_size=16)



            print(email)
            print(password)
            print(name)
            print(surname)
            print(user_type)
            print(isVerified)
            print(industry)

            form = User(

                email = email,
                password = enc_password,
                firstname = name,
                lastname = surname,
                user_type = user_type,
                isVerified = isVerified,
                companyName = companyName,
                industry = industry,
                region = "",
                province = "",
                city = "",
                age = 0
            )
            form.save()
            return redirect('landing:landing_view')
        return HttpResponse("Fail")
