import pytest
import allure
from locators import PersonalAccountLocators

class TestPersonalAccountOptimized:
    @allure.title("Переход в личный кабинет неавторизованным пользователем")
    def test_open_personal_account_unauthorized(self, main_page):
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/login")
        assert "/login" in main_page.driver.current_url

    @allure.title("Переход в личный кабинет авторизованным пользователем")
    def test_open_personal_account_authorized(self, logged_in_user, main_page):
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/account/profile")
        assert "/account/profile" in main_page.driver.current_url

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, logged_in_user, main_page):
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/account/profile")
        main_page.click_element(PersonalAccountLocators.ORDER_HISTORY_LINK)
        main_page.wait_for_url_contains("/account/order-history")
        assert "/account/order-history" in main_page.driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, logged_in_user, main_page):
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/account/profile")
        main_page.click_element(PersonalAccountLocators.LOGOUT_BUTTON)
        main_page.wait_for_url_contains("/login")
        assert "/login" in main_page.driver.current_url