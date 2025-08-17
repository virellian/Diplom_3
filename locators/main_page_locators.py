from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div" # Локатор оверлэя при загрузке главной страницы
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт" на главной странице
    CONSTRUCTOR_TITLE = (By.LINK_TEXT, "Конструктор")  # Надпись "Конструктор" в хедере главной страницы
    ORDER_FEED_TITLE = (By.LINK_TEXT, "Лента Заказов")  # Надпись "Лента заказов" в хедере главной страницы
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ" на главной странице