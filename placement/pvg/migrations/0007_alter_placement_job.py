# Generated by Django 5.0.1 on 2024-03-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvg', '0006_remove_placement_placement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='job',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
