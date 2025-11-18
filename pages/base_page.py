from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url
    
    @property
    def browser_name(self):
        # получаем имя браузера для кроссбраузерных проверок
        return self.driver.name.lower()
    
    @allure.step("Открыть сайт")
    def go_to_site(self):
        # открываем базовый url сайта
        self.driver.get(self.base_url)
    
    def _wait_for_element(self, locator, timeout=15, condition=EC.presence_of_element_located):
        # универсальное ожидание элемента с разными условиями
        return WebDriverWait(self.driver, timeout).until(condition(locator))
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=15):
        return self._wait_for_element(locator, timeout)
    
    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator, timeout=15):
        # кликаем на элемент с ожиданием кликабельности
        # если обычный клик не работает, используем action chains (решение для фаерфокс)))
        element = self._wait_for_element(locator, timeout, EC.element_to_be_clickable)
        
        try:
            element.click()
        except Exception:
            # fallback для случаев когда элемент перекрыт другим элементом
            ActionChains(self.driver).move_to_element(element).pause(0.5).click().pause(0.5).perform()
    
    @allure.step("Дождаться URL содержащего {text}")
    def wait_for_url_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
    
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=15):
        return self._wait_for_element(locator, timeout, EC.visibility_of_element_located)

    
    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=5):
        # проверяем что элемент видим ый
        try:
            return bool(self.wait_for_element_visible(locator, timeout))
        except Exception:
            return False
        
    @allure.step("Проверить что элемент не видим {locator}")
    def is_element_not_visible(self, locator, timeout=5):
        # проверяем что элемент исчез или не видим
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except Exception:
            return False
    
    @allure.step("Перетаскивание элемента для Chrome")
    def drag_and_drop_chrome(self, drag_locator, drop_locator):
        #  перетаскивание для Chrome
        drag_element = self.find_element(drag_locator)
        drop_element = self.find_element(drop_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag_element, drop_element).perform()
    
    @allure.step("Перетаскивание элемента для Firefox")
    def drag_and_drop_firefox(self, drag_locator, drop_locator):
        # перетаскивание через JavaScript для Firefox
        drag_element = self.find_element(drag_locator)
        drop_element = self.find_element(drop_locator)
        
        script = """
        arguments[0].dispatchEvent(new DragEvent('dragstart', { bubbles: true }));
        arguments[1].dispatchEvent(new DragEvent('dragover', { bubbles: true }));
        arguments[1].dispatchEvent(new DragEvent('drop', { bubbles: true }));
        """
        
        self.driver.execute_script(script, drag_element, drop_element)
    
    @allure.step("Переключение на окно")
    def switch_to_window(self, window_index=0):
        # переключаемся на указанное окно браузера
        windows = self.driver.window_handles
        if windows and len(windows) > window_index:
            self.driver.switch_to.window(windows[window_index])
    
    @allure.step("Ввести текст {text} в элемент {locator}")
    def enter_text(self, locator, text):
        # вводим текст в поле с предварительной очисткой
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента {locator}")
    def get_element_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Выполнить скрипт")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    @allure.step("Получить локатор заказа по номеру {order_number}")
    def get_order_locator_by_number(self, order_number):
        # создаем локатор для поиска заказа по номеру
        return (By.XPATH, f"//*[contains(text(), '{order_number}')]")