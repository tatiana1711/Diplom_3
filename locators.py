from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDERS_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__')]")


class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")

class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class ConstructorLocators:
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[6]")
    FILLING_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[11]")
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__')]")
    INGREDIENT_TO_DRAG = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")

class ModalLocators:
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")  # Упрощаем
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text text_type_main-medium')]")
    MODAL_INGREDIENT_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_ID_TEXT = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    COMPOSITION_TEXT = (By.XPATH, "//*[contains(text(), 'Cостав')]")

class OrderFeedLocators:
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")
    FIRST_ORDER = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__')])[1]")
    ORDER_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//div[contains(text(), 'В работе')]//following-sibling::ul//li")
    ORDER_FEED_SECTION = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    ORDERS_IN_FEED = (By.XPATH, "//*[contains(@class, 'OrderHistory_link__')]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, '//p[normalize-space(.)="Выполнено за сегодня:"]/following-sibling::p')
