# Generated by Django 3.2.1 on 2021-05-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0024_auto_20210524_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobTaskDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, null=True)),
                ('hazards', models.CharField(max_length=400, null=True)),
                ('hazard_risk', models.CharField(choices=[('1L', '1L'), ('2M', '2M'), ('3H', '3H'), ('4A', '4A')], max_length=100, null=True)),
                ('control_measures', models.CharField(max_length=400, null=True)),
                ('control_risk', models.CharField(choices=[('1L', '1L'), ('2M', '2M'), ('3H', '3H'), ('4A', '4A')], max_length=100, null=True)),
                ('responsible_person', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SwmsGroupDefault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('job_task', models.ManyToManyField(to='swms_manager.JobTaskDefault')),
            ],
        ),
        migrations.RemoveField(
            model_name='jobtask',
            name='control_measures',
        ),
        migrations.RemoveField(
            model_name='jobtask',
            name='hazards',
        ),
        migrations.RemoveField(
            model_name='swmsgroup',
            name='job_task',
        ),
        migrations.RemoveField(
            model_name='swmsgroup',
            name='swms',
        ),
        migrations.DeleteModel(
            name='ControlMeasure',
        ),
        migrations.DeleteModel(
            name='Hazard',
        ),
        migrations.DeleteModel(
            name='JobTask',
        ),
        migrations.DeleteModel(
            name='SwmsGroup',
        ),
    ]
