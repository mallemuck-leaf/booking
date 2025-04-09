from django.test import TestCase
from service.models import Location
import pytest


class LocationTestCase(TestCase):
    """
    Тестирование модели Location
    """

    def setUp(self):
        self.true_data = {'name': 'Каминный зал',
                          'description': 'Зал с камином',
                          'max_occupancy': 20,
                          'area': 9}
        # self.false_data = {'name': 'Каминный зал'*5,
        #                    'description': 'Зал с камином'*100,
        #                    'max_occupancy': 20.3,
        #                    'area': 10.5}
        self.location_true = Location.objects.create(
            name=self.true_data['name'],
            description=self.true_data['description'],
            max_occupancy=self.true_data['max_occupancy'],
            area=self.true_data['area'],
        )

    def test_str_method(self):
        """
        Проверка метода __str__
        :return:
        True
        """
        self.assertEqual(str(self.location_true), self.location_true.name)


@pytest.mark.django_db
class TestLocationModel:
    def test_str_method(self, location_model):
        location_object = Location.objects.get(pk=1)
        assert str(location_object) == location_object.name