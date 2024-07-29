from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.color_select = (By.XPATH, "//li[@data-value='Red']")
        self.orientation_select = (By.XPATH, "//li[@data-value='Landscape']")
        self.phone_checkbox = (By.ID, 'phone_number_checkbox')
        self.PHONE_FIELD = (By.ID, 'phone_number_field')
        self.description_field = (By.ID, "profile_desc")
        self.upload_logo_locator = (By.ID, "logo")
        self.border_double = (By.ID, "border_double")
        self.add_to_cart_button = (By.CLASS_NAME, "single_add_to_cart_button")
        self.notice = (By.CSS_SELECTOR, ".woocommerce-error li")

    def open(self, url):
        self.driver.get(url)

    def select_color(self, color):
        color_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//li[@data-value='{color}']"))
        )
        color_element.click()

    def select_orientation(self, orientation):
        orientation_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//li[@data-value='{orientation}']"))
        )
        orientation_element.click()

    def enter_description(self, description):
        description_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.description_field)
        )
        description_field.send_keys(description)

    def check_phone_checkbox(self):
        phone_checkbox_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.phone_checkbox)
        )
        phone_checkbox_element.click()

    def enter_phone_number(self, phone):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHONE_FIELD)
        )
        phone_field.send_keys(phone)

    def upload_logo(self, file_path):
        logo_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.upload_logo_locator)
        )
        logo_element.send_keys(file_path)

    def select_border(self, border_id):
        border_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, border_id))
        )
        if not border_element.is_selected():
            border_element.click()

    def add_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_to_cart_button.click()

    def get_notice_message(self):
        notice_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.notice)
        )
        return notice_element.text