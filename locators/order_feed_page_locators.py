from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    TOTAL_ALL_TIME_TITLE = (By.XPATH, "//p[text()='Выполнено за все время:']") # Заголовок счётчика подсчёта количества выполненных заказов за всё время
    ORDER_FEED_COUNTERS = (By.XPATH, '//p[contains(@class,"OrderFeed_number")]') # Счётчики "Выполнено за все время" и "Выполнено за сегодня"
    ORDER_NUMBER_IN_WORK = (By.XPATH, '(//ul[contains(@class,"OrderFeed_orderList")])[2]/li[contains(@class,"digits")]') # Номер оформленного заказа в блоке "В работе"