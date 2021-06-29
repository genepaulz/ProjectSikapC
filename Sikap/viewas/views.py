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
        stuff = request.session['search']
        print(stuff)
        if(stuff != "nothing"):
            stuff2 = request.session['searchResults']
            return HttpResponse(stuff2)
        else:
            request.session['searchResults']
            return render(request,'viewase.html')
    
    def post(self,request):
        # if('search' in request.POST):
        #     string = request.POST.get("materialInput")
        #     context = Employer.search(string)
        #     return render(request,viewase.html,context)
        if('logout' in request.POST):
            del request.session['email']
            del request.session['companyName']
            return redirect('landing:landing_view')
        elif('search' in request.POST):
            request.session['search'] = "nothing"
            
            region = request.POST.get("regionPOST")            
            province = request.POST.get("provincePOST")
            city = request.POST.get("cityPOST")
            industry = request.POST.get("industryPOST")
            filt = request.POST.get("inputPOST")
            request.session['searchResults'] = Employer.search(region,province,city,industry,filt)
            
            print(request.session['search'])
            print(request.session['searchResults'])
            return redirect('viewas:viewase_view')
            # return render(request,'viewase.html')
            # return HttpResponse("NANI")

def LiveSearch(request):
    template_name = "index.html"
    filt = request.GET.getlist("d")[0]
    d=""
    mat = Posts.objects.filter(industry__icontains=filt)
    print(filt)
    image = "/static/img_avatar.png"
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
        
    print(d)
    mat = Posts.objects.filter(region__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    mat = Posts.objects.filter(province__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    mat = Posts.objects.filter(city__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    mat = Posts.objects.filter(position__icontains=filt)
    for objects in mat:
        # d += "<div class='row-lg' id='results'>Name: "+objects.lastname+", "+objects.firstname+"</div>"
        if(objects.isAgeViewable):
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
        else:
            d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
    print(d)
    return JsonResponse({"d": d})