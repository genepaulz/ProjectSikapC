from django.db import models
from rating.models import Rating
from login.models import *
from .forms import *
from datetime import *
from passlib.hash import pbkdf2_sha256
# Create your models here.


class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    companyName = models.CharField(max_length = 100)
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

    def register(email,password,firstname,lastname,user_type,isVerified,companyName,industry,region,province,city,isDeleted,age):
        form = User(
            email = email,
            password = password,
            firstname = firstname,
            lastname = lastname,
            isVerified = isVerified,
            isDeleted = isDeleted,
            companyName = "",
            user_type = user_type,
            industry = industry,
            region = region,
            province = province,
            city = city,
        )
        form.save()
        form1 = Applicant(
                applicantUser = form,
                age = age,
                postion = ""
        )
        form1.save()
        form2 = Rating(
            raterEmail = form1,
            rating = 0.0,
            numOfRates = 0
        )
        form2.save()

    class Meta:
        db_table = "User"



class Applicant(models.Model):
    applicantUser = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)

<<<<<<< HEAD
=======
    def createpost(yearsOfExperience,position,industry,region,province,city,age,email,isAgeViewable,firstname,lastname):
        form = Posts(
            yearsOfExperience = yearsOfExperience,
            position = position,
            industry = industry,
            region = region,
            province = province,
            city = city,
            age = age,
            dateadded = datetime.now(),
            email = request.session['email'],
            isAgeViewable = isAgeViewable,
            firstname = request.session['firstname'],
            lastname = request.session['lastnamename']
        )
        form.save()
>>>>>>> e7ffd3a03e0eda54195d4b4ac4c516a20350fcc4

    class Meta:
        db_table = "Applicant"

class Employer(models.Model):
    employerUser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    companyName =  models.CharField(max_length=100)
    matches = models.IntegerField()

    class Meta:
        db_table = "Employer"
