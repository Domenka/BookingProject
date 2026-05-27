import allure
from core.schemas.booking_schema import BOOKING_SCHEMA
import jsonschema
from core.models.booking import BookingResponse
from pydantic import ValidationError


@allure.feature("Test creation Booking")
@allure.story("Positive: Create booking with custom data")
def test_create_booking_with_custom_data(api_client, generate_booking_data):
    response = api_client.create_booking(generate_booking_data)
    with allure.step("Assert status code"):
        assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"
        with allure.step("Assert format and content from response"):
            assert isinstance(response.json(), dict)
            jsonschema.validate(response.json(), BOOKING_SCHEMA)

@allure.feature("Test creation Booking")
@allure.story("Positive: Create booking with custom data and verify via pydantic")
def test_create_booking_with_custom_data_pydantic(api_client, generate_booking_data):
    response = api_client.create_booking(generate_booking_data)
    with allure.step("Assert status code"):
        assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"
        with allure.step("Assert format and content from response"):
           try:
               BookingResponse(**response.json())
           except ValidationError as e:
               raise ValueError(f"Response validation failed {e}")

           assert response.json()["booking"]["firstname"] == generate_booking_data["firstname"]
           assert response.json()["booking"]["lastname"] == generate_booking_data["lastname"]
           assert response.json()["booking"]["totalprice"] == generate_booking_data["totalprice"]
           assert response.json()["booking"]["depositpaid"] == generate_booking_data["depositpaid"]
           assert response.json()["booking"]["bookingdates"]["checkin"] == generate_booking_data["bookingdates"]["checkin"]
           assert response.json()["booking"]["bookingdates"]["checkout"] == generate_booking_data["bookingdates"]["checkout"]
           assert response.json()["booking"]["additionalneeds"] == generate_booking_data["additionalneeds"]

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking with empty data")
def test_create_booking_with_empty_data(api_client):
    response = api_client.create_booking(booking_data={})
    with allure.step("Assert status code"):
     assert response.status_code == 500, f"Expected status code is 200, but got {response.status_code}"
     assert response.text == "Internal Server Error", f"Expected text 'Internal Server Error' but got other"

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking without names")
def test_create_booking_with_empty_data(api_client, generate_booking_data_without_bookingdates):
    response = api_client.create_booking(generate_booking_data_without_bookingdates)
    assert response.status_code == 500, f"Expected status code is 200, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected text 'Internal Server Error' but got other"

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking with wrong date format")
def test_create_booking_with_wrong_dates_format(api_client, generate_booking_data_with_wrong_dates_format):
    response = api_client.create_booking(generate_booking_data_with_wrong_dates_format)
    assert response.status_code == 500, f"Expected status code is 200, but got {response.status_code}"
    assert response.text == "Internal Server Error", f"Expected text 'Internal Server Error' but got other"

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking with negative sum")
def test_create_booking_with_negative_sum(api_client, generate_booking_data_with_negative_sum):
    response = api_client.create_booking(generate_booking_data_with_negative_sum)
    assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking with wrong depositpaid format")
def test_create_booking_with_negative_sum(api_client, generate_booking_data_with_wrong_depositpaid_format):
    response = api_client.create_booking(generate_booking_data_with_wrong_depositpaid_format)
    assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"

@allure.feature("Test creation Booking")
@allure.story("Negative: Create booking with  float sum")
def test_create_booking_with_negative_sum(api_client, generate_booking_data_with_float_sum):
    response = api_client.create_booking(generate_booking_data_with_float_sum)
    assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"












