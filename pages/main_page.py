import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):

    @allure.step('Дождаться загрузки главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_invisibility(MPL.OVERLAY)

    @allure.step('Кликаем надпись "Конструктор" на главной странице')
    def click_constructor_title(self):
        self.click_on_element(MPL.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем надпись "Лента заказов"')
    def click_order_feed_title(self):
        self.click_on_element(MPL.ORDER_FEED_TITLE)

    @allure.step('Дожидаемся отображения кнопки "Войти в аккаунт"')
    def wait_for_login_button(self):
        return self.wait_for_element_visibility(MPL.LOG_IN_BUTTON)

    @allure.step('Переходим на страницу авторизации пользователя')
    def go_to_login_page(self):
        self.click_on_element(MPL.LOG_IN_BUTTON)

    @allure.step('Дождатьcя появления кнопки "Оформить заказ"')
    def wait_for_order_button_visibility(self):
        self.wait_for_element_visibility(MPL.ORDER_BUTTON)