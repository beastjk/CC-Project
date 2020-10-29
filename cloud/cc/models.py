from django.db import models
from django.contrib.auth.models import  auth, User
# Create your models here.
class Registration(models.Model):

    first_name= models.CharField( max_length=100)
    last_name= models.CharField( max_length=100)
    username = models.CharField(max_length=100,primary_key=True,unique=True)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class ProfileEvaluation(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    contact = models.BigIntegerField()
    country = models.CharField(max_length=100)
    budget = models.IntegerField()
    degree = models.CharField(max_length=100)
    AOI_1 = models.CharField(max_length=100)
    AOI_2 = models.CharField(max_length=100)
    percentage_10 = models.IntegerField(default=0)
    percentage_12 = models.IntegerField(default=0)
    percentage_undergrad = models.IntegerField(default=0)
    backlogs = models.FloatField(default=0)
    username = models.ForeignKey(Registration, on_delete=models.CASCADE)
    GRE_Score = models.IntegerField(default=0)
    TOEFL_Score = models.IntegerField(default=0)
    SOP = models.IntegerField(default=0)
    LOR = models.IntegerField(default=0)
    CGPA = models.IntegerField(default=0)
    Research = models.IntegerField(default=0)


