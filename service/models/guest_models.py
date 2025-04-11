from service.models import *


class Guest(orm_models.Model):
    """
    Модель для данных клиента
    """
    name = orm_models.CharField(max_length=30, help_text='Имя', verbose_name='Имя')
    organization = orm_models.CharField(max_length=50, help_text='Организация',
                                        verbose_name='Организация',
                                        null=True, blank=True, default=None)
    communication_method = orm_models.CharField(max_length=1, choices=Connection.choices,
                                                default=Connection.PHONE,
                                                help_text='Предпочтительный способ связи',
                                                verbose_name='Предпочтительный способ связи')
    phone_number = orm_models.CharField(max_length=12, help_text='Номер телефона',
                                        verbose_name='Номер телефона', default=None,
                                        null=True, blank=True)
    telegram_account = orm_models.CharField(max_length=12, help_text='аккаунт в телеграм',
                                            verbose_name='Telegram', default=None,
                                            null=True, blank=True)
    # viber_account = orm_models.CharField(max_length=12, help_text='аккаунт в вайбер',
    #                                      verbose_name='Viber', default=None,
    #                                      null=True, blank=True)
    # whatsapp_account = orm_models.CharField(max_length=12, help_text='аккаунт в ватсап',
    #                                         verbose_name='Whatsapp', default=None,
    #                                         null=True, blank=True)
    instagram_account = orm_models.CharField(max_length=12, help_text='аккаунт в инстаграм',
                                             verbose_name='Instagram', default=None,
                                             null=True, blank=True)
    email = orm_models.CharField(max_length=12, help_text='электронная почта',
                                 verbose_name='Email', default=None,
                                 null=True, blank=True)
    telegram_chat_id = orm_models.CharField(max_length=15, help_text='Идентификатор чата в ТГ',
                                            verbose_name='Идентификатор чата в ТГ',
                                            default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return f'{self.name}'
