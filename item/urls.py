from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='items_list'),  # This is the items list page


    path('item/<int:item_id>/', views.item_detail, name='item_detail'),

    path('maintenance/', views.maintenance_list, name='maintenance_list'),

    # Preventive Maintenance URLs
    path('preventive/', views.preventive_maintenance_list, name='preventive_maintenance_list'),
    path('alarm/', views.alarm_list, name='alarm_list'),
]



