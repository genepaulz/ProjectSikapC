from django.db import reset_queries
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from posts.models import Posts
from login.models import Employer
from django.template import *
from .import views
from datetime import *
from passlib.hash import pbkdf2_sha256


# Create your views here.

class ViewAsAView(View):
    def get(self,request):
        return render(request,'applicant.html')
    
    def post(self,request):
        if('post' in request.POST):
            return redirect('posts:posts_view')
        elif('logout' in request.POST):
            del request.session['email']
            del request.session['firstname']
            del request.session['lastname']
            del request.session['industry']
            del request.session['region']
            del request.session['province']
            del request.session['city']
            del request.session['age']
            return redirect('landing:landing_view')


class ViewAsEView(View):
    def get(self,request):        
        return render(request,'employer.html')
        
            
    
    def post(self,request):
        if('logout' in request.POST):
            del request.session['email']
            del request.session['companyName']
            del request.session['hasSearched']
            del request.session['searchResults']
            return redirect('landing:landing_view')
        elif('search' in request.POST):
            region = request.POST.get("regionPOST")            
            province = request.POST.get("provincePOST")
            city = request.POST.get("cityPOST")
            industry = request.POST.get("industryPOST")
            filt = request.POST.get("inputPOST")
            request.session['hasSearched'] = 1
            request.session['searchResults'] = Employer.search(region,province,city,industry,filt)
        
            return redirect('viewas:viewase_view')