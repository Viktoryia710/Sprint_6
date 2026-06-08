import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from config import Config

@allure.feature("Навигация по сайту")
@allure.story("Переходы по клику на логотипы в хедере")
class TestLogos:

    @allure.title("Клик на логотип 'Самокат' возвращает на главную страницу")
    @allure.description("Тест уходит со страницы на форму заказа, кликает на логотип 'Самокат' и проверяет возвращение на базовый URL.")
    def test_click_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Принимаем куки"):
            main_page.accept_cookies()
        
        with allure.step("Имитируем уход со страницы через переход к заказу"):
            main_page.click_top_order_button()
        
        with allure.step("Кликаем на логотип 'Самокат'"):
            main_page.click_scooter_logo()
            
        with allure.step("Проверяем, что текущий URL соответствует главной странице"):
            assert driver.current_url == Config.BASE_URL

    @allure.title("Клик на логотип 'Яндекс' перенаправляет на внешнюю платформу")
    @allure.description("Тест кликает по логотипу 'Яндекс', переключается на открывшуюся вкладку и проверяет редирект.")
    def test_click_yandex_logo_redirects_to_dzen(self, driver, wait):
        main_page = MainPage(driver)
        
        with allure.step("Принимаем куки"):
            main_page.accept_cookies()
        
        with allure.step("Кликаем по логотипу 'Яндекс'"):
            main_page.click_yandex_logo()
        
        with allure.step("Ожидаем появление второй вкладки браузера"):
            wait.until(EC.number_of_windows_to_be(2))
        
        with allure.step("Переключаемся на новую вкладку"):
            new_window = driver.window_handles[1]
            driver.switch_to.window(new_window)
        
        with allure.step("Ожидаем старт редиректа"):
            import time
            time.sleep(3)
        
        with allure.step("Проверяем, что мы покинули домен 'Самоката'"):
            assert Config.BASE_URL not in driver.current_url