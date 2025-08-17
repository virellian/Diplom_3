import random
import string
from data import RequestAndResponseKeys as Key

class UserData:

# Метод генерации данных для создания нового пользователя
    @staticmethod
    def generate_new_user_data():
        # Метод генерирует строку, состоящую только из букв нижнего регистра,в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # Генер email, пароль и имя пользователя
        email = generate_random_string(10) + "@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)

        # Сборка тела запроса
        user_data = {
        Key.EMAIL: email,
        Key.PASSWORD: password,
        Key.NAME: name
        }
        # Возврат словаря с электронной почтой, паролем и именем пользователя
        return user_data