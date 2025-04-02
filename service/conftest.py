import pytest
from service import models


@pytest.fixture
def guest_model(request):
    data = {
        'name': 'Антон',
        'organization': 'InnoClass',
    }
    request.cls.guest_object = models.Guest.objects.create(
        name=data['name'],
        organization=data['organization'],
    )
    request.cls.guest_object_assert = data['name']
