from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    INGREDIENT_WINDOW_TITLE = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]') # Заголовок модального окна "Детали ингредиента"
    CLOSE_CROSS_LINK = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//button') # Крестик для закрытия модального окна "Детали ингредиента" и "Детали заказа"
    BUN_FLUO = (By.XPATH, '(//a[contains(@href,"/ingredient/")])') # Локатор флюоресцентной булки
    INGREDIENT_COUNTER = (By.XPATH, '(//a[contains(@href,"/ingredient/")])//p[contains(@class,"counter_counter__num")]') # Счётчик выбранного количества флюоресцентной булки
    BUN_TARGET = (By.XPATH, '//span[text()="Перетяните булочку сюда (верх)"]') # Макет булки для сборки бургера
    ORDER_DETAILS_WINDOW = (By.XPATH, '//section[contains(@class,"Modal_modal_opened__3ISw4")]') # Окно с деталями оформленного заказа
    ANIMATION = (By.XPATH, '//img[@src="./static/media/loading.89540200.svg"]') # Анимация в окне с деталями оформленного заказа
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class,"Modal_modal__title_shadow")]') # Номер оформленного заказа в окне с деталями заказа