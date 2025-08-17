import allure
import pytest
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title('Проверка, что при создании нового заказа счетчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @pytest.mark.parametrize('period', [0, 1])
    def test_total_orders_counter_increases(self, driver, login_user, period):
        with allure.step('Ожидание загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Переход в "Ленту Заказов"'):
            main_page.click_order_feed_title()
            order_feed_page = OrderFeedPage(driver)
        with allure.step('Получение данных со счетчиков: 0 - "Выполнено за всё время", 1 - "Выполнено за сегодня"'):
            order_total_before = order_feed_page.get_counter_value(period)
        with allure.step('Переход на страницу "Конструктора"'):
            main_page.click_constructor_title()
            constructor_page = ConstructorPage(driver)
        with allure.step('Собирание бургера'):
            constructor_page.drag_and_drop_bun()
        with allure.step('Клик на кнопку "Оформить заказ"'):
            constructor_page.click_order_button()
        with allure.step('Ожидание появления модального окна с деталями заказа'):
            constructor_page.wait_for_order_details_window()
        with allure.step('Ожидание прогрузки анимации модального окна с деталями заказа'):
            constructor_page.wait_till_loading_animation_ends()
        with allure.step('Клик на крестик и закрытие модального окно с деталями заказа'):
            constructor_page.click_order_details_cross()
        with allure.step('Переход в "Ленту Заказов"'):
            main_page.click_order_feed_title()
        with allure.step('Получение данных со счетчика "Выполнено за всё время"'):
            order_total_after = order_feed_page.get_counter_value(period)
            assert order_total_after > order_total_before, f'При создании заказа счетчики "Выполнено за всё время" и "Выполнено за сегодня" не увеличиваются'

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе «В работе»')
    def test_order_number_is_in_work(self, driver, login_user):
        with allure.step('Ожидание загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Переход в "Конструктор" и собираем бургер'):
            constructor_page = ConstructorPage(driver)
            constructor_page.drag_and_drop_bun()
        with allure.step('Клик на кнопку "Оформить заказ"'):
            constructor_page.click_order_button()
        with allure.step('Ожидание появления модального окна с деталями заказа'):
            constructor_page.wait_for_order_details_window()
            constructor_page.wait_till_loading_animation_ends()
        with allure.step('Получение номера заказа'):
            order_number = constructor_page.get_order_number()
        with allure.step('Клик на крестик и закрытие модального окна с деталями заказа'):
            constructor_page.click_order_details_cross()
        with allure.step('Переход в "Ленту Заказов"'):
            main_page.click_order_feed_title()
            order_feed_page = OrderFeedPage(driver)
        with allure.step('Получение номера заказа из раздела "В работе"'):
            order_number_in_work = order_feed_page.get_order_number_in_work()
            assert order_number in order_number_in_work, f'Номер оформленного заказа и номер заказа в блоке "В работе" не совпадают'