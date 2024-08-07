# Generated by Django 5.0.1 on 2024-03-09 17:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvg', '0004_admin_alter_student_cgpa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='is_present',
            field=models.CharField(choices=[('Present', 'Present'), ('Not Present', 'Not Present')], default='Not Present', max_length=20),
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(blank=True, default=None, null=True)),
                ('placement_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('placement_type', models.CharField(choices=[('On Campus', 'On Campus'), ('Off Campus', 'Off Campus')], max_length=20)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pvg.jobdetail')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pvg.student')),
            ],
        ),
    ]
