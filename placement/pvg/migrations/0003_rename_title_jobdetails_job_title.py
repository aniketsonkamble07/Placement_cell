# Generated by Django 4.1.3 on 2023-12-09 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pvg', '0002_jobdetails_remove_student_student_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetails',
            old_name='title',
            new_name='job_title',
        ),
    ]