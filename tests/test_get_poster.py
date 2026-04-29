class TestGetPoster():
    def test_get_poster(self, api_manager, test_poster):
        response = api_manager.movie_api.get_movie_poster(test_poster)
        response_data = response.json()
        assert test_poster['pageSize'] == response_data['pageSize'], 'Размер страницы не совпадает'
        assert test_poster['page'] == response_data['page'], 'Номер страницы не совпадает'

    def test_zero_genreId(self, api_manager, test_poster):
        test_poster["genreId"] = 0
        api_manager.movie_api.get_movie_poster(test_poster, expected_status = 400)

    def test_wrong_location(self, api_manager):
        data = {"locations": "wrong_location"}
        api_manager.movie_api.get_movie_poster(data, expected_status = 400)

    def test_maxprice_less_minprice(self, api_manager, test_poster):
        test_poster["maxPrice"] = 1
        test_poster["minPrice"] = 1000
        api_manager.movie_api.get_movie_poster(test_poster, expected_status = 400)



    def test_wrong_param(self, api_manager):
        data = {"wrong": "wrong"}
        api_manager.movie_api.get_movie_poster(data, expected_status = 404)