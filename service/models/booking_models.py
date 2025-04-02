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
                                                            help_text='Продолжительнось бронирования, в часах',
                                                            default=1)
    booking_location = orm_models.ForeignKey('Location', on_delete=orm_models.PROTECT,
                                             help_text='Помещение', verbose_name='Помещение')
    number_of_persons = orm_models.PositiveSmallIntegerField(blank=True, null=True,
                                                             help_text='Количество гостей',
                                                             verbose_name='Количество гостей')
    booking_guest = orm_models.ForeignKey('Guest', on_delete=orm_models.PROTECT)
    booking_status = orm_models.CharField(max_length=1, choices=BookingStatus.choices,
                                          default=BookingStatus.NEW)

    class Meta:
        verbose_name = 'Бронирование'

    def __str__(self):
        location = Location.objects.get(pk=self.booking_location)
        return f'{self.booking_start_date} {self.booking_start_time} {str(location)}'


class BookingAdditional(orm_models.Model):
    """
    Дополнителные опции к брони
    """
    booking_id = orm_models.ForeignKey('Booking', on_delete=orm_models.CASCADE)
    additional_id = orm_models.ForeignKey('Additional', on_delete=orm_models.CASCADE)
    additional_quantity = orm_models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        booking = Booking.objects.get(pk=self.booking_id)
        additional = Additional.objects.get(pk=self.additional_id)
        return f'{str(booking)}: {str(additional)} x {self.additional_quantity}'

