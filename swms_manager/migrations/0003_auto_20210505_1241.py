# Generated by Django 3.2.1 on 2021-05-05 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0002_controlmeasures_hazards_job_jobtask_swms_swmsgroup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ControlMeasures',
            new_name='ControlMeasure',
        ),
        migrations.RenameModel(
            old_name='Hazards',
            new_name='Hazard',
        ),
    ]
