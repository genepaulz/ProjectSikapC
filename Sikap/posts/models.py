from django.db import models
from django.db.models.fields.related import ForeignKey
# from login.models import Applicant

# Create your models here.

class Posts(models.Model):
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
    applicantID = models.ForeignKey("login.Applicant", on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        db_table = "Posts"
    
 
        