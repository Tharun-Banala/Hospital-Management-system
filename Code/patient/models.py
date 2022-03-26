from django.db import models

# Create your models here.
class Patient(models.Model):
    PatientID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    Age = models.IntegerField
    BloodGroup = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
