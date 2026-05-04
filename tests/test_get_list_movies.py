class TestGetPoster():
    def test_get_list_movie(self, api_manager, test_list_movies):
        response = api_manager.movie_api.get_movie_poster(test_list_movies)
        response_data = response.json()
        assert test_list_movies['pageSize'] == response_data['pageSize'], 'Размер страницы не совпадает'
        assert test_list_movies['page'] == response_data['page'], 'Номер страницы не совпадает'
        assert 'movies' in response_data, 'в ответе отсутствует ключ movies'
        assert response_data['count'] >= 0, 'некорректное число фильмов'

    def test_zero_genreId(self, api_manager, test_list_movies):
        test_list_movies["genreId"] = 0
        api_manager.movie_api.get_movie_poster(test_list_movies, expected_status = 400)

    def test_wrong_location(self, api_manager):
        data = {"locations": "wrong_location"}
        api_manager.movie_api.get_movie_poster(data, expected_status = 400)

    def test_maxprice_less_minprice(self, api_manager, test_list_movies):
        test_list_movies["maxPrice"] = 1
        test_list_movies["minPrice"] = 1000
        api_manager.movie_api.get_movie_poster(test_list_movies, expected_status = 400)

    def test_wrong_param(self, api_manager):
        data = {"wrong": "wrong"}
        api_manager.movie_api.get_movie_poster(data, expected_status = 404)