# Generated by Django 3.2.7 on 2022-03-26 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0001_initial'),
        ('billing_desk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalBills',
            fields=[
                ('TotalBill', models.IntegerField()),
                ('AmountPaid', models.IntegerField()),
                ('FullyPaidDate', models.DateField()),
                ('BillID', models.IntegerField(primary_key=True, serialize=False)),
                ('Appointment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.doctorpatientassignment')),
                ('BillerID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='billing_desk.biller')),
            ],
        ),
    ]