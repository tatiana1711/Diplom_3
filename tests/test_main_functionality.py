import pytest
import allure
from locators import *
from urls import *

class TestMainFunctionality:
    @allure.title('Переход в конструктор из личного кабинета')
    def test_go_to_constructor_from_account(self, registered_user, main_page):
        main_page.click_personal_account_button()
        main_page.click_constructor_button()
        current_url = main_page.get_current_url()
        assert current_url == BASE_URL

    @allure.title('Переход в ленту заказов')
    def test_go_to_order_feed(self, main_page):
        main_page.go_to_orders_feed()
        current_url = main_page.get_current_url()
        assert "/feed" in current_url

    @allure.title('Открытие модального окна с деталями ингредиента')
    def test_open_ingredient_modal(self, main_page, constructor_page):
        main_page.wait_for_main_page_load()
        constructor_page.click_bun_ingredient()
        assert constructor_page.is_modal_visible()

    @allure.title('Закрытие модального окна с деталями ингредиента')  
    def test_close_ingredient_modal(self, main_page, constructor_page):
        main_page.wait_for_main_page_load()
        constructor_page.click_bun_ingredient()
        constructor_page.close_modal()
        assert constructor_page.is_ingredient_details_not_visible()

    @allure.title('Увеличение счетчика ингредиента при добавлении')
    def test_ingredient_counter_increase(self, main_page, constructor_page):
        main_page.wait_for_main_page_load()
        counter_before, counter_after = constructor_page.add_ingredient_and_get_counters()
        assert counter_after > counter_before

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_create_order_authorized_user(self, logged_in_user, main_page, constructor_page):
        main_page.wait_for_main_page_load()
        constructor_page.create_basic_order()
        constructor_page.click_order_button()
        constructor_page.wait_for_order_modal_loaded()
        assert constructor_page.is_modal_visible(), "Модальное окно заказа не появилось"
        assert constructor_page.is_order_id_visible(), "Текст 'идентификатор заказа' не отображается"
