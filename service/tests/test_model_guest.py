import pytest


@pytest.mark.django_db
@pytest.mark.usefixtures('guest_model')
class TestGuestModel:

    def test_str_method(self):
        assert str(self.guest_object) == self.guest_object_assert


# @pytest.mark.usefixtures('guest_model')
# def test_str_method(self):
#     assert str(self.guest_object) == self.guest_object_assert
