from service.admin import *


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'communication_method',
                    'phone_number', 'email', 'instagram_account',
                    )
    search_fields = ('name', 'organization', 'communication_method')
    list_filter = ['organization', 'communication_method']
