from service.models import *


class Units(orm_models.TextChoices):
    HOUR = 'h', 'час'
    PIECE = 'p', 'шт.'


class AbstractPrice(orm_models.Model):
    """
    Основа для таблиц изменения цен.
    date_new_price - дата начала действия новой цены
    price - цена
    unit - единица измерения (шт, час) для расчета стоимости - выбор
    """
    date_new_price = orm_models.DateField(default=datetime.now, help_text='Дата изменения цены',
                                          verbose_name='Дата изменения цены')
    price = orm_models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text='Цена',
                                    verbose_name='Цена')
    unit = orm_models.CharField(max_length=1, choices=Units.choices, default=Units.HOUR,
                                help_text='Единица измерения', verbose_name='Единица измерения')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.price} руб/{self.unit.get_units_display()} с {self.date_new_price}'


class PriceLocation(AbstractPrice):
    """
    Данные о ценах помещений
    location_id - ссылка на экземпляр данных о помещении
    """
    location_id = orm_models.ForeignKey(to='Location', on_delete=orm_models.CASCADE,
                                        related_name='price_of_space',
                                        help_text='Помещение', verbose_name='Помещение')

    class Meta:
        verbose_name = "Цена на помещение"


class PriceAdditional(AbstractPrice):
    """
    Данные о ценах на дополнителные помещения
    additional_id - ссылка на экземпляр данных о дополнительном помещении
    """
    additional_id = orm_models.ForeignKey(to='Option', on_delete=orm_models.CASCADE,
                                          related_name='price_of_option',
                                          help_text='Доп. помещение', verbose_name='Доп. помещение')

    class Meta:
        verbose_name = 'Цена на дополнительное помещение'
