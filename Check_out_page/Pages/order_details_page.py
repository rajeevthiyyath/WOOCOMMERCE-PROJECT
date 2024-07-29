from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class OrderDetailsPage:
    BILLING_DETAILS_SECTION = (By.CLASS_NAME, "woocommerce-order-details__title")

    def __init__(self, driver):
        self.driver = driver

    def get_order_details(self):
        order_details_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BILLING_DETAILS_SECTION)
        )
        return order_details_element.text

    def parse_order_details(self, order_details_text):
        details = {}
        for line in order_details_text.split('\n'):
            if ":" in line:
                key, value = line.split(":", 1)
                details[key.strip()] = value.strip()
        return details