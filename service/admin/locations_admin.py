from service.admin import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'max_occupancy', 'area')
