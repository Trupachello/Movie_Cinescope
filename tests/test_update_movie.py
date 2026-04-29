class TestUpdateMovie:
    def test_update_movie(self, existed_movie, test_film, api_manager):
        new_data = test_film
        response = api_manager.movie_api.update_movie(existed_movie['id'], new_data, expected_status = 200)
        response_data = response.json()
        assert response_data['id'] == existed_movie['id'],'id фильмов не совпадают'
        for key in new_data:
            assert new_data[key] == response_data[key], f'поле {key} не совпадает'

    def test_update_negative_id(self, test_film, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.update_movie(-5, test_film, expected_status = 404)

    def test_update_zero_id(self, test_film, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.update_movie(0, test_film, expected_status = 404)

    def test_update_string_id(self, test_film, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.update_movie('abc', test_film, expected_status = 404)

    def test_update_wrong_location(self,existed_movie, api_manager):
        data = {"location": "abc"}
        api_manager.movie_api.update_movie(existed_movie['id'], data, expected_status = 400)

    def test_update_string_in_price(self, existed_movie, test_film, api_manager):
        test_film["price"] = 'abc'
        api_manager.movie_api.update_movie(existed_movie['id'], test_film, expected_status = 400)



