from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import MainPageLocators  # Добавили импорт локаторов!
from config import Config

class MainPage(BasePage):  # Объявляем класс

    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON))
            cookie_btn.click()
        except Exception:
            pass

    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        button = self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def wait_for_redirect_from_base_url(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: Config.BASE_URL not in driver.current_url
        )
    
    def get_faq_answer_text(self, index):
        question_locator = MainPageLocators.faq_question(index)
        question_element = self.wait.until(EC.element_to_be_clickable(question_locator))
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)
        self.driver.execute_script("arguments[0].click();", question_element)
        
        answer_locator = MainPageLocators.faq_answer(index)
        answer_element = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer_element.text