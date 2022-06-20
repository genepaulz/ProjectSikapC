from django.db import models
from django.db.models.fields.related import ForeignKey
#from login.models import Applicant

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

def __str__(self):
    return self.applicantID


def viewPosts(id):      
        
        d = ""
        post = Posts.objects.filter(applicantID=id)
        for objects in post:
        
                d += "<div class='card'><div class='container'><h4>ID: <input name='postID' type='hidden' value="+str(objects.id)+">"+str(objects.id)+"</h3><input name='appID' type='hidden' value="+str(objects.applicantID_id)+"><h4><b>"+objects.lastname+", "+objects.firstname+"</b></h4><p>Position: "+objects.position+"</p><p>Years of Experience: "+str(objects.yearsOfExperience)+"</p><p>Industry: "+objects.industry+"</p><p>Region: "+objects.region+"</p><p>Province: "+objects.province+"</p><p>City: "+objects.city+"</p></div><center><input type='submit' class='btn btn-info btn-lg btn-block p-3' name='match' value='Match'></div><br>"
        
        context = {
            'result' : d
      
        }        
        return context
 
        