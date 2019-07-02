from django.contrib import admin
from .models import Check

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('controller','unit_type','serial_number','checked_date')
    list_filter = ('controller','unit_type','serial_number','checked_date')