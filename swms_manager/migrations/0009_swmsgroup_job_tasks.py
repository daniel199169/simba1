# Generated by Django 3.2.1 on 2021-05-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0008_alter_jobtask_responsible_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='swmsgroup',
            name='job_tasks',
            field=models.ManyToManyField(to='swms_manager.JobTask'),
        ),
    ]
