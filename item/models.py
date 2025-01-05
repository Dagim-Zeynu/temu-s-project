from django.db import models
from django.contrib.auth.models import User

class Medical_device_inventory(models.Model):
    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50, default='Unknown')
    manufacturer = models.CharField(max_length=100, default='Unknown')
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('unavailable', 'Unavailable'),
            ('maintenance', 'Maintenance')
        ],
        default='available'
    )
    serial_number = models.CharField(max_length=50, unique=True, default='Unknown')
    location = models.CharField(max_length=200, default='Unknown')
    photo = models.ImageField(upload_to='item_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Corrective_maintenance(models.Model):
    name = models.CharField(max_length=100, verbose_name="Equipment Name")
    model = models.CharField(max_length=100, verbose_name="Model")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Serial Number")
    location = models.CharField(max_length=100, verbose_name="Location")
    problem_area = models.TextField(max_length=1000, verbose_name="Problem Area")
    cause_of_failure = models.TextField(max_length=1000, verbose_name="Cause of Failure")
    action_taken = models.TextField(max_length=1000, verbose_name="Action Taken")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Reported At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return f"{self.name} - {self.serial_number}"


class Preventive_maintenance(models.Model):
    name = models.CharField(max_length=100, verbose_name="Equipment Name")
    model = models.CharField(max_length=100, verbose_name="Model")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Serial Number")
    description_of_maintenance_task_performed = models.TextField(
        max_length=1000, 
        verbose_name="Description of Maintenance Task Performed"
    )
    who_performed_the_maintenance = models.TextField(
        max_length=1000, 
        verbose_name="Who Performed the Maintenance"
    )
    how_often_the_maintenance_task_was_performed = models.TextField(
        max_length=1000, 
        verbose_name="How Often the Maintenance Task Was Performed"
    )
    dates_the_maintenace_task_was_performed_during_internship = models.TextField(
        max_length=1000, 
        verbose_name="Dates the Maintenance Task Was Performed During Internship"
    )
    steps_taken_to_ensure_continued_performance_of_maintenance_task = models.TextField(
        max_length=1000, 
        verbose_name="Steps Taken to Ensure Continued Performance of Maintenance Task"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Reported At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return f"{self.name} - {self.serial_number}"
