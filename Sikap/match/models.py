from django.db import models
# from login.models import Applicant, Employer


# Create your models here.

class Match(models.Model):
    employerID = models.ForeignKey("login.Employer", on_delete=models.CASCADE,db_column='employerID')
    postsID = models.ForeignKey("posts.Posts", on_delete=models.CASCADE,db_column='postsID')
    applicantID = models.ForeignKey("login.Applicant", on_delete=models.CASCADE,db_column='applicantID')


    class Meta:
        db_table = "Match"