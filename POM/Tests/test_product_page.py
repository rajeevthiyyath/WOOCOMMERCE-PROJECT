import pytest
from selenium import webdriver
from POMdemo.Pages.product_page import ProductPage  # Ensure the correct import path
import os
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_product_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.open("https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card")

    product_page.select_color("Red")
    product_page.select_orientation("Landscape")
    product_page.enter_description("Description")
    product_page.check_phone_checkbox()
    product_page.enter_phone_number("9876543210")
    # Make sure to provide the correct path to the file
    file_path = os.path.abspath(r"C:\Users\DELL\Downloads\Cris.jpg")
    product_page.upload_logo(file_path)

    product_page.select_borders(["border_double", "border_dashed"])
    product_page.add_to_cart()

    assert product_page.is_product_added_to_cart()
    time.sleep(30)
