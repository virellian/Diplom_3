import requests
from curl import Url
from data import RequestAndResponseKeys as Key

class HelperMethods:

    # Отправка запроса на создание пользователя через API
    @staticmethod
    def register_new_user(user_data):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_FEED_PAGE}', data=user_data)

    # Отправка запроса на удаление существующего пользователя
    @staticmethod
    def delete_user(access_token):
        return requests.delete(f'{Url.BASE_URL}{Url.ORDER_FEED_PAGE}', headers={Key.AUTH_FIELD_NAME: access_token})