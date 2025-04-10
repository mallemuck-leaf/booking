from service.admin import *


# @admin.register(AbstractArea)
class AbstractAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Location)
class LocationAdmin(AbstractAreaAdmin):
    # list_display = ('name', 'description', 'max_occupancy', 'area')
    def get_list_display(self, request):
        return self.list_display + ('max_occupancy', 'area')


@admin.register(Additional)
class AdditionalAdmin(AbstractAreaAdmin):
    def get_list_display(self, request):
        return self.list_display + ('all_count',)
