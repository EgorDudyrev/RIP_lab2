from base_client import *
import requests
import vk_api

class VK_User(BaseClient):
    def __init__(self, username):
        pass

    BASE_URL = 'https://vk.com/dev/'
    method = 'users.get'
    http_method = 'GET'

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):
        response = None

        # todo выполнить запрос
        response = vk_api.VkApi.method(method='users.get',values={'user_ids': 'egordudyrev'})

        return self.response_handler(response)


