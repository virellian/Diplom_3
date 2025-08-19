from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Поле для ввода email при авторизации
    PASSWORD = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input") # Поле для ввода пароля при авторизации
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"