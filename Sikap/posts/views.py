from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import *
from .import views
from datetime import *
from passlib.hash import pbkdf2_sha256


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
        if isAgeViewable == 'on':
            isAgeViewable = 1
        else:
            isAgeViewable = 0

        
        return redirect('viewas:viewasa_view')