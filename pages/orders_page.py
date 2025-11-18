from .base_page import BasePage
from locators import OrderFeedLocators, ModalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrdersPage(BasePage):
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER)
    
    @allure.step("Получить счетчик всех заказов")
    def get_total_orders_count(self):
        # получаем число из счетчика "выполнено за все время"
        element = self.wait_for_element_visible(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(element.text)

    @allure.step("Получить счетчик заказов за сегодня")
    def get_today_orders_count(self):
        # получаем число из счетчика "выполнено за сегодня"
        element = self.wait_for_element_visible(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text)
        
    @allure.step("Проверить видимость текста 'состав' в модальном окне")
    def is_composition_text_visible(self):
        # проверяем что в модальном окне отображается текст 'состав'
        return self.is_element_visible(ModalLocators.COMPOSITION_TEXT)
    
    def _find_order_by_number(self, order_number, timeout=15):
        # общий метод для поиска заказа по номеру
        try:
            # ждем загрузки ленты заказов
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(OrderFeedLocators.ORDERS_IN_FEED)
            )
            
            # ищем заказ по номеру
            order_locator = self.get_order_locator_by_number(order_number)
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(order_locator)
            )
            
            return element.is_displayed()
            
        except Exception as e:
            # логируем ошибку но возвращаем false для assert
            print(f"заказ {order_number} не найден: {e}")
            return False

    @allure.step("Найти заказ по номеру в ленте заказов")
    def find_order_in_feed_by_number(self, order_number, timeout=15):
        # ищем заказ по номеру в основной ленте заказов
        return self._find_order_by_number(order_number, timeout)

    @allure.step("Найти заказ по номеру в разделе 'В работе'")
    def find_order_in_progress_by_number(self, order_number, timeout=15):
        # ищем заказ по номеру в разделе "в работе"
        return self._find_order_by_number(order_number, timeout)

    @allure.step("Дождаться увеличения счетчика всех заказов")
    def wait_for_total_orders_increase(self, initial_count, timeout=15):
        # ждем пока счетчик всех заказов станет больше начального значения
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_total_orders_count() > initial_count
        )

    @allure.step("Дождаться увеличения счетчика заказов за сегодня")
    def wait_for_today_orders_increase(self, initial_count, timeout=15):
        # ждем пока счетчик заказов за сегодня станет больше начального значения
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_today_orders_count() > initial_count
        )

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_feed_page_loaded(self):
        # ждем когда загрузится страница ленты заказов
        self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_SECTION)