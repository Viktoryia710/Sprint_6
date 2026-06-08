import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Оформление заказа")
@pytest.mark.parametrize(
    "entry_point, name, surname, address, phone, date, rent_days, color, comment",
    [
        ("top", "Иван", "Петров", "ул. Ленина, д. 10, кв. 5", "79991112233", "15.06.2026", "сутки", "black", "Позвонить за час"),
        ("bottom", "Светлана", "Иванова", "Проспект Мира, д. 45", "79110005566", "20.06.2026", "двое суток", "grey", "Оставить у консьержа")
    ]
)
def test_successful_scooter_ordering(driver, entry_point, name, surname, address, phone, date, rent_days, color, comment):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    
    main_page.accept_cookies()
    
    if entry_point == "top":
        main_page.click_top_order_button()
    else:
        main_page.click_bottom_order_button()
        
    order_page.fill_first_form(name, surname, address, phone)
    order_page.fill_second_form(date, rent_days, color, comment)
    
    assert order_page.is_success_modal_displayed()