from pickle import TRUE
from django.db import models
from receptionist.models import DoctorPatientAssignment
# Create your models here.


class Diagnostician(models.Model):
    DiagnosticianID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField
    Salary = models.IntegerField
    Shift = models.IntegerField
    BloodGroup = models.CharField(max_length=45)

class Diagnosis(models.Model):
    DiagnosticReportID = models.IntegerField(primary_key=True)
    Diagnostician = models.ForeignKey(Diagnostician,default=None,on_delete=models.CASCADE)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=True,on_delete=models.CASCADE)