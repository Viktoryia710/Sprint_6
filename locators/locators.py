from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header') or contains(@class, 'Button')]/button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION_FIRST = (By.XPATH, "//li[@class='select-search__row' or contains(@class, 'select-search__item')][1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    
    @staticmethod
    def rent_time_option(days_text):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{days_text}']")

    @staticmethod
    def color_checkbox(color_id):
        return (By.ID, color_id)

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_FINAL_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    SUCCESS_MODAL_HEADER = (By.XPATH, "//*[contains(text(), 'Заказ оформлен') or contains(@class, 'Order_ModalHeader')]")