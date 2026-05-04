
from faker import Faker
import pytest
import requests
import random
from utils.data_generator import DataGenerator
from api.api_manager import ApiManager

faker = Faker()

@pytest.fixture(scope="function")
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
        "genreId": faker.random_int(min = 1, max = 10)
    }

@pytest.fixture(scope="function")
def test_list_movies():
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

@pytest.fixture(scope="function")
def existed_movie(api_manager, test_film):
    api_manager.auth_api.authenticate_super_admin()
    response = api_manager.movie_api.create_movie(test_film)
    response_data = response.json()
    existed_movie = test_film.copy()
    existed_movie["id"] = response_data["id"]
    yield existed_movie
    api_manager.movie_api.delete_movie(existed_movie["id"], expected_status = None)
    api_manager.auth_api.logout_user()

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

@pytest.fixture(scope="function")
def unauthenticated_api_manager():
    """
    Фикстура для создания экземпляра ApiManager.
    """
    http_session = requests.Session()
    yield ApiManager(http_session)
    http_session.close()