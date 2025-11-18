import pytest
import allure
from helpers import TEST_EMAIL

class TestForgotPassword:
    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_forgot_password_page(self, login_page, main_page):
        # переходим на страницу логина через главную
        main_page.click_personal_account_button()
        login_page.wait_for_url_contains("/login")
        
        # кликаем на восстановление пароля
        login_page.click_forgot_password_link()
        login_page.wait_for_url_contains("/forgot-password")
        assert "/forgot-password" in login_page.driver.current_url

    @allure.title('Восстановление пароля с вводом email')
    def test_password_recovery_with_email(self, login_page, main_page, forgot_password_page):
        # переходим на страницу восстановления пароля через UI
        main_page.click_personal_account_button()
        login_page.wait_for_url_contains("/login")
        login_page.click_forgot_password_link()
        login_page.wait_for_url_contains("/forgot-password")
        
        # вводим email и кликаем восстановить
        forgot_password_page.enter_email(TEST_EMAIL)
        forgot_password_page.click_restore_button()
        
        # проверяем переход на страницу сброса пароля
        forgot_password_page.wait_for_url_contains("/reset-password")
        assert "/reset-password" in forgot_password_page.driver.current_url

    @allure.title('Активация поля пароля при клике на иконку')
    def test_password_field_activation(self, login_page, main_page, forgot_password_page):
        # переходим на страницу восстановления пароля через UI
        main_page.click_personal_account_button()
        login_page.wait_for_url_contains("/login")
        login_page.click_forgot_password_link()
        login_page.wait_for_url_contains("/forgot-password")
        
        # вводим email и переходим на страницу сброса
        forgot_password_page.enter_email(TEST_EMAIL)
        forgot_password_page.click_restore_button()
        forgot_password_page.wait_for_url_contains("/reset-password")
        
        # кликаем на иконку показа пароля
        forgot_password_page.click_show_password_button()
        
        # проверяем активацию поля через метод класса
        assert forgot_password_page.is_password_field_active(), "Поле пароля не активировалось"