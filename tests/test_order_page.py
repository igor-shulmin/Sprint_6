import allure
import pytest
from locators import LocatorsOrderPage
from page_objects.order_page import OrderPageScooter
from data import Url


@pytest.mark.usefixtures('driver', 'order')
class TestOrderPage:

    @allure.title('Проверка функции оформления заказа')
    @pytest.mark.parametrize('locator', [LocatorsOrderPage.order_button_up, LocatorsOrderPage.order_button_down])
    def test_check_order(self, locator):
        order_page = OrderPageScooter(self.driver, self.order)

        order_page.go_to_site()
        element = order_page.driver_find_element(locator)
        order_page.driver_scroll_to_element(element)
        order_page.driver_wait_for_clickable_element(locator)
        order_page.driver_click_element(element)

        order_page.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)
        order_page.make_order()

        assert order_page.driver_find_element(LocatorsOrderPage.pop_up_window)

    @allure.title('Проверка перехода на главную страницу при клике на логотип сайта')
    def test_check_from_logo_samokat_to_home_page(self):
        order_page = OrderPageScooter(self.driver, self.order)

        order_page.go_to_site()
        element = order_page.driver_find_element(LocatorsOrderPage.order_button_up)
        order_page.driver_click_element(element)
        order_page.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)
        order_page.make_order()

        element = order_page.driver_find_element(LocatorsOrderPage.order_button_not)
        order_page.driver_click_element(element)
        element = order_page.driver_find_element(LocatorsOrderPage.logo_scooter)
        order_page.driver_click_element(element)
        order_page.driver_wait_for_visibile_element(LocatorsOrderPage.logo_scooter)

        assert self.driver.current_url == Url.url_home_page

    @allure.title('Проверка перехода на главную страницу Дзена при клике на логотип "Яндекса"')
    def test_check_from_logo_yandex_to_dzen(self):
        order_page = OrderPageScooter(self.driver, self.order)

        order_page.go_to_site()
        element = order_page.driver_find_element(LocatorsOrderPage.order_button_up)
        order_page.driver_click_element(element)
        order_page.driver_wait_for_visibile_element(LocatorsOrderPage.order_header)
        order_page.make_order()

        element = order_page.driver_find_element(LocatorsOrderPage.order_button_not)
        order_page.driver_click_element(element)
        element = order_page.driver_find_element(LocatorsOrderPage.logo_yandex)
        order_page.driver_click_element(element)

        order_page.driver_switch_to_window()
        order_page.driver_wait_for_visibile_element(LocatorsOrderPage.logo_dzen)

        assert self.driver.current_url == Url.url_dzen
