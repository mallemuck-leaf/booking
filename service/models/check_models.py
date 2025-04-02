from service.models import *


class Check(orm_models.Model):
    """
    Чек брони с учетом промокодов
    """
    booking_id = orm_models.ForeignKey('Booking', on_delete=orm_models.CASCADE,
                                       help_text='Бронь', verbose_name='Бронь')
    check_location = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                             help_text='Стоимость бронирования помещения без промокода',
                                             verbose_name='Стоимость бронирования помещения без промокода')
    check_additionals = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                                help_text='Стоимость доп. опций без промокода',
                                                verbose_name='Стоимость доп. опций без промокода')
    check_location_with_promo = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                                        help_text='Стоимость бронирования помещения c промокодом',
                                                        verbose_name='Стоимость бронирования помещения c промокодом')
    check_additionals_with_promo = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                                           help_text='Стоимость доп. опций c промокодом',
                                                           verbose_name='Стоимость доп. опций c промокодом')
    check_all = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                        help_text='Итоговый чек без промокода',
                                        verbose_name='Итоговый чек без промокода')
    check_all_with_promo = orm_models.DecimalField(decimal_places=2, max_digits=8,
                                                   help_text='Итоговый чек без промокодом',
                                                   verbose_name='Итоговый чек без промокодом')

    class Meta:
        verbose_name = 'Чек'

    def __str__(self):
        return f'{self.check_all} byn.'
