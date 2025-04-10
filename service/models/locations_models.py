from service.models import *


class AbstractArea(orm_models.Model):
    """
    Основа для моделей помещений и доп. опций
    name - название
    description - описание
    """
    name = orm_models.CharField(max_length=20, help_text='Название',
                                verbose_name='Название')
    description = orm_models.TextField(max_length=1000, help_text='Описание',
                                       verbose_name='Описание')

    class Meta:
        abstract = True
        ordering = ['name',]

    def __str__(self):
        return f'{self.name}'


class Location(AbstractArea):
    """
    Информация об основных помещениях
    max_occupancy - вместимость, человек
    area - площадь помещения, в квадратных метрах (целое число)
    """
    max_occupancy = orm_models.PositiveSmallIntegerField(default=10, help_text='Максимальное количество человек',
                                                         verbose_name='Максимальное количество человек')
    area = orm_models.PositiveSmallIntegerField(default=10, help_text='Площадь помещения',
                                                verbose_name='Площадь помещения')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'


class Additional(AbstractArea):
    """
    Информация о дополнительных помещениях
    all_count - общее количество единиц в наличии
    """
    all_count = orm_models.PositiveSmallIntegerField(default=1, help_text='Общее количество',
                                                     verbose_name='Общее количество')

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'
