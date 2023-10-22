import pytest
from locators.order_page_locators import OrderPageLocators as Order
from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import BasePage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize('button, name, surname, adress, phone', [
        [Main.ORDER_UP, 'Иван', 'Иванов', 'Ленина 1', '89991243456'],
        [Main.ORDER_DOWN, 'Анна', 'Коровкина', 'Суворова 1534', '89123456798']
    ]
                             )
    def test_order_button_up(self, driver, button, name, surname, adress, phone):
        base_page = BasePage(driver)

        order_page = OrderPage(driver)
        base_page.go_to_site()
        order_page.scroll_order(driver, button)
        order_page.click_on_button_order(button)
        order_page.filling_form_order(name, surname, adress, phone)

        assert driver.find_element(*Order.HEADER).text == 'Хотите оформить заказ?\n '






