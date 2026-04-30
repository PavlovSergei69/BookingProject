from core.clients.api_client import APIClient
import pytest
from datetime import datetime, timedelta
from faker import Faker


@pytest.fixture(scope="session")
#scope диапазон работы, в рамках данной сессии
def api_client():
    client = APIClient()
    #подтягивает данные с класса APIclient
    client.auth()
    return client


@pytest.fixture
def booking_dates():
#генерирует даты после текущей даты работы автотеста, чтобы каждый раз новые даты не придумывать
    today = datetime.today()
    checkin_date = today+timedelta(days=10)
    checkout_date = checkin_date +timedelta(days=5)
    return {
        "checkin": checkin_date.strftime('%y-%m-%d'),
        "checkout": checkout_date.strftime('%y-%m-%d')
    }


@pytest.fixture
def generate_random_booking_data(booking_dates):
#генерирует нового клиента
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": booking_dates,
        "additionalneeds": additionalneeds
    }

    return data
