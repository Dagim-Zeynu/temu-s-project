from django.contrib import admin
from .models import Medical_device_inventory, Corrective_maintenance, Preventive_maintenance


@admin.register(Medical_device_inventory)
class Medical_device_inventoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',  
        'model_number',
        'manufacturer',
        'status',
        'serial_number',
        'location'
    )
    search_fields = ('name', 'manufacturer', 'model_number')
    list_filter = ('status',)

@admin.register(Corrective_maintenance)
class Corrective_maintenanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'location', 'created_at')
    search_fields = ('name', 'model', 'serial_number')
    list_filter = ('location', 'created_at')



@admin.register(Preventive_maintenance)
class PreventiveMaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'model', 
        'serial_number', 
        'created_at', 
        'updated_at'
    )
    search_fields = (
        'name', 
        'model', 
        'serial_number'
    )
    list_filter = ('created_at', 'updated_at')
