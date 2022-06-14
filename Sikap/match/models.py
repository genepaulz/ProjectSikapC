from django.db import models
from django.db.models.fields.related import ForeignKey
from login.models import Applicant, Employer
from posts.models import Posts

# Create your models here.

class Match(models.Model):
    employerID = models.ForeignKey(Employer, on_delete=models.CASCADE, db_column='EmployerID')
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE, db_column='PostID')
    applicantID = models.ForeignKey(Applicant, on_delete=models.CASCADE, db_column='ApplicantID')


    class Meta:
        db_table = "Match"