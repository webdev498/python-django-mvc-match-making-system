# Generated by Django 2.0.2 on 2018-03-21 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180321_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_role',
            old_name='role_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='report',
            name='sent_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_by_report', to='api.Profile'),
        ),
    ]
