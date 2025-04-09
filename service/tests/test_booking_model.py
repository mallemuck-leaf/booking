import pytest
from service.models import *


@pytest.mark.django_db
class TestBookingModel:
    def test_get_booking_time_method(self, booking_model):
        booking_object = Booking.objects.get(pk=1)
        assert booking_object.booking_status == BookingStatus.CONFIRMED
        assert booking_object.get_booking_time() == self.time_assert_true
