# Generated by Django 3.2.1 on 2021-05-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlMeasures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hazards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Minor Works', 'MW'), ('Construction', 'C')], max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swms_manager.site')),
            ],
        ),
        migrations.CreateModel(
            name='SwmsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Swms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swms_manager.job')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='swms_manager.site')),
            ],
        ),
        migrations.CreateModel(
            name='JobTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('hazard_risk', models.CharField(max_length=100, null=True)),
                ('control_risk', models.CharField(max_length=100, null=True)),
                ('responsible_person', models.CharField(max_length=100, null=True)),
                ('control_measures', models.ManyToManyField(to='swms_manager.ControlMeasures')),
                ('hazards', models.ManyToManyField(to='swms_manager.Hazards')),
            ],
        ),
    ]
