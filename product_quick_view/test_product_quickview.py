import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from product_quick_view.shop_page import ShopPage  # Ensure these imports match your directory structure
from product_quick_view.quickview_modal import QuickViewModal


import time

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()

    # Use the Service class to specify the WebDriver path
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_product_quickview(driver):
    shop_page = ShopPage(driver)
    quickview_modal = QuickViewModal(driver)

    shop_page.load()
    shop_page.click_quick_view("RF ID Card")

    quickview_modal.select_variation_color("Red")
    quickview_modal.select_variation_orientation("Landscape")
    quickview_modal.enter_profile_description("This is a test description.")
    quickview_modal.check_add_phone_number()
    quickview_modal.enter_phone_number("9876543210")
    quickview_modal.upload_logo(r"C:\Users\DELL\Downloads\Cris.jpg")  # Ensure you use the correct path
    quickview_modal.select_border1()
    quickview_modal.select_borders2()

    quickview_modal.add_to_cart()
    time.sleep(10)
    assert quickview_modal.is_product_added_to_cart(), "“RF ID Card” has been added to your cart"