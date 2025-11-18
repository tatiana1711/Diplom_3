from .base_page import BasePage
from locators import ConstructorLocators, ModalLocators, MainLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ConstructorPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
    
    @allure.step("Кликнуть на ингредиент булки")
    def click_bun_ingredient(self):
        # кликаем на первый ингредиент булки в списке
        self.click_element(ConstructorLocators.BUN_INGREDIENT)
    
    @allure.step("Кликнуть на ингредиент соуса")
    def click_sauce_ingredient(self):
        # кликаем на ингредиент соуса в списке
        self.click_element(ConstructorLocators.SAUCE_INGREDIENT)
    
    @allure.step("Кликнуть на ингредиент начинки")
    def click_filling_ingredient(self):
        # кликаем на ингредиент начинки в списке
        self.click_element(ConstructorLocators.FILLING_INGREDIENT)
    
    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_order_button(self):
        # кликаем на кнопку оформления заказа
        self.click_element(ConstructorLocators.ORDER_BUTTON)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        # закрываем модальное окно кликом на крестик
        self.click_element(ModalLocators.MODAL_CLOSE)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        # проверяем отображается ли модальное окно
        return self.is_element_visible(ModalLocators.MODAL)
    
    
    @allure.step("Проверить видимость деталей ингредиента")
    def is_ingredient_details_visible(self):
        # проверяем отображается ли модальное окно с деталями ингредиента
        return self.is_element_visible(ModalLocators.MODAL_INGREDIENT_TITLE)
    
    @allure.step("Проверить что детали ингредиента скрыты")
    def is_ingredient_details_not_visible(self, timeout=3):
        # проверяем что модальное окно с деталями ингредиента закрыто
        return self.is_element_not_visible(ModalLocators.MODAL_INGREDIENT_TITLE, timeout)
    
    @allure.step("Проверить что отображается идентификатор заказа")
    def is_order_id_visible(self):
        # проверяем что в модальном окне заказа отображается идентификатор
        return self.is_element_visible(ModalLocators.ORDER_ID_TEXT)


    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_locator):
        # добавляем ингредиент в конструктор через drag and drop
        # для разных браузеров используем разные методы перетаскивания
        if self.browser_name == 'chrome':
            self.drag_and_drop_chrome(ingredient_locator, ConstructorLocators.CONSTRUCTOR_DROP_ZONE)
        else:
            self.switch_to_window()
            self.drag_and_drop_firefox(ingredient_locator, ConstructorLocators.CONSTRUCTOR_DROP_ZONE)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        # получаем числовое значение счетчика у ингредиента
        # если счетчик не найден или не число, возвращаем 0
        elements = self.driver.find_elements(*ConstructorLocators.INGREDIENT_COUNTER)
        if elements and elements[0].text.isdigit():
            return int(elements[0].text)
        return 0
    
    @allure.step("Добавить ингредиент и получить значения счетчика")
    def add_ingredient_and_get_counters(self):
        # добавляем ингредиент и возвращаем значения счетчика до и после
        counter_before = self.get_ingredient_counter()
        self.add_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT)
        counter_after = self.get_ingredient_counter()
        return counter_before, counter_after
    
    @allure.step("Собрать базовый заказ")
    def create_basic_order(self):
        # создаем базовый заказ из булки, соуса и начинки
        # это минимальный набор для тестирования оформления заказа
        self.add_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT)
        self.add_ingredient_to_constructor(ConstructorLocators.SAUCE_INGREDIENT)
        self.add_ingredient_to_constructor(ConstructorLocators.FILLING_INGREDIENT)
    
    @allure.step("Дождаться видимости модального окна заказа")
    def wait_for_order_modal_visible(self, timeout=15):
        # ждем когда модальное окно заказа станет видимым
        self.wait_for_element_visible(ModalLocators.MODAL, timeout)
    
    @allure.step("Дождаться загрузки модального окна заказа")
    def wait_for_order_modal_loaded(self, timeout=20):
        # ждем полной загрузки модального окна заказа
        # проверяем что номер заказа загрузился (не равен заглушке 9999)
        self.wait_for_element_visible(ModalLocators.MODAL, timeout)
        
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_order_number() != "9999"
        )
    
    @allure.step("Дождаться закрытия модального окна заказа")
    def wait_for_modal_closed(self, timeout=10):
        # ждем когда модальное окно полностью закроется
        WebDriverWait(self.driver, timeout).until(
            lambda driver: not self.is_modal_visible()
        )
    
    @allure.step("Дождаться загрузки страницы конструктора")
    def wait_for_constructor_page_loaded(self):
        # ждем когда страница конструктора полностью загрузится
        self.wait_for_element_visible(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        # получаем номер заказа из модального окна оформления
        element = self.find_element(ModalLocators.ORDER_NUMBER)
        return element.text