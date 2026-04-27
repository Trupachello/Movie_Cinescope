
from faker import Faker
import pytest
import requests
import random
from constants import BASE_URL, REGISTER_ENDPOINT
from custom_requester.custom_requester import CustomRequester
from utils.data_generator import DataGenerator
from api.api_manager import ApiManager

faker = Faker()

@pytest.fixture(scope="session")
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": ["USER"]
    }

@pytest.fixture(scope="session")
def test_film():
    film_name = DataGenerator.generate_film_name()
    img_url = DataGenerator.generate_img_url()
    film_description = DataGenerator.generate_film_description()
    price = DataGenerator.generate_film_price()
    return {
        "name": film_name,
        "imageUrl": img_url,
        "price": price,
        "description": film_description,
        "location": random.choice(["SPB","MSK"]),
        "published": faker.boolean(),
        # "published": True,
        "genreId": faker.random_int(min = 1, max = 10)
    }

@pytest.fixture(scope="session")
def test_poster():
    min_price = faker.random_int(min = 1, max = 100)
    max_price = faker.random_int(min = min_price, max = min_price + 1000)
    return {
        "pageSize": random.randint(1, 20),
        "page": random.randint(1, 5),
        "minPrice": min_price,
        "maxPrice": max_price,
        "location": random.choice(["SPB", "MSK"]),
        "published": faker.boolean(),
        "genreId": faker.random_int(min=1, max=10),
        "createdAt": random.choice(["asc", "desc"])
    }

@pytest.fixture(scope="session")
def registered_user(requester, test_user):
    """
    Фикстура для регистрации и получения данных зарегистрированного пользователя.
    """
    response = requester.send_request(
        method="POST",
        endpoint=REGISTER_ENDPOINT,
        data=test_user,
        expected_status=201
    )
    response_data = response.json()
    registered_user = test_user.copy()
    registered_user["id"] = response_data["id"]
    return registered_user

@pytest.fixture(scope="session")
def existed_movie(api_manager, test_film):
    api_manager.auth_api.authenticate_super_admin()
    response = api_manager.movie_api.create_movie(test_film)
    response_data = response.json()
    existed_movie = test_film.copy()
    existed_movie["id"] = response_data["id"]
    yield existed_movie
    api_manager.movie_api.delete_movie(existed_movie["id"], expected_status = None)

@pytest.fixture(scope="session")
def requester(url = BASE_URL):
    """
    Фикстура для создания экземпляра CustomRequester.
    """
    session = requests.Session()
    return CustomRequester(session = session, base_url = url)

@pytest.fixture(scope="session")
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()

@pytest.fixture(scope="session")
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)