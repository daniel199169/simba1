# Generated by Django 3.2.1 on 2021-05-05 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swms_manager', '0010_auto_20210505_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swms',
            old_name='name',
            new_name='efs_name',
        ),
        migrations.RenameField(
            model_name='swms',
            old_name='phone_number',
            new_name='efs_phone_number',
        ),
        migrations.RenameField(
            model_name='swms',
            old_name='signature',
            new_name='efs_signature',
        ),
    ]
