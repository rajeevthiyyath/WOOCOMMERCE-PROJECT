from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os



class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.color_select = (By.ID, "color")
        self.orientation_select = (By.ID, "orientation")
        self.description_field = (By.ID, "profile_desc")
        self.phone_checkbox = (By.ID, "phone_number_checkbox")
        self.phone_field = (By.ID, "phone_number_field")
        self.upload_logo_locator = (By.ID, "logo")
        self.border_double = (By.ID, "border_double")
        self.border_dashed = (By.ID, "border_dashed")
        self.add_to_cart_button = (By.CLASS_NAME, "single_add_to_cart_button")
        self.cart_success_message = (By.CLASS_NAME, "woocommerce-message")

    def open(self, url):
        self.driver.get(url)

    def select_color(self, color):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.color_select)
        )
        element.click()
        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{color}']"))
        )
        option.click()

    def select_orientation(self, orientation):
        element = self.driver.find_element(*self.orientation_select)
        element.click()
        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//option[text()='{orientation}']"))
        )
        option.click()

    def enter_description(self, description):
        element = self.driver.find_element(*self.description_field)
        element.send_keys(description)

    def check_phone_checkbox(self):
        element = self.driver.find_element(*self.phone_checkbox)
        if not element.is_selected():
            element.click()

    def enter_phone_number(self, phone_number):
        element = self.driver.find_element(*self.phone_field)
        element.send_keys(phone_number)



    def upload_logo(self, file_path):
        element = self.driver.find_element(*self.upload_logo_locator)
        element.send_keys(file_path)

    def select_borders(self, borders):
        for border in borders:
            border_element = self.driver.find_element(By.ID, border)
            if not border_element.is_selected():
                border_element.click()

    def add_to_cart(self):
        element = self.driver.find_element(*self.add_to_cart_button)
        element.click()

    def is_product_added_to_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_success_message)
        ).is_displayed()