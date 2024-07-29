from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from Validation.Pages.base_page import BasePage

class ProductPage(BasePage):
    URL = 'https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card'

    COLOR_DROPDOWN = (By.ID, 'color')
    ORIENTATION_DROPDOWN = (By.ID, 'orientation')
    DESCRIPTION_FIELD = (By.ID, 'profile_desc')
    PHONE_CHECKBOX = (By.ID, 'phone_number_checkbox')
    PHONE_FIELD = (By.ID, 'phone_number_field')
    ADDITIONAL_ELEMENTS_LOGO = (By.ID, 'logo')
    ADDITIONAL_ELEMENTS_BORDER = (By.ID, 'border')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'single_add_to_cart_button')
    VALIDATION_MESSAGES = (By.CSS_SELECTOR, '.woocommerce-error li')

    def open(self):
        self.open_url(self.URL)

    def select_color(self, color):
        color_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COLOR_DROPDOWN)
        )
        select = Select(color_element)
        select.select_by_visible_text(color)

    def select_orientation(self, orientation):
        orientation_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ORIENTATION_DROPDOWN)
        )
        select = Select(orientation_element)
        select.select_by_visible_text(orientation)

    def enter_description(self, description):
        description_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DESCRIPTION_FIELD)
        )
        description_field.send_keys(description)

    def check_phone_checkbox(self):
        phone_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHONE_CHECKBOX)
        )
        phone_checkbox.click()

    def enter_phone_number(self, phone):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHONE_FIELD)
        )
        phone_field.send_keys(phone)

    def select_additional_elements(self):
        logo_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ADDITIONAL_ELEMENTS_LOGO)
        )
        logo_element.click()

        border_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ADDITIONAL_ELEMENTS_BORDER)
        )
        border_element.click()

    def upload_logo(self, file_path):
        logo_upload_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ADDITIONAL_ELEMENTS_LOGO)
        )
        logo_upload_element.send_keys(file_path)

    def click_add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_button.click()

    def get_validation_messages(self):
        validation_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.VALIDATION_MESSAGES)
        )
        return [element.text for element in validation_elements]
