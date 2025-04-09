import pytest
from service.models import Guest


@pytest.mark.django_db
class TestGuestModel:

    def test_str_method(self, guest_model):
        guest_object = Guest.objects.get(pk=1)
        assert str(guest_object) == guest_object.name


# @pytest.mark.usefixtures('guest_model')
# def test_str_method(self):
#     assert str(self.guest_object) == self.guest_object_assert
