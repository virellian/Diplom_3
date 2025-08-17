import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LPL


class LoginPage(BasePage):

    @allure.step('Вводим "email" и "пароль" для авторизованного входа')
    def enter_user_data(self, email, password):
        # Кликаем по полю "email"
        self.click_on_element(LPL.EMAIL)
        # Вводим email
        self.send_keys_to_input(LPL.EMAIL, email)
        # Кликаем по полю "Пароль"
        self.click_on_element(LPL.PASSWORD)
        # Вводим пароль
        self.send_keys_to_input(LPL.PASSWORD, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_enter_button(self):
        self.click_on_element(LPL.ENTER_BUTTON)