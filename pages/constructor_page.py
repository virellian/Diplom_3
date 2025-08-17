import allure
from locators.constructor_page_locators import  ConstructorPageLocators as CPL
from locators.main_page_locators import MainPageLocators as MPL
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Кликаем на ингредиент "Флюоресцентная булка"')
    def click_bun_fluo(self):
        self.click_on_element(CPL.BUN_FLUO)

    @allure.step('Дожидаемся отображения модального окна с деталями ингредиента')
    def wait_for_ingredient_window(self):
        return self.wait_for_element_visibility(CPL.INGREDIENT_WINDOW_TITLE)

    @allure.step('Кликаем на крестик закрытия окна с деталями ингредиента')
    def click_ingredient_window_cross(self):
        self.click_on_element(CPL.CLOSE_CROSS_LINK)

    @allure.step('Дожидаемся скрытия надписи "Детали ингредиента"')
    def ingredient_window_is_closed(self):
        return self.wait_for_element_invisibility(CPL.INGREDIENT_WINDOW_TITLE)

    @allure.step('Получаем счетчик булок')
    def get_counter(self):
        counter = self.get_text(CPL.INGREDIENT_COUNTER)
        counter = int(counter)
        return counter

    @allure.step('Перетаскиваем флюоресцентную булочку в бургер')
    def drag_and_drop_bun(self):
        source = self.wait_for_element_visibility(CPL.BUN_FLUO)
        target = self.wait_for_element_visibility(CPL.BUN_TARGET)
        self.drag_and_drop_element(source, target)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element(MPL.ORDER_BUTTON)

    @allure.step('Дожидаемся появления модального окна с деталями заказа')
    def wait_for_order_details_window(self):
        return self.wait_for_element_visibility(CPL.ORDER_DETAILS_WINDOW)

    @allure.step('Дожидаемся исчезновения анимации в модальном окне с деталями заказа')
    def wait_till_loading_animation_ends(self):
        self.wait_for_element_invisibility(CPL.ANIMATION)

    @allure.step('Кликаем на крестик для закрытия модального окна с деталями заказа')
    def click_order_details_cross(self):
        self.click_on_element(CPL.CLOSE_CROSS_LINK)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        return self.wait_for_element_visibility(CPL.ORDER_NUMBER).text