# Generated by Django 3.2.1 on 2021-05-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0004_alter_controlmeasure_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlmeasure',
            name='name',
            field=models.CharField(max_length=400, null=True),
        ),
    ]