from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsOrderPage


class OrderPageScooter:

    def __init__(self, driver, order):
        self.driver = driver
        self.name = order.name
        self.surname = order.surname
        self.address = order.address
        self.station = order.station
        self.telephone = order.telephone
        self.date = order.date
        self.rental_period = order.rental_period
        self.color = order.color
        self.comment = order.comment

    def wait_for_load_order_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPage.order_header))

    def set_name(self):
        self.driver.find_element(*LocatorsOrderPage.name_field).send_keys(self.name)

    def set_surname(self):
        self.driver.find_element(*LocatorsOrderPage.surname_field).send_keys(self.surname)

    def set_address(self):
        self.driver.find_element(*LocatorsOrderPage.address_field).send_keys(self.address)

    def choose_station(self):
        self.driver.find_element(*LocatorsOrderPage.station_field_1).click()
        self.driver.find_element(*LocatorsOrderPage.station_field_2).send_keys(self.station)
        elements = self.driver.find_elements(*LocatorsOrderPage.station_field_3)
        for element in elements:
            while element.text == self.station:
                self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
                element.click()
                break

    def set_telephone(self):
        self.driver.find_element(*LocatorsOrderPage.telephone_field).send_keys(self.telephone)

    def click_sign_in_button(self):
        self.driver.find_element(*LocatorsOrderPage.order_button_next).click()

    def set_date(self):
        self.driver.find_element(*LocatorsOrderPage.date_field).click()
        day_str = str(int(self.driver.find_element(*LocatorsOrderPage.current_day).text) + self.date)
        self.driver.find_element(By.XPATH, f".//div[text()={day_str}]").click()

    def choose_rental_period(self):
        self.driver.find_element(*LocatorsOrderPage.rental_period_field).click()
        self.driver.find_element(By.XPATH, f".//div[text()='{self.rental_period}']").click()

    def choose_color(self):
        self.driver.find_element(*LocatorsOrderPage.color_field).click()
        self.driver.find_element(By.ID, f"{self.color}").click()

    def set_comment(self):
        self.driver.find_element(*LocatorsOrderPage.comment_field).send_keys(self.comment)

    def click_sign_in_button2(self):
        self.driver.find_elements(*LocatorsOrderPage.order_button_final)[1].click()

    def wait_for_load_pop_up_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(LocatorsOrderPage.pop_up_window))

    def make_order(self):
        self.wait_for_load_order_header()
        self.set_name()
        self.set_surname()
        self.set_address()
        self.choose_station()
        self.set_telephone()
        self.click_sign_in_button()
        self.wait_for_load_order_header()
        self.set_date()
        self.choose_rental_period()
        self.choose_color()
        self.set_comment()
        self.click_sign_in_button2()
        self.wait_for_load_pop_up_window()
