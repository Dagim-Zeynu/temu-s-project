# from django.contrib import admin
# from .models import Medical_device_inventory, Corrective_maintenance, Preventive_maintenance


# @admin.register(Medical_device_inventory)
# class Medical_device_inventoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',  
#         'model_number',
#         'manufacturer',
#         'status',
#         'serial_number',
#         'location'
#     )
#     search_fields = ('name', 'manufacturer', 'model_number')
#     list_filter = ('status',)

# @admin.register(Corrective_maintenance)
# class Corrective_maintenanceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'model', 'serial_number', 'location', 'created_at')
#     search_fields = ('name', 'model', 'serial_number')
#     list_filter = ('location', 'created_at')



# @admin.register(Preventive_maintenance)
# class PreventiveMaintenanceAdmin(admin.ModelAdmin):
#     list_display = (
#         'name', 
#         'model', 
#         'serial_number', 
#         'created_at', 
#         'updated_at'
#     )
#     search_fields = (
#         'name', 
#         'model', 
#         'serial_number'
#     )
#     list_filter = ('created_at', 'updated_at')


from django.contrib import admin
from .models import Medical_device_inventory, Corrective_maintenance, Preventive_maintenance, MaintenanceAlarm

@admin.register(Medical_device_inventory)
class MedicalDeviceInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_number', 'manufacturer', 'status', 'serial_number', 'location')

@admin.register(Corrective_maintenance)
class CorrectiveMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'location', 'created_at', 'updated_at')

@admin.register(Preventive_maintenance)
class PreventiveMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'created_at', 'updated_at')

@admin.register(MaintenanceAlarm)
class MaintenanceAlarmAdmin(admin.ModelAdmin):
    list_display = ('device', 'severity', 'message', 'created_by', 'created_at')
    list_filter = ('severity', 'created_at')
    search_fields = ('device__name', 'message')
