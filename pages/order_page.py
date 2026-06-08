from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, phone):
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.click_element(OrderPageLocators.METRO_OPTION_FIRST)
        
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rent_days, color_id, comment):
        date_field = self.find_element(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.click_element(OrderPageLocators.RENT_TIME_DROPDOWN)
        self.click_element(OrderPageLocators.rent_time_option(rent_days))
        
        self.click_element(OrderPageLocators.color_checkbox(color_id))
        
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(OrderPageLocators.ORDER_FINAL_BUTTON)
        
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_success_modal_displayed(self):
        header = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL_HEADER))
        return header.is_displayed()