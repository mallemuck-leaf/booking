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


class BookingTime(orm_models.Model):
    """
    Учет занятого времени
    time_00 .. time_23 - состояние часа (занято/свободно/недоступно)
    """
    booking_date = orm_models.DateField(primary_key=True, help_text='Дата бронирования',
                                        verbose_name='Дата бронирования')
    # booking_date_id = orm_models.ForeignKeyField('BookingDate', on_delete=orm_models.CASCADE,
    #                                              related_name='booking_date_time',
    #                                              help_text='дата бронирования',
    #                                              verbose_name='дата бронирования')
    time_00 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_01 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_02 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_03 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_04 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_05 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_06 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_07 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_08 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_09 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_10 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_11 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_12 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_13 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_14 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_15 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_16 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_17 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_18 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_19 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_20 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_21 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_22 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)
    time_23 = orm_models.CharField(max_length=1, choices=Status.choices, default=Status.VACANCY)

    class Meta:
        verbose_name = 'Дата и время бронирования'

    def __str__(self):
        return f'{self.booking_date}'
