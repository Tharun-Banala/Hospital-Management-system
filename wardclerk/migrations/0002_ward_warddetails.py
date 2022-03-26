# Generated by Django 3.2.7 on 2022-03-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0001_initial'),
        ('patient', '0001_initial'),
        ('wardclerk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('WardNo', models.IntegerField(primary_key=True, serialize=False)),
                ('WardCapacity', models.IntegerField()),
                ('Population', models.IntegerField()),
                ('WardClerk', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wardclerk.wardclerk')),
            ],
        ),
        migrations.CreateModel(
            name='WardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BedNo', models.IntegerField()),
                ('Description', models.CharField(max_length=500)),
                ('JoinedDate', models.DateField()),
                ('LeftDate', models.DateField()),
                ('Appointment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='receptionist.doctorpatientassignment')),
                ('Patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('WardNo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wardclerk.ward')),
            ],
        ),
    ]