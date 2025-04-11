from service.admin import *


class AbstractAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(AbstractAreaAdmin):
    def get_list_display(self, request):
        return self.list_display + ('max_occupancy', 'area')


@admin.register(Additional)
class AdditionalAdmin(AbstractAreaAdmin):
    def get_list_display(self, request):
        return self.list_display + ('all_count',)
