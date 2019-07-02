from django.contrib import admin


from .models import KCX
from .models import Amber

@admin.register(Amber)
class AmberAdmin(admin.ModelAdmin):
    list_display = ('controller','serial_number','checked_date')
    list_filter = ('controller','serial_number','checked_date')

admin.site.register(KCX)
