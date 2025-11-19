import pytest
import allure
from helpers import TEST_EMAIL, TEST_PASSWORD
from locators import *

class TestOrders:
    @allure.title('Открытие модального окна с деталями заказа')
    def test_open_order_details_modal(self, main_page, orders_page):
        main_page.go_to_orders_feed()
        orders_page.click_first_order()
        assert orders_page.is_composition_text_visible()

    @allure.title('Отображение заказов пользователя в ленте заказов')
    def test_user_orders_in_feed(self, logged_in_user, main_page, orders_page, created_order):
        main_page.go_to_orders_feed()
        assert orders_page.find_order_in_feed_by_number(created_order)

    @allure.title('Увеличение счетчиков выполненных заказов')
    def test_total_orders_counter_increase(self, constructor_page, orders_page, main_page, logged_in_user):
        # тест не использует created_order, тк ему нужно создать заказ внутри теста
        constructor_page.wait_for_constructor_page_loaded()
        main_page.go_to_orders_feed()
        orders_page.wait_for_feed_page_loaded()
        initial_total = orders_page.get_total_orders_count()
        initial_today = orders_page.get_today_orders_count()
        main_page.click_constructor_button()
        constructor_page.wait_for_constructor_page_loaded()
        constructor_page.create_basic_order()
        constructor_page.click_order_button()
        constructor_page.wait_for_order_modal_loaded()
        constructor_page.close_modal()
        constructor_page.wait_for_modal_closed()
        main_page.go_to_orders_feed()
        orders_page.wait_for_feed_page_loaded()
        orders_page.wait_for_total_orders_increase(initial_total)
        orders_page.wait_for_today_orders_increase(initial_today)
        new_total = orders_page.get_total_orders_count()
        new_today = orders_page.get_today_orders_count()
        assert new_total > initial_total
        assert new_today > initial_today

    @allure.title('Отображение номера заказа в разделе В работе')
    def test_order_number_in_progress(self, main_page, orders_page, logged_in_user, created_order):
        main_page.go_to_orders_feed()
        orders_page.wait_for_feed_page_loaded()
        assert orders_page.find_order_in_progress_by_number(created_order)