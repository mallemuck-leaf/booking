from service.models import *


class Connection(orm_models.TextChoices):
    """
    Предпочтительные способы связи (для опции выбора)
    """
    PHONE = 'p', 'телефон'
    TELEGRAM = 't', 'телеграм'
    WHATSAPP = 'w', 'whatsapp'
    VIBER = 'v', 'viber'
    INSTAGRAM = 'i', 'инстаграм'
    EMAIL = 'e', 'эл. почта'


class Units(orm_models.TextChoices):
    """
    Единицы для вывода стоимости
    """
    HOUR = 'h', 'час'
    PIECE = 'p', 'шт.'


class TimeStatus(orm_models.TextChoices):
    """
    Состояние брони
    """
    VACANCY = 'v', 'свободно'
    OCCUPIED = 'o', 'забронировано'
    UNAVAILABLE = 'u', 'недоступно'


class BookingStatus(orm_models.TextChoices):
    """
    Состояние брони
    """
    NEW = 'n', 'новое'
    CANCELLED = 'c', 'отменено'
    CONFIRMED = 'f', 'подтверждено'
