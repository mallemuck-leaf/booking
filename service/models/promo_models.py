from service.models import *


class Promocode(orm_models.Model):
    """
    Промокоды
    """
    name = orm_models.CharField(max_length=10, unique=True,
                                help_text='Текст промокода', verbose_name='Текст промокода')
    description = orm_models.TextField(max_length=300, null=True, blank=True,
                                       help_text='Описание условий', verbose_name='Описание условий')

    class Meta:
        verbose_name = 'Промокод'

    def __str__(self):
        return f'{self.name}'


class AbstractPromo(orm_models.Model):
    """
    Общий класс для условий промоакций
    """
    promocode_id = orm_models.ForeignKey('Promocode', on_delete=orm_models.PROTECT)
    discont = orm_models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class LocationPromo(AbstractPromo):
    """
    Условия по промокоду для помещений
    """
    location_id = orm_models.ForeignKey('Location', on_delete=orm_models.PROTECT)

    class Meta:
        verbose_name = 'Условия по промокоду для помещений'

    def __str__(self):
        location = Location.objects.get(pk=self.location_id)
        return f'{str(location)}: {self.discont}%'


class AdditionalPromo(AbstractPromo):
    """
    Условия по промокоду для доп. опций
    """
    additional_id = orm_models.ForeignKey('Additional', on_delete=orm_models.PROTECT)

    class Meta:
        verbose_name = 'Условия по промокоду для доп. опций'

    def __str__(self):
        additional = Additional.objects.get(pk=self.additional_id)
        return f'{str(additional)}: {self.discont}%'
