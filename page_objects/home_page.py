from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsHomePage


class HomePageScooter:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_subheader(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsHomePage.list_subheader))

    def answer_on_question(self, question_locator, answer_locator):
        element = self.driver.find_element(*question_locator)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(question_locator))
        element.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(answer_locator))

        return self.driver.find_element(*answer_locator).text
