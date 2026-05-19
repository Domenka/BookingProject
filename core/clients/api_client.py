from http.client import responses

import requests
import os
from dotenv import load_dotenv
from core.settings.environments import Environment
import allure
from core.clients.endpoints import Endpoints
from core.settings.config import Creds, Timeouts
from core.schemas.booking_schema import BOOKING_SCHEMA
import jsonschema


load_dotenv()

class ApiClient():
    def __init__(self):
        environment_str = os.getenv("ENVIRONMENT")

        try:
            environment = Environment(environment_str)
        except KeyError:
            raise ValueError(f"Unsupported environment value: {environment_str}")

        self.base_url = self.get_base_url(environment)
        self.session = requests.Session()
        self.session.headers = {
            "Content-Type": "application/json"
        }


    def get_base_url(self, environment: Environment) -> str:
        if environment == Environment.TEST:
            return os.getenv('TEST_BASE_URL')

        elif environment == Environment.PROD:
            return os.getenv('PROD_BASE_URL')

        else:
            raise ValueError(f"Unsupported environment: {environment}")


    def get(self, endpoint, params=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code:
            assert response.status_code == status_code
        return response.json()


    def post(self, endpoint, data=None, status_code=200):
        url = self.base_url + endpoint
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code:
            assert response.status_code == status_code
        return response.json()


    def ping(self):
        with allure.step("Ping api client"):
            url = f"{self.base_url}{Endpoints.PING_ENDPOINT}"
            response = self.session.get(url)
            response.raise_for_status()

        with allure.step("Assert status code"):
            assert response.status_code == 201, f"Expected status code is 201, but got {response.status_code}"

        return response.status_code


    def auth(self):
        with allure.step("Getting auth"):
            url = f"{self.base_url}{Endpoints.AUTH_ENDPOINT}"
            payload = {"username": Creds.USERNAME, "passwrod": Creds.PASSWORD}
            response = self.session.post(url, json=payload, timeout=Timeouts.TIMEOUT)
            response.raise_for_status()

        with allure.step("Assert status code"):
            assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"
        token = response.json().get("token")

        with allure.step("Updating header with auth"):
            self.session.headers.update({"Authorization": f"Bearer {token}"})


    def get_booking_by_id(self, booking_id):
        with allure.step("Get booking by id"):
            url = f"{self.base_url}{Endpoints.BOOKING_ENDPOINT/booking_id}"
            response = self.session.get(url)
            response.raise_for_status()

        with allure.step("Assert status code"):
            assert response.status_code == 200, f"Expected status code is 200, but got {response.status_code}"

        with allure.step("Assert format and content from response"):
            assert isinstance(response.json(), dict)
            jsonschema.validate(response.json(), BOOKING_SCHEMA)

            return response.json()

