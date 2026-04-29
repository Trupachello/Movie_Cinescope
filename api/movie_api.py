from custom_requester.custom_requester import CustomRequester
from constants import MOVIE_ENDPOINT

class MovieAPI(CustomRequester):
    """
    Класс для работы с API фильмов.
    """

    def __init__(self, session):
        super().__init__(session = session,base_url="https://api.dev-cinescope.coconutqa.ru/")


    def get_movie_info(self, movie_id, expected_status = 200):
        """
        Получение информации о фильме.
        :param movie_id: ID фильма.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method = "GET",
            endpoint = f'{MOVIE_ENDPOINT}/{movie_id}',
            expected_status = expected_status
        )

    def get_movie_poster(self, data, expected_status = 200):
        return self.send_request(
            method = "GET",
            endpoint = f'{MOVIE_ENDPOINT}',
            params = data,
            expected_status = expected_status
        )

    def delete_movie(self, movie_id, expected_status = 200):
        """
        Удаление фильма.
        :param movie_id: ID фильма.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method = "DELETE",
            endpoint = f'{MOVIE_ENDPOINT}/{movie_id}',
            expected_status = expected_status
        )

    def create_movie(self, movie_data, expected_status = 201):
        return self.send_request(
            method = "POST",
            endpoint = f'{MOVIE_ENDPOINT}',
            data = movie_data,
            expected_status = expected_status
        )

    def update_movie(self, movie_id, update_data, expected_status = 200):
        return self.send_request(
            method = "PATCH",
            endpoint = f'{MOVIE_ENDPOINT}/{movie_id}',
            data = update_data,
            expected_status = expected_status
        )

