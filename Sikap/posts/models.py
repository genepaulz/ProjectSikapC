from django.db import models
from django.db.models.fields.related import ForeignKey
from login.models import *
from .models import *
# Create your models here.

class Posts(models.Model):
    applicantID = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)   
    region = models.CharField(max_length = 10)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()
    industry = models.CharField(max_length = 100)
    yearsOfExperience = models.IntegerField()
    position = models.CharField(max_length = 100)
    dateAdded = models.DateTimeField()
    isAgeViewable = models.IntegerField()
    isDeleted = models.IntegerField()

    # def isvalid():
    #     return 1
    # def ishired():
    #     return 1

    class Meta:
        db_table = "Posts"

