from django.db import models
from patient.models import Patient
from receptionist.models import DoctorPatientAssignment
class WardClerk(models.Model):
    WardClerkID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField
    Salary = models.IntegerField
    Shift = models.IntegerField
    BloodGroup = models.CharField(max_length=45)

class Ward(models.Model):
    WardNo = models.IntegerField(primary_key=True)
    WardClerk = models.ForeignKey(WardClerk,default=None,on_delete=models.CASCADE)
    WardCapacity=models.IntegerField()
    Population = models.IntegerField()  

class WardDetails(models.Model):
    WardNo = models.ForeignKey(Ward,default=None,on_delete=models.CASCADE)
    BedNo= models.IntegerField()
    Patient= models.ForeignKey(Patient,default=None,on_delete=models.CASCADE)
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)
    Description = models.CharField(max_length=500)
    JoinedDate=models.DateField()
    LeftDate= models.DateField()