import pytest
from Validation.Pages.product_page import ProductPage




def test_field_validation(browser):
    product_page = ProductPage(browser)
    product_page.open()

    product_page.select_color('Red')
    product_page.select_orientation('Landscape')
    product_page.enter_description('Profile Description')
    product_page.check_phone_checkbox()
    product_page.enter_phone_number('abcdefgh')
    product_page.upload_logo(r"C:\Users\DELL\Downloads\Cris.jpg")
    product_page.click_add_to_cart()

    validation_messages = product_page.get_validation_messages()
    assert any('is not a valid number' in message for message in validation_messages)