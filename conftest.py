import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.constructor_page import ConstructorPage
from pages.orders_page import OrdersPage

BASE_URL = "https://stellarburgers.education-services.ru/"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # фикстура драйвера с параметризацией для кроссбраузерного тестирования
    # запускает каждый тест в chrome и firefox
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    # фикстура главной страницы - автоматически открывает сайт
    page = MainPage(driver, BASE_URL)
    page.go_to_site() 
    return page

@pytest.fixture
def login_page(driver):
    # фикстура страницы логина
    return LoginPage(driver, BASE_URL)

@pytest.fixture
def forgot_password_page(driver):
    # фикстура страницы восстановления пароля
    return ForgotPasswordPage(driver, BASE_URL)

@pytest.fixture
def constructor_page(driver):
    # фикстура страницы конструктора бургеров
    return ConstructorPage(driver, BASE_URL)

@pytest.fixture
def orders_page(driver):
    # фикстура страницы ленты заказов
    return OrdersPage(driver, BASE_URL)

@pytest.fixture
def registered_user(login_page, main_page):  
    # фикстура создает пользователя через api и выполняет логин
    # автоматически удаляет пользователя после теста
    user_data = create_user_via_api()
    
    main_page.click_personal_account_button()
    login_page.wait_for_url_contains("/login")
    login_page.login(user_data["email"], user_data["password"])
    main_page.wait_for_main_page_load()
    
    yield user_data
    
    # очистка после теста
    if user_data.get('accessToken'):
        delete_user_via_api(user_data['accessToken'])

@pytest.fixture
def logged_in_user(main_page, login_page):
    # фикстура для логина стандартного тестового пользователя
    from helpers import TEST_EMAIL, TEST_PASSWORD
    from selenium.webdriver.support.ui import WebDriverWait
    
    # переходим на страницу логина и вводим данные
    main_page.click_personal_account_button()
    login_page.wait_for_url_contains("/login")
    login_page.enter_email(TEST_EMAIL)
    login_page.enter_password(TEST_PASSWORD)
    login_page.click_login_button()
    
    # ждем завершения логина (редирект с /login)
    WebDriverWait(login_page.driver, 15).until(
        lambda driver: "/login" not in driver.current_url
    )
    
    # ждем загрузки главной страницы после логина
    main_page.wait_for_main_page_load()
    yield

@pytest.fixture
def created_order(constructor_page):
    # фикстура создает тестовый заказ и возвращает его номер
    # используется в тестах где нужно проверить отображение заказа
    constructor_page.create_basic_order()
    constructor_page.click_order_button()
    constructor_page.wait_for_order_modal_loaded()
    order_number = constructor_page.get_order_number()
    constructor_page.close_modal()
    constructor_page.wait_for_modal_closed()
    return order_number