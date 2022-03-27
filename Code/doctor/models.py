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
    department = models.CharField(max_length=45)
    status = models.CharField(max_length=45) 