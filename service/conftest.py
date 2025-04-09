import pytest
from service import models


@pytest.fixture
def guest_model():
    data = {
        'name': 'Антон',
        'organization': 'InnoClass',
    }
    models.Guest.objects.create(
        name=data['name'],
        organization=data['organization'],
    )
    # request.cls.guest_object_assert = data['name']


@pytest.fixture
def location_model():
    data = {
        'name': 'Каминный зал',
        'description': 'Уютный зал с камином.',
        'max_occupancy': 30,
        'area': 9,
    }
    models.Location.objects.create(
        name=data['name'],
        description=data['description'],
        max_occupancy=data['max_occupancy'],
        area=data['area'],
    )


@pytest.fixture
def additional_model():
    data = {
        'name': 'Кофемашина',
        'description': 'Вкуснейший капучина.',
        'all_count': 30,
    }
    models.Additional.objects.create(
        name=data['name'],
        description=data['description'],
        all_count=data['all_count'],
    )


@pytest.fixture
def promocode_model():
    data = {
        'name': 'КАПУЧЫНА',
        'description': 'Бесплатный кофе.',
    }
    models.Promocode.objects.create(
        name=data['name'],
        description=data['description'],
    )


@pytest.fixture
def booking_model(promocode_model, additional_model, location_model, guest_model, request):
    promo_obj = models.Promocode.objects.get(pk=1)
    additional_obj = models.Additional.objects.get(pk=1)
    location_obj = models.Location.objects.get(pk=1)
    guest_obj = models.Guest.objects.get(pk=1)
    data = {
        'booking_start_datetime': '2025-11-03 11:30',
        # 'booking_start_date': '2025-11-03',
        # 'booking_start_time': '11:30',
        'booking_duration': 1,
        'numbers_of_person': 15,
    }
    booking_object = models.Booking.objects.create(
        booking_start_datetime=data['booking_start_datetime'],
        # booking_start_time=data['booking_start_time'],
        booking_duration=data['booking_duration'],
        number_of_persons=data['numbers_of_person'],
        # booking_location=location_obj,
        # booking_additional=additional_obj,
        booking_guest=guest_obj,
        promocode_id=promo_obj,
        booking_status=models.BookingStatus.CONFIRMED,
    )
    booking_object.booking_location.add(location_obj)
    booking_object.booking_additional.add(additional_obj)
    request.cls.time_assert_true = (data['booking_start_datetime'][:10], '11:00', '13:00')
