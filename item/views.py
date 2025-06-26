from django.shortcuts import render, get_object_or_404, redirect
from .models import Medical_device_inventory, Corrective_maintenance, Preventive_maintenance, MaintenanceAlarm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def item_list(request):
    items = Medical_device_inventory.objects.all()
    return render(request, 'item_list.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Medical_device_inventory, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})

# View to list all maintenance records
def maintenance_list(request):
    records = Corrective_maintenance.objects.all()
    return render(request, 'maintenance_list.html', {'records': records})

# View to create a new maintenance record
def create_maintenance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        serial_number = request.POST.get('serial_number')
        location = request.POST.get('location')
        problem_area = request.POST.get('problem_area')
        cause_of_failure = request.POST.get('cause_of_failure')
        action_taken = request.POST.get('action_taken')

        Corrective_maintenance.objects.create(
            name=name,
            model=model,
            serial_number=serial_number,
            location=location,
            problem_area=problem_area,
            cause_of_failure=cause_of_failure,
            action_taken=action_taken
        )
        return redirect('maintenance_list')

    return render(request, 'create_maintenance.html')



# Preventive Maintenance List View
def preventive_maintenance_list(request):
    records = Preventive_maintenance.objects.all()
    return render(request, 'preventive_maintenance_list.html', {'records': records})

# Create Preventive Maintenance Record View
def create_preventive_maintenance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        serial_number = request.POST.get('serial_number')
        description = request.POST.get('description_of_maintenance_task_performed')
        who_performed = request.POST.get('who_performed_the_maintenance')
        how_often = request.POST.get('how_often_the_maintenance_task_was_performed')
        dates = request.POST.get('dates_the_maintenace_task_was_performed_during_internship')
        steps = request.POST.get('steps_taken_to_ensure_continued_performance_of_maintenance_task')
        
        Preventive_maintenance.objects.create(
            name=name,
            model=model,
            serial_number=serial_number,
            description_of_maintenance_task_performed=description,
            who_performed_the_maintenance=who_performed,
            how_often_the_maintenance_task_was_performed=how_often,
            dates_the_maintenace_task_was_performed_during_internship=dates,
            steps_taken_to_ensure_continued_performance_of_maintenance_task=steps,
        )
    return redirect('preventive_maintenance_list')
def alarm_list(request):
    alarms = MaintenanceAlarm.objects.all().order_by('-created_at')
    return render(request, 'alarm_list.html', {'alarms': alarms})

