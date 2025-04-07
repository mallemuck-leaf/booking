from service.models import *


class Booking(orm_models.Model):
    """
    Бронирование помещения
    """
    # booking_datetime = orm_models.ForeignKey('BookingTime', on_delete=orm_models.PROTECT,
    #                                          help_text='Дата и время бронирования',
    #                                          verbose_name='Дата и время бронирования')
    booking_start_date = orm_models.DateField(verbose_name='Дата начала бронирования',
                                              help_text='Дата начала бронирования')
    booking_start_time = orm_models.TimeField(verbose_name='Время начала бронирования',
                                              help_text='Время начала бронирования')
    booking_duration = orm_models.PositiveSmallIntegerField(verbose_name='Продолжительность бронирования',
                                                            help_text='Продолжительнось бронирования, в минутах',
                                                            default=30)
    booking_location = orm_models.ManyToManyField('Location', blank=True, related_name='locations',
                                                  help_text='Помещение', verbose_name='Помещение')
    booking_additional = orm_models.ManyToManyField('Additional', blank=True, related_name='additional',
                                                    help_text='Дополнения', verbose_name='Дополнения')
    number_of_persons = orm_models.PositiveSmallIntegerField(blank=True, null=True,
                                                             help_text='Количество гостей',
                                                             verbose_name='Количество гостей')
    booking_guest = orm_models.ForeignKey('Guest', on_delete=orm_models.PROTECT)
    booking_status = orm_models.CharField(max_length=1, choices=BookingStatus.choices,
                                          default=BookingStatus.NEW)
    promocode_id = orm_models.ForeignKey('Promocode', on_delete=orm_models.PROTECT)

    class Meta:
        verbose_name = 'Бронирование'

    def __str__(self):
        # location = Location.objects.get(pk=self.booking_location)
        return f'{self.booking_start_date} {self.booking_start_time}'

    def get_booking_time(self):
        if self.booking_status is BookingStatus.CONFIRMED:
            booking_start_time = self.booking_start_time - timedelta(hours=0.5)
            booking_end_time = self.booking_start_time + timedelta(hours=self.booking_duration/30 + 0.5)
            return self.booking_start_date, booking_start_time, booking_end_time, self.booking_duration
        else:
            return self.booking_start_date, self.booking_start_time, self.booking_duration


# class BookingAdditional(orm_models.Model):
#     """
#     Дополнителные опции к брони
#     """
#     booking_id = orm_models.ForeignKey('Booking', on_delete=orm_models.CASCADE)
#     additional_id = orm_models.ForeignKey('Additional', on_delete=orm_models.CASCADE)
#     additional_quantity = orm_models.PositiveSmallIntegerField(default=1)
#
#     def __str__(self):
#         booking = Booking.objects.get(pk=self.booking_id)
#         additional = Additional.objects.get(pk=self.additional_id)
#         return f'{str(booking)}: {str(additional)} x {self.additional_quantity}'

