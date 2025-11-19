from .base_page import BasePage
from locators import ForgotPasswordLocators
import allure


class ForgotPasswordPage(BasePage):
    @allure.step("Ввести email: {email}")
    def enter_email(self, email):
        # вводим email в поле восстановления пароля
        element = self.find_element(ForgotPasswordLocators.EMAIL_INPUT)
        element.clear()
        element.send_keys(email)
    
    @allure.step("Кликнуть на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click_element(ForgotPasswordLocators.RESTORE_BUTTON)
    
    @allure.step("Кликнуть на иконку показа пароля")
    def click_show_password_button(self):
        # кликаем на глазок чтобы показать/скрыть пароль
        self.click_element(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)
    
    @allure.step("Проверить активацию поля пароля")
    def is_password_field_active(self):
        # проверяем что поле пароля стало активным после клика на глазок
        return self.is_element_visible(ForgotPasswordLocators.PASSWORD_INPUT_ACTIVE)