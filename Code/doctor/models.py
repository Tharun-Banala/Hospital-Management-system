from curses import def_prog_mode
from pickle import NONE
from django.db import models

# Create your models here.
  
class Doctor(models.Model):
    DoctorID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField
    Salary = models.IntegerField
    Shift = models.IntegerField
    BloodGroup = models.CharField(max_length=45)
    Department = models.CharField(max_length=45,default=None)
    status = models.CharField(max_length=45,default=None) 
    contact = models.CharField(max_length=15,default=None)