import pytest
from selenium import webdriver
from data import Order1, Order2


@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver

    yield

    driver.quit()


@pytest.fixture(params=["data1", "data2"],scope="class")
def order(request, driver):
    if request.param == "data1":
        order = Order1()
    if request.param == "data2":
        order = Order2()

    request.cls.order = order
