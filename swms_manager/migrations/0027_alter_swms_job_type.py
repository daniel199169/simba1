# Generated by Django 3.2.1 on 2021-05-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0026_jobtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swms',
            name='job_type',
            field=models.CharField(choices=[('MW', 'MW'), ('C', 'C'), ('M', 'M')], max_length=100, null=True),
        ),
    ]
