from .base_page import BasePage
from locators import LoginLocators
import allure


class LoginPage(BasePage):
    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.driver.get(f"{self.base_url}login")
    
    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        # вводим email в поле ввода
        element = self.find_element(LoginLocators.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        # вводим пароль в поле ввода
        element = self.find_element(LoginLocators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
    
    @allure.step("Нажать кнопку входа")
    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)
    
    @allure.step("Нажать 'Забыли пароль?'")
    def click_forgot_password_link(self):
        self.click_element(LoginLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Выполнить вход")
    def login(self, email, password):
        # полный процесс входа в систему
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()