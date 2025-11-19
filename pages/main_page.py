from .base_page import BasePage
from locators import MainLocators
import allure


class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.click_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Перейти в ленту заказов")
    def go_to_orders_feed(self):
        # переходим в ленту заказов и ждем загрузки
        self.click_element(MainLocators.ORDERS_BUTTON)
        self.wait_for_url_contains("/feed")
    
    @allure.step("Кликнуть на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_element(MainLocators.LOGIN_BUTTON)
    
    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_main_page_load(self):
        # ждем когда загрузится главная страница
        self.wait_for_element_visible(MainLocators.CONSTRUCTOR_BUTTON)