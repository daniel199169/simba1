# Generated by Django 3.2.1 on 2021-05-12 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0021_auto_20210511_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='swmsgroup',
            name='job_task',
            field=models.ManyToManyField(to='swms_manager.JobTask'),
        ),
    ]
