from django.db import models
#from login.models import Employer

# Create your models here.

class Rating(models.Model):
    raterEmail = models.ManyToManyField("login.Employer",blank=True, null=True)
    rating = models.FloatField()
    numOfRates = models.IntegerField()

    class Meta:
        db_table = "Rating"

