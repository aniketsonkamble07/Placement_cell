# Generated by Django 4.1.3 on 2024-01-29 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pvg', '0007_student_student_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
    ]
