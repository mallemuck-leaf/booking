from service.models import *


class WorkTimeInfo(orm_models.Model):
    """
    Время работы помещений для аренды
    """
    time_open = orm_models.TimeField(verbose_name='Время начала аренды', help_text='Время начала аренды',
                                     default='08:00')
    time_close = orm_models.TimeField(verbose_name='Время закрытия', help_text='Время закрытия',
                                      default='23:00')
    date_new_times = orm_models.DateField(verbose_name='Дата введения нового режима работы',
                                          help_text='Дата введения нового режима работы')

    class Meta:
        verbose_name = 'Время работы'

    def __str__(self):
        return f'{self.time_open} - {self.time_close} c {self.date_new_times}'


class BookingDate(orm_models.Model):
    """
    Занятые даты календаря
    """
    booking_date = orm_models.DateField(primary_key=True, help_text='Дата бронирования',
                                        verbose_name='Дата бронирования')

    class Meta:
        verbose_name = 'Дата бронирования'

    def __str__(self):
        return f'{self.booking_date}'
