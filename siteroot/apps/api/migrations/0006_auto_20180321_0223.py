# Generated by Django 2.0.2 on 2018-03-21 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180321_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='time_completed',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='time_commenced',
            new_name='start_time',
        ),
    ]
