from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import *
from .import views
from login.views import *
from datetime import *



# Create your views here.

class LandingView(View):
    def get(self,request):
        return render(request,'index.html')
    
    def post(self,request):
        if('login' in request.POST):
            return redirect('login:login_view')
        elif('rega' in request.POST):
            return redirect('registration:registera_view')
        elif('rege' in request.POST):
            return redirect('registration:registere_view')
        # elif('encrypt' in request.POST):
        #     qs = User.objects.all()
        #     id = 1
        #     for user in qs:
        #         encryptedPassword = User.debug_password(user.password)
        #         form = User.objects.filter(id=id).update(
        #             password = encryptedPassword,                    
        #         )
        #         id+=1
                
