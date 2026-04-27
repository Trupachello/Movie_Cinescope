class TestDelete:
    def test_delete_existed_movie(self, api_manager, existed_movie):
        api_manager.movie_api.delete_movie(existed_movie['id'])
        api_manager.movie_api.get_movie_info(existed_movie['id'], expected_status = 404)

    def test_delete_without_auth(self, api_manager, existed_movie):
        existed_id = existed_movie['id']
        api_manager.auth_api.logout_user()
        api_manager.movie_api.delete_movie(existed_id, expected_status = 401)

    def test_delete_empty_movieid(self, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.delete_movie(movie_id = '', expected_status = 404)

    def test_delete_negative_movieid(self, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.delete_movie(movie_id = -5, expected_status = 404)

    def test_delete_string_movieid(self, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.delete_movie(movie_id = 'abc', expected_status = 404)

    def test_delete_extrim_big_movieid(self, api_manager):
        api_manager.auth_api.authenticate_super_admin()
        api_manager.movie_api.delete_movie(movie_id = 1e99, expected_status=404)
