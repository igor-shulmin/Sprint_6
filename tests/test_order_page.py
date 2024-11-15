import pytest
from locators import LocatorsOrderPage
from page_objects.order_page import OrderPageScooter
from data import Url
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('driver', 'order')
class TestOrderPage:

    @pytest.mark.parametrize('locator', [LocatorsOrderPage.order_button_up, LocatorsOrderPage.order_button_down])
    def test_check_order(self, locator):
        self.driver.get(Url.url_home_page)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

        order_page = OrderPageScooter(self.driver, self.order)
        order_page.wait_for_load_order_header()
        order_page.make_order()

        assert self.driver.find_element(*LocatorsOrderPage.pop_up_window)

    def test_check_from_logo_samokat_to_home_page(self):
        self.driver.get(Url.url_home_page)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsOrderPage.order_button_up))
        self.driver.find_element(*LocatorsOrderPage.order_button_up).click()

        order_page = OrderPageScooter(self.driver, self.order)
        order_page.wait_for_load_order_header()
        order_page.make_order()

        self.driver.find_element(*LocatorsOrderPage.order_button_not).click()
        self.driver.find_element(*LocatorsOrderPage.logo_scooter).click()

        assert self.driver.current_url == Url.url_home_page

    def test_check_from_logo_yandex_to_dzen(self):
        self.driver.get(Url.url_home_page)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsOrderPage.order_button_up))
        self.driver.find_element(*LocatorsOrderPage.order_button_up).click()

        order_page = OrderPageScooter(self.driver, self.order)
        order_page.wait_for_load_order_header()
        order_page.make_order()

        self.driver.find_element(*LocatorsOrderPage.order_button_not).click()
        self.driver.find_element(*LocatorsOrderPage.logo_yandex).click()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPage.logo_dzen))

        assert self.driver.current_url == Url.url_dzen
