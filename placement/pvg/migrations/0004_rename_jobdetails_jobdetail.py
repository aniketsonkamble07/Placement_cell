# Generated by Django 4.1.3 on 2023-12-09 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pvg', '0003_rename_title_jobdetails_job_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobDetails',
            new_name='JobDetail',
        ),
    ]
