import time

from Check_out_page.Pages.product_page import ProductPage
from Check_out_page.Pages.checkout_page import CheckoutPage
from Check_out_page.Pages.order_details_page import OrderDetailsPage
from Check_out_page.Pages.orders_page import OrdersPage
from datetime import date, timedelta

def test_checkout(driver):
    product_page = ProductPage(driver)
    product_page.open()
    product_page.add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open()
    checkout_page.fill_form(
        first_name="Fname",
        last_name="Lname",
        country="India",
        address="123 abc",
        city="Calicut",
        state="Kerala",
        postcode="673016",
        phonenumber="1234567",
        email="test@example.com",
        delivery_date=(date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
    )

    checkout_page.select_second_delivery_time_option()


    order_details_page = OrderDetailsPage(driver)
    assert order_details_page, "Thank you. Your order has been received."


    orders_page = OrdersPage(driver)
    orders_page.open()
    #orders_page.view_order()
    time.sleep(90)

