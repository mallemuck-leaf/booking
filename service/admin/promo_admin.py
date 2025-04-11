from service.admin import *


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
