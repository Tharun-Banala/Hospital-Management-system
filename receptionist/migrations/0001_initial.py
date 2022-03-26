# Generated by Django 3.2.7 on 2022-03-26 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('ReceptionistID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('EmailAddress', models.CharField(max_length=45)),
                ('PermantAddress', models.CharField(max_length=100)),
                ('BloodGroup', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorPatientAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppointmentID', models.IntegerField(default=None)),
                ('VisitNo', models.IntegerField(default=None)),
                ('Doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('Patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('Receptionist', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.receptionist')),
            ],
            options={
                'unique_together': {('AppointmentID', 'VisitNo')},
            },
        ),
    ]