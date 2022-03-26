from django.db import models
from receptionist.models import DoctorPatientAssignment
# Create your models here.

class Biller(models.Model):
    BillerID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=45)
    LastName = models.CharField(max_length=45)
    EmailAddress = models.CharField(max_length=45)
    PermantAddress = models.CharField(max_length=100)
    Age = models.IntegerField
    Salary = models.IntegerField
    Shift = models.IntegerField
    BloodGroup = models.CharField(max_length=45)

class HospitalBills(models.Model):
    Appointment = models.ForeignKey(DoctorPatientAssignment,default=None,on_delete=models.CASCADE)
    TotalBill = models.IntegerField()
    AmountPaid = models.IntegerField()
    FullyPaidDate = models.DateField()
    BillerID = models.ForeignKey(Biller,default=None,on_delete=models.CASCADE)
    BillID = models.IntegerField(primary_key=True)

