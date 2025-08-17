import allure
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from curl import Url


class TestConstructorPage:

    @allure.title('Переход по клику на раздел «Конструктор»')
    def test_open_constructor_by_click(self, driver):
        with allure.step('Ожидание загрузки сайта и клик по надписи "Лента заказов" в заголовке страницы'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_order_feed_title()
        with allure.step('Клик по надписи "Конструктор" в заголовке страницы"'):
            main_page.click_constructor_title()
        with allure.step('Ожидание перехода на вкладку "Конструктор" и отображения кнопки "Войти в аккаунт"'):
            main_page.wait_for_login_button()
        with allure.step('Проверка, что текущий Url совпадает с Url главной страницы'):
            assert main_page.get_current_url() == Url.BASE_URL+'/', f'Текущий Url не совпадает с Url главной страницы'


    @allure.title('Переход по клику на раздел «Лента заказов»')
    def test_open_order_feed_by_click(self, driver):
        with allure.step('Ожидание загрузки сайта и клик по надписи "Лента заказов" в заголовке страницы'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_order_feed_title()
        with allure.step('Ожидание перехода на вкладку "Лента заказов" и отображения надписи "Выполнено за все время"'):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.wait_for_total_all_time_title()
        with allure.step('Проверка, что текущий Url совпадает с Url главной страницы'):
            assert order_feed_page.get_current_url() == Url.ORDER_FEED_PAGE, f'Текущий Url не совпадает с Url страницы ленты заказов'


    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_open_ingredient_window(self, driver):
        with allure.step('Ожидание загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Клик на ингредиент "Флюоресцентная булка"'):
            constructor_page = ConstructorPage(driver)
            constructor_page.click_bun_fluo()
            assert constructor_page.wait_for_ingredient_window(), f'Окно с деталями ингредиента не открывается'


    @allure.title('Всплывающее окно с деталями ингредиентов закрывается кликом по крестику')
    def test_ingredient_window_close_by_cross(self, driver):
        with allure.step('Ожидание загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Клик на ингредиент "Флюоресцентная булка"'):
            constructor_page = ConstructorPage(driver)
            constructor_page.click_bun_fluo()
        with allure.step('Ожидание открытия модального окна с деталями ингредиента'):
            constructor_page.wait_for_ingredient_window()
        with allure.step('Клик на крестик'):
            constructor_page.click_ingredient_window_cross()
        with allure.step('Ожидание закрытия модального окна с деталями ингредиента'):
            constructor_page.ingredient_window_is_closed()
        with allure.step('Проверка, что модальное окно с деталями ингредиента закрылось'):
            assert main_page.wait_for_login_button, f'Модальное окно с ингредентами не закрылось'


    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_ingredient_counter_is_rising(self, driver):
        with allure.step('Ожидание загрузки сайта'):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
        with allure.step('Получение значения счётчика до добавления ингредиента'):
            constructor_page = ConstructorPage(driver)
            counter_before = constructor_page.get_counter()
        with allure.step('Перетаскивание флюоресцентной булки из меню в конструктор бургера'):
            constructor_page.drag_and_drop_bun()
        with allure.step('Получение значения счётчика после добавления ингредиента'):
            counter_after = constructor_page.get_counter()
        with allure.step('Проверка, что счетчик ингредиента увеличился'):
            assert counter_after > counter_before, f'Счетчик ингредиента после его перетаскивания в бургер не увеличился'