# Generated by Django 3.2.7 on 2022-03-27 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20220327_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='department',
            new_name='Department',
        ),
    ]
