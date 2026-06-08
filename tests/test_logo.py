import pytest
import allure
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
            assert main_page.get_current_url() == Config.BASE_URL

    @allure.title("Клик на логотип 'Яндекс' перенаправляет на внешнюю платформу")
    @allure.description("Тест кликает по логотипу 'Яндекс', переключается на открывшуюся вкладку и проверяет редирект.")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("Принимаем куки"):
            main_page.accept_cookies()
        
        with allure.step("Кликаем по логотипу 'Яндекс'"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключаемся на новую вкладку"):
            main_page.switch_to_new_tab()
        
        with allure.step("Ожидаем редирект (уход с базового домена)"):
            main_page.wait_for_redirect_from_base_url()
        
        with allure.step("Проверяем, что мы покинули домен 'Самоката'"):
            assert Config.BASE_URL not in main_page.get_current_url()