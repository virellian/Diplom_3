import requests
from curl import Url
from data import RequestAndResponseKeys as Key

class HelperMethods:

    # Отправка запроса на создание пользователя через API
    @staticmethod
    def register_new_user(user_data):
        return requests.post(f'{Url.REGISTER_USER}', data=user_data)

    # Отправка запроса на удаление существующего пользователя
    @staticmethod
    def delete_user(access_token):
        return requests.delete(f'{Url.DELETE_USER}', headers={Key.AUTH_FIELD_NAME: access_token})