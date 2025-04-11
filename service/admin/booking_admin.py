from service.admin import *
from django.forms import CheckboxSelectMultiple
from django.db import models


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('booking_start_datetime', 'booking_duration',
                    'get_booking_location', 'get_booking_additional',
                    'number_of_persons', 'booking_guest', 'booking_status', 'promocode_id')

    def get_booking_location(self, instance):
        return [str(location) for location in instance.booking_location.all()]

    def get_booking_additional(self, instance):
        return [str(additional) for additional in instance.booking_additional.all()]

    get_booking_location.short_description = 'Помещения'
    get_booking_additional.short_description = 'Доп. услуги'
