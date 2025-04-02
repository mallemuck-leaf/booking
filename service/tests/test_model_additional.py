from django.test import TestCase
from service.models import Additional


class AdditionalTestCase(TestCase):
    """
    Тестирование модели Additional
    """
    def setUp(self):
        self.true_data = {'name': 'Каминный зал',
                          'description': 'Зал с камином',
                          'all_count': 20
                          }
        self.additional_true = Additional.objects.create(
            name=self.true_data['name'],
            description=self.true_data['description'],
            all_count=self.true_data['all_count'],
        )

    def test_str_method(self):
        """
        Проверка метода __str__
        :return:
        True
        """
        self.assertEqual(str(self.additional_true), self.additional_true.name)
