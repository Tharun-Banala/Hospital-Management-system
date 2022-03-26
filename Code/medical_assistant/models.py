from django.db import models
from receptionist.models import DoctorPatientAssignment
# Create your models here.

class MedicalAssistant(models.Model):
    MedicalAssistantID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField
    Salary = models.IntegerField
    Shift = models.IntegerField
    BloodGroup = models.CharField(max_length=45)

class MedicalReport(models.Model):
    ReportID = models.IntegerField(primary_key=True)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)
    MedicalAssistant = models.ForeignKey(MedicalAssistant,default=None,on_delete=models.CASCADE)
