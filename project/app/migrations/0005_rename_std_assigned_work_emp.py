# Generated by Django 5.0.4 on 2024-05-13 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_work_std_assigned_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assigned_work',
            old_name='std',
            new_name='emp',
        ),
    ]