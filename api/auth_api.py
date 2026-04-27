
from custom_requester.custom_requester import CustomRequester
from constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT, ADMIN_USERNAME, ADMIN_PASSWORD, LOGOUT_ENDPOINT

class AuthAPI(CustomRequester):
    """
      Класс для работы с аутентификацией.
      """

    def __init__(self, session):
        super().__init__(session = session, base_url = "https://auth.dev-cinescope.coconutqa.ru/")

    def register_user(self, user_data, expected_status=201):
        """
        Регистрация нового пользователя.
        :param user_data: Данные пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method = "POST",
            endpoint = REGISTER_ENDPOINT,
            data = user_data,
            expected_status = expected_status
        )

    def login_user(self, login_data, expected_status=200):
        """
        Авторизация пользователя.
        :param login_data: Данные для логина.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method = "POST",
            endpoint = LOGIN_ENDPOINT,
            data = login_data,
            expected_status = expected_status
        )

    def logout_user(self, expected_status=200):
        self.send_request(
            method = "GET",
            endpoint = LOGOUT_ENDPOINT,
            expected_status = expected_status
        )
        self._update_session_headers(**{"authorization": ("Bearer " + "")})


    def authenticate(self, user_creds):
        login_data = {
            "email": user_creds[0],
            "password": user_creds[1]
        }

        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]
        self._update_session_headers(**{"authorization": ("Bearer " + token)})

    def authenticate_super_admin(self):
        login_data = {
            "email": ADMIN_USERNAME,
            "password": ADMIN_PASSWORD
        }

        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]
        self._update_session_headers(**{"authorization": ("Bearer " + token)})