# Generated by Django 5.1.4 on 2025-01-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corrective_maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Equipment Name')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Serial Number')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('problem_area', models.TextField(max_length=1000, verbose_name='Problem Area')),
                ('cause_of_failure', models.TextField(max_length=1000, verbose_name='Cause of Failure')),
                ('action_taken', models.TextField(max_length=1000, verbose_name='Action Taken')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Reported At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
        ),
    ]