from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from login.models import Applicant
from django.template import *
from .import views
from datetime import *
from django.contrib import messages



# Create your views here.

class PostsView(View):
    def get(self,request):
        return render(request,'createpost.html')

    def post(self,request):
        
        yearsOfExperience = request.POST.get("yearsOfExperience")
        position = request.POST.get("position")
        industry = request.POST.get("industry")
        region = request.POST.get("region")
        province = request.POST.get("province")
        city = request.POST.get("city")
        age = request.POST.get("age")
        isAgeViewable = request.POST.get("isAgeViewable")
        email = request.session['email']
        
        if isAgeViewable == 'on':
            isAgeViewable = 1
        else:
            isAgeViewable = 0

        email = request.session.get('email')
        firstname = request.session.get('firstname')
        lastname = request.session.get('lastname')

        Applicant.createpost(email,firstname,lastname,region,province,city,age,industry,yearsOfExperience,position,isAgeViewable)
        messages.success(request,'Post Succesful!')
        return redirect('viewas:viewasa_view')