from django.db import models
from rating.models import Rating
from datetime import *
from posts.forms import Posts
from django.http import JsonResponse
from passlib.hash import pbkdf2_sha256
# Create your models here.


class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 10)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    isVerified = models.IntegerField()
    isDeleted = models.IntegerField()
    user_type = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    def debug_password(raw_password):
        enc_password = pbkdf2_sha256.encrypt(raw_password, rounds=10,salt_size=16)
        return enc_password

    def registerApplicant(email,password,firstname,lastname,user_type,isVerified,industry,region,province,city,isDeleted,age):
        form = User(
            email = email,
            password = password,
            firstname = firstname,
            lastname = lastname,
            isVerified = isVerified,
            isDeleted = isDeleted,
            user_type = user_type,
            industry = industry,
            region = region,
            province = province,
            city = city,
        )
        form.save()
        form2 = Rating(            
            rating = 0.0,
            numOfRates = 0
        )
        form2.save()
        form1 = Applicant(
                applicantUser = form,
                age = age,
                position = "",
                ratings = form2
        )
        form1.save()

    def registerEmployer(email,password,firstname,lastname,user_type,isVerified,companyName,industry,region,province,city,isDeleted):
        form = User(
            email = email,
            password = password,
            firstname = firstname,
            lastname = lastname,
            isVerified = isVerified,
            isDeleted = isDeleted,
            user_type = user_type,
            industry = industry,
            region = region,
            province = province,
            city = city
        )
        form.save()
        # form4 = Matches(

        # )
        form3 = Employer(
            employerUser = form,
            companyName = companyName,
            matches = 0
        )
        form3.save()

    def login(email,password):
        flag = -1
        q = User.objects.get(email=email)
        if(q.verify_password(password)):
            if(User.viewas(q.user_type)==0):
                flag = 0
            else:
                flag = 1
        
        return flag

    def viewas(user_type):
        if(user_type == 0):
            flag = 0
        elif(user_type == 1):
            flag = 1
        return flag
        
    class Meta:
        db_table = "User"


class Applicant(models.Model):
    applicantUser = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def createpost(email,firstname,lastname,region,province,city,age,industry,yearsOfExperience,position,isAgeViewable):
        a = Applicant.objects.get(applicantUser = User.objects.get(email=email))
        form = Posts(
            applicantID = a,
            email = email,
            firstname = firstname,
            lastname = lastname,
            region = region,
            province = province,
            city = city,
            age = age,
            industry = industry,
            yearsOfExperience = yearsOfExperience,
            position = position,
            dateAdded = datetime.now(),
            isAgeViewable = isAgeViewable,
            isDeleted = 0
        )
        form.save()

    class Meta:
        db_table = "Applicant"

class Employer(models.Model):
    employerUser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    companyName =  models.CharField(max_length=100)
    matches = models.IntegerField()

    class Meta:
        db_table = "Employer"

    def search(region,province,city,industry,filt):      
        image = "/static/img_avatar.png"
        d = ""
        mat = Posts.objects.filter(region=region,province=province,city=city,industry=industry,position__icontains=filt)
        for objects in mat:
            
            if(objects.isAgeViewable):
                d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p><p>Age: "+str(objects.age)+"</p></div></div><br>"
            else:
                d += "<div class='card'><img src="+image+" alt='Avatar' style='width:100%'><div class='container'><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div></div><br>"
        context = {
            'result' : d
        }        
        return context
