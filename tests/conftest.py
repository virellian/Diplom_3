import pytest
from selenium import webdriver
from helper_methods import HelperMethods as Help
from curl import Url
from generators import UserData as UD
from data import RequestAndResponseKeys as Key
from pages.login_page import LoginPage
from pages.main_page import MainPage


# Открытие окна веб-браузера
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_URL)
    yield driver
    driver.quit()

#Создание пользователя и сохранение его данных для удаления после завершения тестов
@pytest.fixture
def generate_user():
    # Генер email, пароля и имя нового пользователя
    user_data = UD.generate_new_user_data()
    # Отправление запроса на создание уникального пользователя
    response = Help.register_new_user(user_data)
    # Получение тела ответа в формате словаря
    response_dict = response.json()
    # Получение авторизационного токена
    access_token = response_dict[Key.ACCESS_TOKEN]
    # Возвращение данных пользователя
    yield user_data
    # Удаление созданного пользователя после завершения теста
    Help.delete_user(access_token)

# Авторизование под созданным новым пользователем на сайте
@pytest.fixture
def login_user(driver, generate_user):
    # Получение данных зарегестрированного пользователя
    email = generate_user[Key.EMAIL]
    password = generate_user[Key.PASSWORD]
    # Открытие главной страницы веб-приложения
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    # Переход на страницу авторизации пользователя
    main_page.go_to_login_page()
    # Ввод email и пароля созданного пользователя
    login_page = LoginPage(driver)
    login_page.enter_user_data(email, password)
    # Клик на кнопку войти
    login_page.click_enter_button()
    # Ожидание отображения кнопки "Оформить заказ" на главной странице
    main_page.wait_for_order_button_visibility()
    return driver