from django.http import HttpResponseRedirect
from django.shortcuts import render
from flask import render_template
from patient.models import Patient
from receptionist.models import DoctorPatientAssignment
from wardclerk.models import Ward,WardDetails
from doctor.models import Doctor
# Create your views here.
def allPatientDetails(request):
    if request.method == 'POST':
        if 'patientId' in request.POST and request.POST['patientId']!='':
            patientId = request.POST['patientId']
        else:
            patientId = 0
        if 'patientName' in request.POST and request.POST['patientName']!='':
            patientName = request.POST['patientName']
        else:
            patientName = None
        if patientId!=0:
            specificPatientDetails ={'patients':list(Patient.objects.filter(PatientID=patientId))}
            return render(request,'receptionist/allPatients.html',specificPatientDetails)
        elif patientName!=None :
            specificPatientDetails ={'patients':list(Patient.objects.filter(FirstName=patientName))}
            return render(request,'receptionist/allPatients.html',specificPatientDetails)
        else:
            allPatientDetails={'patients':list(Patient.objects.all())}
            return render(request,'receptionist/allPatients.html',allPatientDetails)
    else:
        allPatientDetails={'patients':list(Patient.objects.all())}
        return render(request,'receptionist/allPatients.html',allPatientDetails)

def patientDetails(request):
    if request.method== 'POST':
        if 'patientId' in request.POST and request.POST['patientId']!='':
            patientId = request.POST['patientId']
            PatientDetails={'appointments':list(DoctorPatientAssignment.objects.filter(Patient_id=patientId))}
            return render(request,'receptionist/patientDetails.html',PatientDetails)
        else:
            # return HttpResponseRedirect('/')
            return HttpResponseRedirect('/receptionist/allPatients/')
    else:
        # return HttpResponseRedirect('/receptionist/allPatients/')
        return HttpResponseRedirect('/')

def wardDoctorDetails(request):
    Details={'Ward':list(Ward.objects.all()),
            'WardDetails':list(WardDetails.objects.all()),
            'DoctorDetails':list(Doctor.objects.all())}
    return render(request,'receptionist/wardDoctorDetails.html',Details)

def registration(request):
    if request.method=='POST':
        p=Patient.objects.create(
            PatientID = len(Patient.objects.all())+1,
            FirstName = request.POST['fname'],
            LastName = request.POST['lname'],
            contact = request.POST['Contact'],
            gender = request.POST['gender'],
            Age = request.POST['Age'],
            Height = request.POST['Height'],
            Weight = request.POST['Weight'],
            BloodGroup = request.POST['Blood_group'],
            EmailAddress = request.POST['Email'],
            PermantAddress = request.POST['Address']
        )
        p.save()
        return HttpResponseRedirect('/receptionist/allPatients/') 
    else:
        return render(request,'receptionist/registration.html')
