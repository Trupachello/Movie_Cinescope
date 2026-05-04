class TestGetMovieID:
    def test_get_movie_id(self, api_manager, existed_movie):
        response = api_manager.movie_api.get_movie_info(movie_id = existed_movie['id'], expected_status = 200)
        response_data = response.json()
        assert response_data['id'] == existed_movie['id'], 'id фильмов не совпадают'
        assert response_data['name'] == existed_movie['name'], 'имена фильмов не совпадают'
        assert response_data['price'] == existed_movie['price'], 'стоимость фильмов не совпадают'

    def test_get_negative_id(self, api_manager):
        api_manager.movie_api.get_movie_info(movie_id = -5, expected_status = 404)

    def test_get_string_id(self, api_manager):
        api_manager.movie_api.get_movie_info(movie_id = 'abc', expected_status = 404)

    def test_get_underline_id(self, api_manager):
        api_manager.movie_api.get_movie_info(movie_id = '_', expected_status = 404)

