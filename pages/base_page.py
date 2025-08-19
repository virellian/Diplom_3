import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_visibility(locator, timeout)
        element.click()

    @allure.step("Получаем текущий Url")
    def get_current_url(self):
       return self.driver.current_url

    @allure.step("Дождаться скрытия элемента")
    def wait_for_element_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
       return self.wait_for_element_visibility(locator).text

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Ввести данные в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element_visibility(locator, timeout)
        element.send_keys(keys)

    @allure.step("Подождать видимости всех элементов")
    def wait_for_all_elements_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))