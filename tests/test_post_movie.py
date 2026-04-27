class TestPostMovie():
    def test_create_movie(self, api_manager, test_film):
        api_manager.auth_api.authenticate_super_admin()
        response = api_manager.movie_api.create_movie(test_film)
        response_data = response.json()
        for key in test_film:
            assert test_film[key] == response_data[key], "поле {key} не совпадает"

    def test_create_movie_without_auth(self, api_manager, test_film):
        api_manager.movie_api.create_movie(test_film, expected_status = 401)

    def test_wrong_param_in_body(self, api_manager, test_film):
        api_manager.auth_api.authenticate_super_admin()
        test_film["wrong_data"] = "abc"
        api_manager.movie_api.create_movie(test_film, expected_status = 400)

    def test_create_movie_without_name(self, api_manager, test_film):
        test_film.pop("name")
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.create_movie(test_film, expected_status = 400)

    def test_empty_name(self, api_manager, test_film):
        test_film["name"] = ""
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.create_movie(test_film, expected_status = 400)

    def test_wrong_location(self, api_manager, test_film):
        test_film["location"] = "abc"
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.create_movie(test_film, expected_status = 400)

    def test_string_in_price(self, api_manager, test_film):
        api_manager.auth_api.authenticate_super_admin()
        test_film["price"] = -1
        api_manager.movie_api.create_movie(test_film, expected_status = 400)