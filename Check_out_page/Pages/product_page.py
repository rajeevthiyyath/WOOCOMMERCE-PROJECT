from selenium.webdriver.common.by import By


class ProductPage:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "single_add_to_cart_button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/product/cap")

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()