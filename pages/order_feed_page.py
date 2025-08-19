import allure
from locators.order_feed_page_locators import OrderFeedPageLocators as OPL
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Ждем отображения надписи "Выполнено за все время"')
    def wait_for_total_all_time_title(self):
        return self.wait_for_element_visibility(OPL.TOTAL_ALL_TIME_TITLE)

    @allure.step('Получаем список элементов страницы с данными со счетчиков "Выполнено за всё время" и "Выполнено за сегодня"')
    def get_counters_data(self):
        elements = self.wait_for_all_elements_visibility(OPL.ORDER_FEED_COUNTERS)
        return elements

    @allure.step('Получаем данные со счетчиков "Выполнено за всё время" и "Выполнено за сегодня"')
    def get_counter_value(self, d):
        elements = self.get_counters_data()
        return int(str(elements[d].text))

    @allure.step('Получаем номер заказа из раздела "В работе"')
    def get_order_number_in_work(self):
        return self.get_text(OPL.ORDER_NUMBER_IN_WORK)