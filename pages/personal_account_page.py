import pytest
import allure
from helpers import create_user_via_api, delete_user_via_api
from locators import PersonalAccountLocators

class TestPersonalAccount:
    @allure.title("Переход в личный кабинет авторизованного пользователя")
    def test_open_personal_account_success(self, main_page, login_page):
        user_data = create_user_via_api()
        main_page.click_personal_account_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.wait_for_main_page_load()
        main_page.click_personal_account_button()
        current_url = main_page.get_current_url()
        assert "/account/profile" in current_url
        if user_data.get('accessToken'):
            delete_user_via_api(user_data['accessToken'])

    @allure.title("Переход в раздел 'История заказов'")
    def test_redirect_to_order_history_page_success(self, main_page, login_page):
        user_data = create_user_via_api()
        main_page.click_personal_account_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.wait_for_main_page_load()
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/account/profile")
        main_page.click_element(PersonalAccountLocators.ORDER_HISTORY_LINK)
        current_url = main_page.get_current_url()
        assert "/account/order-history" in current_url
        if user_data.get('accessToken'):
            delete_user_via_api(user_data['accessToken'])

    @allure.title("Выход из аккаунта")
    def test_exit_account_success(self, main_page, login_page):
        user_data = create_user_via_api()
        main_page.click_personal_account_button()
        login_page.login(user_data["email"], user_data["password"])
        main_page.wait_for_main_page_load()
        main_page.click_personal_account_button()
        main_page.wait_for_url_contains("/account/profile")
        main_page.click_element(PersonalAccountLocators.LOGOUT_BUTTON)
        current_url = main_page.get_current_url()
        assert "/login" in current_url
        if user_data.get('accessToken'):
            delete_user_via_api(user_data['accessToken'])