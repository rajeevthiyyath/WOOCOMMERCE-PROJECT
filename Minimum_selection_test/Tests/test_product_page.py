import pytest
from selenium import webdriver

from Minimum_selection_test.Pages.product_page import ProductPage
import os


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Or any other driver you are using
    yield driver
    driver.quit()


def test_minimum_selection(driver):
    product_page = ProductPage(driver)
    product_page.open("https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card")

    product_page.select_color("Red")
    product_page.select_orientation("Landscape")
    product_page.enter_description("This is a sample description under 100 characters.")
    product_page.check_phone_checkbox()
    product_page.enter_phone_number('9999999')


    file_path = os.path.abspath(r"C:\Users\DELL\Downloads\Cris.jpg")
    product_page.upload_logo(file_path)


    product_page.select_border("border_double")
    product_page.add_to_cart()

    notice_message = product_page.get_notice_message()
    assert "make at least 2 selections." in notice_message.lower()
