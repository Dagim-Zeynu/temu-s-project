# Generated by Django 5.1.4 on 2025-01-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_corrective_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preventive_maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Equipment Name')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Serial Number')),
                ('description_of_maintenance_task_performed', models.TextField(max_length=1000, verbose_name='Description of Maintenance Task Performed')),
                ('who_performed_the_maintenance', models.TextField(max_length=1000, verbose_name='Who Performed the Maintenance')),
                ('how_often_the_maintenance_task_was_performed', models.TextField(max_length=1000, verbose_name='How Often the Maintenance Task Was Performed')),
                ('dates_the_maintenace_task_was_performed_during_internship', models.TextField(max_length=1000, verbose_name='Dates the Maintenance Task Was Performed During Internship')),
                ('steps_taken_to_ensure_continued_performance_of_maintenance_task', models.TextField(max_length=1000, verbose_name='Steps Taken to Ensure Continued Performance of Maintenance Task')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Reported At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
        ),
    ]
