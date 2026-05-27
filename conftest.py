from core.clients.api_client import ApiClient
import pytest
from datetime import datetime, timedelta
from faker import Faker

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()
    client.auth()
    return client

@pytest.fixture
def booking_dates():
    today = datetime.today()
    checkin_date = today + timedelta(days=10)
    checkout_date = checkin_date + timedelta(days=5)

    return {
        "checkin": checkin_date.strftime("%Y-%m-%d"),
        "checkout": checkout_date.strftime("%Y-%m-%d")
    }

@pytest.fixture
def generate_booking_data_without_bookingdates():
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_int(min=100, max=999)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": None,
        "additionalneeds": additionalneeds
    }
    return data


@pytest.fixture
def generate_booking_data_with_wrong_dates_format():
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_int(min=100, max=999)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": 12345,
        "additionalneeds": additionalneeds
    }
    return data



@pytest.fixture
def generate_booking_data(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_int(min=100, max=999)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : depositpaid,
        "bookingdates" : booking_dates,
        "additionalneeds" : additionalneeds
    }
    return data

@pytest.fixture
def generate_booking_data_with_negative_sum(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_int(min=-999, max=-100)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : depositpaid,
        "bookingdates" : booking_dates,
        "additionalneeds" : additionalneeds
    }
    return data

@pytest.fixture
def generate_booking_data_with_wrong_depositpaid_format(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_int(min=-999, max=-100)
    additionalneeds = faker.sentence()

    data = {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : "depositpaid",
        "bookingdates" : booking_dates,
        "additionalneeds" : additionalneeds
    }
    return data

@pytest.fixture
def generate_booking_data_with_float_sum(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.pyfloat(min_value=-100.25, max_value=-0.001)
    additionalneeds = faker.sentence()

    data = {
        "firstname" : firstname,
        "lastname" : lastname,
        "totalprice" : totalprice,
        "depositpaid" : "depositpaid",
        "bookingdates" : booking_dates,
        "additionalneeds" : additionalneeds
    }
    return data